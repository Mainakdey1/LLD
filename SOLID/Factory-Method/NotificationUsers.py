from .NotificationCreator import NotificationCreater
from .Notification import Notification
from .notification_services import EmailNotification, SMSNotification, PushNotification

class EmailNotificationCreator(NotificationCreater):
    def create_notification(self) -> Notification:
        return EmailNotification()
    

class SMSNotificationCreator(NotificationCreater):
    def create_notification(self) -> Notification:
        return SMSNotification
    
class PushNotificationCreator(NotificationCreater):
    def create_notification(self) -> Notification:
        return PushNotification