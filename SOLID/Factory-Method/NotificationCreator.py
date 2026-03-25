from abc import ABC, abstractmethod
from .Notification import Notification

class NotificationCreater:

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send(self, message: str) -> None:
        notification = self.create_notification()
        notification.send(message)

        