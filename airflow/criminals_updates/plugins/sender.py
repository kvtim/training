import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

from criminal import Criminal


class Sender:
    def __init__(self, new: List[Criminal], updated: List[Criminal], deleted: List[Criminal]):
        self.new = new
        self.updated = updated
        self.deleted = deleted

    def send_email(self, sender, password, recipients):        
        message = MIMEMultipart('alternative')
        message['From'] = f"FBI <{sender}>"
        message['Subject'] = "WANTED!"

        msg_content = MIMEText(self.__create_html(), 'html')

        message.attach(msg_content)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(sender, password)
        server.sendmail(sender, recipients, message.as_string())

    def __create_html(self):
        new_text = self.__join_criminals(self.new)
        updated_text = self.__join_criminals(self.updated)
        deleted_text = self.__join_criminals(self.deleted)

        return f"""  
        <html>
        <head></head>
        <body>
        <h1>FBI</h1>
        <h2>WANTED</h2>
        <p>By Artem Kozlovski</p>
        <a href="https://github.com/kvtim/training/tree/main/airflow/criminals_updates">Code and logs<a/>
        <h3>New:</h3>
        {new_text if new_text else '<p>There are no such</p>'}
        <h3>Updated:</h3>
        {updated_text if updated_text else '<p>There are no such</p>'}
        <h3>Deleted:</h3>
        {deleted_text if deleted_text else '<p>There are no such</p>'}
        </body>
        </html>"""

    @staticmethod
    def __join_criminals(criminals):
        return ''.join([
            f'''
            <ul>
                <li>
                    <h4>uid:</h4>
                    <p>{criminal.id}</p>
                </li>
                <li>
                    <h4>Fullname:</h4>
                    <p>{criminal.fullname}</p>
                </li>
                <li>
                    <h4>Description:</h4>
                    <p>{criminal.description}</p>
                </li>
                <li>
                    <a href="{criminal.url}">see more<a/>
                </li>
            </ul>
            <hr></hr>'''
            for criminal in criminals
        ])

