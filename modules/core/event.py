from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, event_type: str, data: dict) -> None:
        """Receive update from subject."""


class EventManager:
    def __init__(self) -> None:
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        self.__observers.remove(observer)

    def notify(self, event_type: str, data: dict) -> None:
        """Notify all observers about an event."""
        for observer in self.__observers:
            observer.update(event_type, data)
