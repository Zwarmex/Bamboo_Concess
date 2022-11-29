import sqlite3 as sql
import sys

from Main.Class.database import DBAccess as Db


class Customer(Db):
    def __init__(self) -> None:
        """
        It creates a new object Customer
        """
        self.id: int = 0
        self.first_name: str = ""
        self.last_name: str = ""
        self.phone: int | str = 0
        self.mail: str = ""
        self.address: str = ""

    @staticmethod
    def get_customer(id_customer: int) -> object | None:
        """
        This function get a customer from the database chosen by its id
        :param id_customer: An integer number
        :returns: A customer object
        """
        cursor: sql.dbapi2.Cursor = Customer.db_cursor()[0]
        if cursor is not None:
            try:
                query: str = f"SELECT * FROM customer WHERE id = {id_customer}"
                cursor.execute(query)
                new_customer: Customer = Customer.load_results(cursor, cursor.fetchone())
                return new_customer
            except sql.OperationalError:
                print(f"Error in GetCustomer : {sys.exc_info()}")
            finally:
                Customer.db_close(cursor)
        return None

    def insert_db(self) -> bool:
        """
        This function insert a customer in the database
        :returns: True if the insertion was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = f"INSERT INTO customer (first_name, last_name, phone, mail, address) " \
                        f"VALUES ('{self.first_name}', '{self.last_name}', {self.phone}, " \
                             f"'{self.mail}', '{self.address}')"
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDB Customer {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the customer table in the database
        :returns: The name of the customer table in the database
        """
        return "customer"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the customer table in the database
        :returns: The name of the primary key in the customer table in the database
        """
        return "id"
