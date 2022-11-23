from Class.DB import DBAccess as DB
from Class.Car import Car
from Class.Customer import Customer
import sqlite3 as sql
import sys


class Deal(DB):
    def __init__(self) -> None:
        self.idCar = 0
        self.idCustomer = 0
        self.isRent = 0
        self.dateStartRent = ""
        self.durationDaysRent = 0
        self.car = {}
        self.customer = {}

    @staticmethod
    def NameTable() -> str:
        # Return the name table
        return "Deal"

    @staticmethod
    def IdColumn() -> str:
        # Return the id column
        return "id"

    def InsertDB(self) -> bool:
        cursor, dbConnection = DB.DBCursor()
        if cursor is not None:
            try:
                query = f"INSERT INTO Deal (isRent, dateStartRent, durationDaysRent, idCar, idCustomer) " \
                        f"VALUES ({self.isRent}, '{self.dateStartRent}', {self.durationDaysRent},{self.idCar}, " \
                        f"{self.idCustomer})"
                cursor.execute(query)
                dbConnection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBDeal {sys.exc_info()}")
            finally:
                DB.DBClose(cursor)
        return None

    @staticmethod
    def GetAll() -> list:
        cursor = Deal.DBCursor()[0]
        dealList = []
        if cursor is not None:
            try:
                cursor.execute(f"SELECT * FROM {Deal.NameTable()}")
                resultsQuery = cursor.fetchall()
                for row in resultsQuery:
                    newDeal = Deal.LoadResults(cursor, row)
                    newDeal.car = Car.GetCar(newDeal.idCar)
                    newDeal.customer = Customer.GetCustomer(newDeal.idCustomer)
                    dealList.append(newDeal)
                return dealList
            except sql.OperationalError:
                print(f"Error in GetAllDeal {sys.exc_info()}")
            finally:
                Deal.DBClose(cursor)
        return None
