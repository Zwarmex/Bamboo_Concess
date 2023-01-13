from main_project.classes.database import DBAccess as Db
import sqlite3 as sql
import sys

class Brand(Db):
    """
    It manages all the methods for brands utilities
    """

    def __init__(self, name: str = "") -> None:
        """
        It creates a new object Brand
        """
        self.id: int = 0
        self.name: str = name

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

    def insert_db(self) -> bool:
        """
        This function insert in the database a new brand
        :returns: True if the insert was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = (f"INSERT INTO brand (name) "
                              f"VALUES ('{self.name}')")
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBBrand {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False


class Motor(Db):
    """
    It manages all the methods for motors utilities
    """

    def __init__(self, name: str = "") -> None:
        """
        It creates a new object Motor
        """
        self.id: int = 0
        self.name: str = name

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

    def insert_db(self) -> bool:
        """
        This function insert in the database a new motor
        :returns: True if the insert was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = (f"INSERT INTO motor (name) "
                              f"VALUES ('{self.name}')")
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBMotor {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False

class Type(Db):
    """
    It manages all the methods for types utilities
    """

    def __init__(self, name: str = "") -> None:
        """
        It creates a new object Type
        """
        self.id: int = 0
        self.name: str = name

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

    def insert_db(self) -> bool:
        """
        This function insert in the database a new brand
        :returns: True if the insert was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = (f"INSERT INTO type (name) "
                              f"VALUES ('{self.name}')")
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBBrand {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False
