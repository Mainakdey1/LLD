from abc import ABC

class Notification(ABC):
    @staticmethod
    def send(self, message: str) -> None:
        pass

