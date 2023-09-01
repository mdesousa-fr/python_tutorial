from modules.core.event import Observer


class SlackObserver(Observer):
    def update(self, event_type: str, data: dict) -> None:
        match event_type:
            case "register":
                print(
                    f"{self.__class__.__name__}: The user {data['username']} have been registered!"
                )
            case "unregister":
                print(
                    f"{self.__class__.__name__}: The user {data['username']} have quit"
                )
