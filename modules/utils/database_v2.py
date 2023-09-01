class IdentifierAlreadyExistsError(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "The identifier already exists on the database"
        if not args:
            args = (default_message,)
        super().__init__(*args)


class IdentifierNotExistsError(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "The identifier not exists on the database"
        if not args:
            args = (default_message,)
        super().__init__(*args)


class FieldNotExistsError(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "The field not exists on the record"
        if not args:
            args = (default_message,)
        super().__init__(*args)


class Database:
    def __init__(self) -> None:
        self.__db = {}

    def add_record(self, identifier: str, data: dict) -> None:
        if identifier in self.__db:
            raise IdentifierAlreadyExistsError
        self.__db.update({identifier: data})

    def del_record(self, identifier: str) -> None:
        if identifier not in self.__db:
            raise IdentifierNotExistsError
        self.__db.pop(identifier)

    def get_record(self, identifier: str) -> dict:
        if identifier not in self.__db:
            raise IdentifierNotExistsError
        return self.__db[identifier]

    def get_all_records(self) -> dict:
        return self.__db

    def get_record_field(self, identifier: str, field: str) -> str:
        record = self.get_record(identifier)
        if field not in record:
            raise FieldNotExistsError
        return record[field]
