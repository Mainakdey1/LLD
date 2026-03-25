from .Notification import Notification

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f'Sending email{message}')

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f'Sending email{message}')

class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f'Sending email{message}')
