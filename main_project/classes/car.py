from __future__ import annotations

import sqlite3 as sql
import sys

from main_project.classes.car_components import Brand, Type, Motor
from main_project.classes.database import DBAccess as Db


class Car(Db):
    """
    It manages all the methods for cars utilities
    """

    def __init__(self) -> None:
        """
        It creates a new object Car
        """
        self.id: int = 0
        self.date_stock: str = ""
        self.date_tech_control: str = ""
        self.price: int = 0
        self.promo: int = 0
        self.id_brand: int = 0
        self.id_type: int = 0
        self.id_motor: int = 0
        self.brand: Brand = Brand()
        self.motor: Motor = Motor()
        self.type: Type = Type()

    @staticmethod
    def name_table() -> str:
        """
        This function returns the name of the car table in the database
        :returns: The name of the car table in the database
        """
        return "car"

    @staticmethod
    def id_column() -> str:
        """
        This function returns the primary key name in the car table in the database
        :returns: The name of the primary key in the car table in the database
        """
        return "idCar"

    @staticmethod
    def get_car_list() -> list | None:
        """
        This function get the cars in the database
        :return: A list of cars from the database if found
        """
        car_list: list = []
        cursor: sql.dbapi2.Cursor = Db.db_cursor()[0]
        if cursor:
            try:
                query: str = (f"SELECT id, STRFTIME('%d/%m/%Y', date_stock) as date_stock, "
                              f"date_tech_control, price, promo FROM car "
                              f"WHERE id NOT IN (select id_car FROM deal WHERE is_rent = 0)")
                cursor.execute(query)
                results_query: list = cursor.fetchall()
                for row in results_query:
                    car: Car = Car.load_results(cursor, row)
                    car.get_components()
                    car_list.append(car)
                return car_list
            except sql.OperationalError:
                print(f"Error in GetCarList {sys.exc_info()}")
            finally:
                Db.db_close(cursor)
        return None

    @staticmethod
    def number_of_cars_stock() -> int | None:
        """
        This function check if there is free places in the stock for another car
        :returns: The number of free places in the stock
        """
        cursor: sql.dbapi2.Cursor = Db.db_cursor()[0]
        if cursor is not None:
            try:
                query: str = "SELECT count(*) FROM car WHERE id NOT IN (SELECT id FROM deal WHERE is_rent = 0)"
                cursor.execute(query)
                return cursor.fetchone()[0]
            except sql.OperationalError:
                print(f"Error in CarFreePlacesStock {sys.exc_info()}")
            finally:
                Db.db_close(cursor)
        return None

    def insert_db(self) -> bool:
        """
        This function insert in the database a new car
        :returns: True if the insert was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = (f"INSERT INTO car (date_tech_control, price, id_brand, id_type, id_motor, promo) "
                              f"VALUES ('{self.date_tech_control}', {self.price}, {self.id_brand},{self.id_type}, "
                              f"{self.id_motor}, {self.promo})")
                cursor.execute(query)
                db_connection.commit()
                return True
            except sql.OperationalError:
                print(f"Error in InsertDBCar {sys.exc_info()}")
            finally:
                self.db_close(cursor)
        return False

    def remove_db(self) -> bool:
        """
        This function delete the car
        :returns: True if the deleting was correctly executed
        """
        tuple_db: tuple = self.db_cursor()
        cursor: sql.dbapi2.Cursor = tuple_db[0]
        db_connection: sql.dbapi2.Connection = tuple_db[1]
        if cursor is not None:
            try:
                query: str = f"DELETE FROM car WHERE id = {self.id}"
                cursor.execute(query)
                db_connection.commit()
                del self
                return True
            except sql.OperationalError:
                print(f"Error in RemoveCarDB {sys.exc_info()}")
            finally:
                Db.db_close(cursor)
        return False

    @staticmethod
    def get_car(id_car: int) -> Car | None:
        """
        This function get a car in the database chosen by its id
        :param id_car: A integer number
        :returns: An object car with all its components
        """
        cursor: sql.dbapi2.Cursor = Car.db_cursor()[0]
        if cursor is not None:
            try:
                query: str = (f"SELECT id, STRFTIME('%d/%m/%Y', date_stock) as date_stock, date_tech_control, "
                              f"price, promo FROM car WHERE id = {id_car} ")
                cursor.execute(query)
                new_car: Car = Car.load_results(cursor, cursor.fetchone())
                new_car.get_components()
                return new_car
            except sql.OperationalError:
                print(f"Error in GetCar {sys.exc_info()}")
            finally:
                Car.db_close(cursor)
        return None

    def get_components(self) -> None:
        """
        This function add to the car its components from the database
        """
        self.brand = Brand.get_car_component(self.id)
        self.motor = Motor.get_car_component(self.id)
        self.type = Type.get_car_component(self.id)
