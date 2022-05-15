import math
import os
from typing import List
import requests
from criminal import Criminal
from crud import CRUD
from sender import Sender


class CriminalsUpdates:
    def __init__(self, sender, password, recipients):
        self.__crud = CRUD() 
        self.sender = sender
        self.password = password
        self.recipients = recipients


    @staticmethod
    def get_criminals() -> List[Criminal]:
        items_on_page = 50
        items_count = requests.get(
            'https://api.fbi.gov/@wanted?pageSize=1&page=1').json()['total']
        pages_count = math.ceil(items_count / items_on_page)

        return [
            Criminal(
                criminal['uid'],
                criminal['title'],
                criminal['description'],
                criminal['url']
            )
            for page in range(1, pages_count + 1)
            for criminal in requests.get(f'https://api.fbi.gov/@wanted?pageSize={items_on_page}&page={page}'
                                         f'&sort_on=publication&sort_order=asc').json()['items']]

    def find_criminals_updates(self) -> List[List[Criminal]]:
        new_criminals = self.get_criminals()

        if not os.path.exists('criminals.sqlite'):
            self.__crud.create_criminals(new_criminals)
            return [[], [], []]

        old_criminals = self.__crud.select_criminals()

        created = [new for new in new_criminals if new.id not in [
            old.id for old in old_criminals]]
        updated = []
        deleted = []

        for new in created:
            self.__crud.insert_criminal(new)

        for old in old_criminals:
            exists = False
            for new in new_criminals:
                if old.id == new.id:
                    exists = True
                    if (old.fullname != new.fullname or
                            old.description != new.description or
                            old.url != new.url):
                        self.__crud.update_criminal(new)
                        updated.append(new)

            if exists is False:
                self.__crud.delete_criminal(old)
                deleted.append(old)

        return [created, updated, deleted]

    def send_criminals_updates(self):
        criminals_updates = self.find_criminals_updates()
        sender = Sender(
            criminals_updates[0], criminals_updates[1], criminals_updates[2])
        sender.send_email(self.sender, self.password, self.recipients)
