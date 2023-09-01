from modules.core.event import Observer
from modules.core.log import logger


class LogObserver(Observer):
    def __init__(self) -> None:
        self.log = logger.getChild(self.__class__.__name__)
        self.log.setLevel("INFO")

    def update(self, event_type: str, data: dict) -> None:
        self.log.info(
            f"""
    {self.__class__.__name__}: This is a Log event
    {event_type=}
    {data=}
    """
        )
