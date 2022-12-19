from main_project.classes.deal import Deal
from main_project.classes.car import Car
from main_project.classes.customer import Customer
import sqlite3 as sql
import sys


class HistoricDeal(Deal):
    """
    It manages all the methods for historic utilities
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the historic table in the database
        :returns: The name of the historic table in the database
        """
        return "historic_deal"

    @staticmethod
    def get_all() -> list | None:
        """
        This function get all the historic deals from the database
        :returns: A list of all the historic deals
        """
        cursor: sql.dbapi2.Cursor = HistoricDeal.db_cursor()[0]
        deal_list: list = []
        if cursor:
            try:
                query: str = f"SELECT * FROM historic_deal order by id"
                cursor.execute(query)
                results_query: list = cursor.fetchall()
                for row in results_query:
                    new_historical_deal: HistoricDeal = HistoricDeal.load_results(cursor, row)
                    new_historical_deal.car = Car.get_car(new_historical_deal.id_car)
                    new_historical_deal.customer = Customer.get_customer(new_historical_deal.id_customer)
                    deal_list.append(new_historical_deal)
                return deal_list
            except sql.OperationalError:
                print(f"Error in get_all_deal_historic {sys.exc_info()}")
            finally:
                Deal.db_close(cursor)
        return None
