from modules.core.event import Observer


class MailObserver(Observer):
    def update(self, event_type: str, data: dict) -> None:
        print(
            f"""
    {self.__class__.__name__}: This is a Mail event
    {event_type=}
    {data=}
    """
        )
