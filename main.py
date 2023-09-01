def event_tutorial() -> None:
    from faker import Faker

    from modules.core.event import EventManager
    from modules.observer.log import LogObserver
    from modules.observer.mail import MailObserver
    from modules.observer.slack import SlackObserver

    class RegistrationService:
        def __init__(self) -> None:
            self.event_manager = EventManager()

        def register(self, username: str) -> None:
            event_type = "register"
            # Business logic
            self.event_manager.notify(event_type, {"username": username})

        def unregister(self, username: str) -> None:
            event_type = "unregister"
            # Business logic
            self.event_manager.notify(event_type, {"username": username})

    fake = Faker()

    service = RegistrationService()
    log_observer = LogObserver()
    mail_observer = MailObserver()
    slack_observer = SlackObserver()

    service.event_manager.attach(log_observer)
    service.event_manager.attach(mail_observer)
    service.event_manager.attach(slack_observer)

    for _ in range(2):
        service.register(fake.simple_profile()["username"])
        service.unregister(fake.simple_profile()["username"])


def logging_tutorial() -> None:
    from modules.core.log import logger

    def print_log_messages(log) -> None:
        log.debug("🐶")
        log.info("👀")
        log.warning("😮")
        log.error("😰")
        log.critical("🤬")

    # Get a logger which is a descendant to the root one
    log = logger.getChild("tutorial")
    print("--- Default log level ---")
    print_log_messages(log)

    print("\n--- Set log level to DEBUG ---")
    log.setLevel("DEBUG")
    print_log_messages(log)

    print("\n--- Use a child logger ---")
    log2 = log.getChild("subprocess")
    log2.setLevel("ERROR")
    print_log_messages(log2)


def exception_tutorial() -> None:
    from modules.utils import database

    jdoe = {"username": "@jdoe", "mail": "jdoe@example.com"}
    adoe = {"username": "@adoe", "mail": "adoe@example.com"}

    def add_record_without_exception(data: dict) -> None:
        if not database.add_record_without_exception(data["username"], data):
            print("The record already exists")
        else:
            print("The record have been registered")

    def add_record_with_exception(data: dict) -> None:
        try:
            database.add_record_with_exception(data["username"], data)
            print("The record have been registered")
        except database.IdentifierAlreadyExistsError:
            print("The record already exists")
        except Exception:
            print("Unexpected error")

    print("--- Without exception ---")
    add_record_without_exception(jdoe)
    add_record_without_exception(jdoe)

    # The limits without exceptions ⬇️
    print(database.get_record_field_without_exception(jdoe["username"], "mail"))
    # This identifier not exists
    print(database.get_record_field_without_exception("anonymous", "mail"))
    # This field not exists
    print(database.get_record_field_without_exception(jdoe["username"], "email"))

    print("\n--- With exception ---")
    add_record_with_exception(adoe)
    add_record_with_exception(adoe)

    try:
        print(database.get_record_field_with_exception(adoe["username"], "mail"))
        print(database.get_record_field_with_exception("anonymous", "mail"))
    except Exception as error:  # Capture all exceptions (not recommended)
        print(error)

    try:
        print(database.get_record_field_with_exception(adoe["username"], "email"))
    except Exception as error:
        print(error)


def recursive_tutorial() -> None:
    import json

    import boto3.session

    def list_objects(bucket: str, continuation_token: str | None = None) -> list[str]:
        session = boto3.session.Session()
        client = session.client("s3")
        parameters = {"Bucket": bucket, "MaxKeys": 10}

        if continuation_token:
            parameters.update({"ContinuationToken": continuation_token})

        response = client.list_objects_v2(**parameters)

        # files = []
        # for key in response["Contents"]:
        #     files.append(key["Key"])

        files = [key["Key"] for key in response["Contents"]]

        if response["IsTruncated"]:
            continuation_token = response["NextContinuationToken"]
            files.extend(list_objects(bucket, continuation_token))

        return files

    print(json.dumps(list_objects("devsecops-701382299455"), indent=2))


def fun_with_classes() -> None:
    from faker import Faker

    fake = Faker()

    class User:
        def __init__(self) -> None:
            self.fname = fake.first_name()
            self.lname = fake.last_name()

        @property
        def username(self):
            return f"{self.fname[0]}.{self.lname}".lower()

    user = User()
    print(f"{user.fname=}")
    print(f"{user.lname=}")
    print(f"{user.username=}")


def fun_with_classes_advanced() -> None:
    import json

    from faker import Faker

    # Avoid using as except for common usage like -> import numpy as np
    from modules.utils import database_v2 as database

    fake = Faker()
    db = database.Database()

    for _ in range(5):
        (fname, lname) = fake.first_name(), fake.last_name()
        username = f"{fname}.{lname}".lower()
        mail = f"{username}@example.com"
        data = {"username": username, "mail": mail}
        db.add_record(data["username"], data)

    print(json.dumps(db.get_all_records(), indent=2))


def main():
    print("Hello, World!")
    # event_tutorial()
    # fun_with_classes()
    # fun_with_classes_advanced()
    # recursive_tutorial()
    # exception_tutorial()
    # logging_tutorial()


if __name__ == "__main__":
    main()
