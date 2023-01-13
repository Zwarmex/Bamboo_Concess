from main_project.classes.database import DBAccess as Db
from main_project.classes.car import Car
from main_project.classes.customer import Customer
import sqlite3 as sql
import sys
from datetime import datetime, timedelta


class Deal(Db):
    """
    It manages all the methods for deals utilities
    """

    def __init__(self, id_car: int = 0, id_customer: int = 0, is_rent: bool = False, date_start_rent: str = "",
                 duration_days_rent: int = 0) -> None:
        """
        It creates a new object Deal
        """
        self.id: int = 0
        self.id_car: int = id_car
        self.id_customer: int = id_customer
        self.is_rent: bool = is_rent
        self.date_start_rent: str = date_start_rent
        self.duration_days_rent: int = duration_days_rent
        self.car: Car = Car()
        self.customer: Customer = Customer()

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the deal table in the database
        :returns: The name of the deal table in the database
        """
        return "deal"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the deal table in the database
        :returns: The name of the primary key in the deal table in the database
        """
        return "id"

    def insert_db(self) -> bool:
        """
        This function insert in the database a new deal
        :returns: True if the insert was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor:
            try:
                query: str = (f"INSERT INTO deal (is_rent, id_car, id_customer)"
                              f"VALUES ({self.is_rent}, {self.id_car}, {self.id_customer})")
                if self.is_rent:
                    query: str = (f"INSERT INTO deal "
                                  f"(is_rent, date_start_rent, duration_days_rent, id_car, id_customer) "
                                  f"VALUES ({self.is_rent}, '{self.date_start_rent}', {self.duration_days_rent}, "
                                  f"{self.id_car}, {self.id_customer})")
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBDeal {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False

    def remove_db(self) -> bool:
        """
        This function delete the deal in the database
        :returns: True if the deleting was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor:
            try:
                query: str = f"DELETE FROM deal WHERE id = {self.id}"
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in check_rent {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False

    def check_rent(self) -> bool:
        """
        It checks if the rent continue or is finished
        :returns: True if the rent is finished
        """
        if self.is_rent:
            if (datetime.today() - (datetime.strptime(self.date_start_rent, "%d/%m/%Y") +
                                    timedelta(days=self.duration_days_rent))).days >= 0:
                return self.remove_db()
        return False

    @staticmethod
    def get_all() -> list | None:
        """
        This function get all the deals from the database
        :returns: A list of all the deals
        """
        cursor: sql.dbapi2.Cursor = Deal.db_cursor()[0]
        deal_list: list = []
        if cursor:
            try:
                query: str = f"SELECT * FROM deal"
                cursor.execute(query)
                results_query: list = cursor.fetchall()
                for row in results_query:
                    new_deal: Deal = Deal.load_results(cursor, row)
                    new_deal.car = Car.get_car(new_deal.id_car)
                    new_deal.customer = Customer.get_customer(new_deal.id_customer)
                    if new_deal.check_rent():
                        new_deal.is_rent = 0
                        new_deal.date_start_rent = ""
                        new_deal.duration_days_rent = 0
                    deal_list.append(new_deal)
                return deal_list
            except sql.OperationalError:
                print(f"Error in GetAllDeal {sys.exc_info()}")
            finally:
                Deal.db_close(cursor)
        return None
