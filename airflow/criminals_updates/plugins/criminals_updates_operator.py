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
        criminalsUpdates = CriminalsUpdates(self.sender, self.password, self.recipients)
        criminalsUpdates.send_criminals_updates()
        self.log.info("Sent")

    def execute(self, context):       
        self.send_email()
