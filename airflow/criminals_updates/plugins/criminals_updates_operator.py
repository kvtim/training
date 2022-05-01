from airflow.models.baseoperator import BaseOperator
from criminals_updates import CriminalsUpdates

class CriminalsUpdatesOperatop(BaseOperator):

    def __init__(
            self,
            sender,
            password,
            recipients,
            data_with_default_value = 'default',
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.sender = sender
        self.password = password
        self.recipients = recipients
        self.data_with_default_value = data_with_default_value

    def send_email(self):
        # from crud import CRUD
        # from criminal import Criminal
        # criminal_updates = CriminalsUpdates(self.sender, self.password, self.recipients)
        # crs = criminal_updates.get_criminals()
        # c = crs[500]
        # c.fullname = 'New fullname'
        # c.description = 'New description'
        # c.url = 'https://api.fbi.gov/docs#!/Wanted/get_wanted'
        # crud = CRUD()
        # crud.insert_criminal(Criminal('itsnewid', 'Some criminal', 'Very dangerous criminal',
        # 'https://api.fbi.gov/docs#!/Wanted/get_wanted'))
        # crud.update_criminal(c)
        # crud.delete_criminal(crs[28])
        # crud.delete_criminal(crs[909])
        
        criminalsUpdates = CriminalsUpdates(self.sender, self.password, self.recipients)
        criminalsUpdates.send_criminals_updates()
        self.log.info("Sent")

    def execute(self, context):       
        self.send_email()
