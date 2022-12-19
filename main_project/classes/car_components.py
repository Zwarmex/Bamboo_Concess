from main_project.classes.database import DBAccess as Db


class Brand(Db):
    """
    It manages all the methods for brands utilities
    """

    def __init__(self) -> None:
        """
        It creates a new object Brand
        """
        self.id: int = 0
        self.name: str = ""

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the brand table in the database
        :returns: The name of the brand table in the database
        """
        return "brand"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the brand table in the database
        :returns: The name of the primary key in the brand table in the database
        """
        return "id"


class Motor(Db):
    """
    It manages all the methods for motors utilities
    """

    def __init__(self) -> None:
        """
        It creates a new object Motor
        """
        self.id: int = 0
        self.name: str = ""

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the motor table in the database
        :returns: The name of the motor table in the database
        """
        return "motor"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the motor table in the database
        :returns: The name of the primary key in the motor table in the database
        """
        return "id"


class Type(Db):
    """
    It manages all the methods for types utilities
    """

    def __init__(self) -> None:
        """
        It creates a new object Type
        """
        self.id: int = 0
        self.name: str = ""

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the type table in the database
        :returns: The name of the type table in the database
        """
        return "type"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the type table in the database
        :returns: The name of the primary key in the type table in the database
        """
        return "id"
