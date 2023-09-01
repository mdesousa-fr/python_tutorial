__db = {}


class IdentifierAlreadyExistsError(Exception):
    """The identifier already exists on the database."""

    def __init__(self, *args: object) -> None:
        default_message = "The identifier already exists on the database"
        if not args:
            args = (default_message,)
        super().__init__(*args)


class IdentifierNotExistsError(Exception):
    """The identifier not exists on the database."""

    def __init__(self, *args: object) -> None:
        default_message = "The identifier not exists on the database"
        if not args:
            args = (default_message,)
        super().__init__(*args)


class FieldNotExistsError(Exception):
    """The field not exists on the record."""

    def __init__(self, *args: object) -> None:
        default_message = "The field not exists on the record"
        if not args:
            args = (default_message,)
        super().__init__(*args)


def add_record_without_exception(identifier: str, data: dict) -> bool:
    """Add record to the database.

    Args:
        identifier (str): Unique identifier of the data.
        data (dict): The data to store.

    Returns:
        bool: Returns False if the identifier already exists else it returns True.
    """
    if identifier in __db:
        return False
    __db.update({identifier: data})
    return True


def add_record_with_exception(identifier: str, data: dict) -> None:
    """Add record to the database.

    Args:
        identifier (str): Unique identifier of the data.
        data (dict): The data to store.

    Raises:
        IdentifierAlreadyExistsError: The identifier already exists on the database.
    """
    if identifier in __db:
        raise IdentifierAlreadyExistsError
    __db.update({identifier: data})


def del_record_without_exception(identifier: str) -> bool:
    """Delete record from the database.

    Args:
        identifier (str): Unique identifier of the data.

    Returns:
        bool: Returns False if the identifier not exists else it returns True.
    """
    if identifier not in __db:
        return False
    __db.pop(identifier)
    return True


def del_record_with_exception(identifier: str) -> None:
    """Delete record from the database.

    Args:
        identifier (str): Unique identifier of the data.

    Raises:
        IdentifierNotExistsError: The identifier not exists on the database.
    """
    if identifier not in __db:
        raise IdentifierNotExistsError
    __db.pop(identifier)


def get_record_without_exception(identifier: str) -> dict | None:
    """Get record from the database.

    Args:
        identifier (str): Unique identifier of the data.

    Returns:
        dict | None: Returns the data if it exists else return None.
    """
    if identifier not in __db:
        return None
    return __db[identifier]


def get_record_with_exception(identifier: str) -> dict:
    """Get record from the database.

    Args:
        identifier (str): Unique identifier of the data.

    Raises:
        IdentifierNotExistsError: The identifier not exists on the database.

    Returns:
        dict: Return the data.
    """
    if identifier not in __db:
        raise IdentifierNotExistsError
    return __db[identifier]


def get_record_field_without_exception(identifier: str, field: str) -> str | None:
    record = get_record_without_exception(identifier)
    if not record:
        return None
    if field not in record:
        return None
    return record[field]


def get_record_field_with_exception(identifier: str, field: str) -> str:
    record = get_record_with_exception(identifier)
    if field not in record:
        raise FieldNotExistsError
    return record[field]
