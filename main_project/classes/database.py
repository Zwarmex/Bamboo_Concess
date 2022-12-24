import sqlite3 as sql
import sys


class DBAccess:
    """
    It manages all the methods for general database utilities
    """

    @staticmethod
    def db_cursor() -> tuple | None:
        """
        This function get the connection and the cursor of the database
        :returns: The connection and the cursor of the database
        """
        try:
            db_connection: sql.dbapi2.Connection = sql.connect("./database/bamboo_concess.db")
            return db_connection.cursor(), db_connection
        except sql.OperationalError:
            print(f"Error in DBCursor {sys.exc_info()}")
            return None, None

    @staticmethod
    def db_close(cursor: sql.dbapi2.Cursor) -> None:
        """
        This function close a connection of the database chosen by its cursor
        :param cursor: A SQLITE3 object
        :returns: None
        """
        cursor.close()

    @classmethod
    def load_results(cls, cursor: sql.Cursor, data: list) -> any:
        """
        This function create a new object with the data
        :param cursor: A SQLITE3 object
        :param data: A list with all the data to create a new object
        :returns: A new cls object
        """
        new_instance = cls()
        counter: int = 0
        for columnName in cursor.description:
            setattr(new_instance, columnName[0], data[counter])
            counter += 1
        return new_instance

    @classmethod
    def get_all(cls) -> list | None:
        """
        This function get all the data from the database chosen by cls.
        :returns: A list of all the cls object from the database.
        """
        cursor: sql.dbapi2.Cursor = cls.db_cursor()[0]
        instances_list: list = []
        if cursor is not None:
            try:
                cursor.execute(f"SELECT * FROM {cls.name_table()}")
                results_query: list = cursor.fetchall()
                for row in results_query:
                    new_instance: object = cls.load_results(cursor, row)
                    instances_list.append(new_instance)
                return instances_list
            except sql.OperationalError:
                print(f"Error in GetAllDB {sys.exc_info()}")
            finally:
                cls.db_close(cursor)
        return None

    @classmethod
    def get_id(cls, name: str) -> int | None:
        """
        This function get the id from the row that the name matches
        :param name: A string of the name of a row in the database
        :returns: The id of the row checked with the name
        """
        tuple_db: tuple = cls.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor and name:
            try:
                query: str = f"SELECT {cls.id_column()} FROM {cls.name_table()} WHERE name = '{name}'"
                cursor.execute(query)
                result: tuple = cursor.fetchone()
                if not result:
                    query: str = f"INSERT INTO {cls.name_table()} (name) VALUES ('{name}')"
                    cursor.execute(query)
                    db_connection.commit()
                    cursor.execute("SELECT last_insert_rowid()")
                    result: tuple = cursor.fetchone()
                return result[0]
            except sql.OperationalError:
                print(f"Error in GetId {sys.exc_info()}")
            finally:
                cls.db_close(cursor)
        return None

    @classmethod
    def get_car_component(cls, id_car: int) -> any:
        """
        This function get a component of a car chosen by its id
        :param id_car: An integer number matches a car
        :returns: A new cls object
        """
        cursor: sql.dbapi2.Cursor = cls.db_cursor()[0]
        if cursor:
            try:
                query: str = f"SELECT {cls.name_table()}.id, {cls.name_table()}.name FROM {cls.name_table()} " \
                             f"JOIN car ON {cls.name_table()}.{cls.id_column()} = car.id_{cls.name_table()} " \
                             f"WHERE car.id = {id_car}"
                cursor.execute(query)
                return cls.load_results(cursor, cursor.fetchone())
            except sql.OperationalError:
                print(f"Error in GetCarComponent {sys.exc_info()}")
            finally:
                cls.db_close(cursor)
        return None
