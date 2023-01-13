import unittest
from main_project.classes.car import Car
from main_project.classes.car_components import Brand
from main_project.classes.car_components import Motor
from main_project.classes.car_components import Type
import sqlite3 as sql


class TestCar(unittest.TestCase):
    def setUp(self):
        """
        Code à exécuter avant chaque test
        """
        brand1 = Brand("ToyotaTest")
        brand1.insert_db()
        motor1 = Motor("3000TEST")
        motor1.insert_db()
        type1 = Type("SUVTEST")
        type1.insert_db()
        car1 = Car("3-2-2022TEST", 45_000, 0, 1, 1, 1)
        car1.insert_db()

    def test_name_table(self):
        # Test de la méthode name_table
        self.assertEqual(Car.name_table(), "car")

    def test_id_column(self):
        # Test de la méthode id_column
        self.assertEqual(Car.id_column(), "idCar")

    def test_get_car_list(self):
        self.assertEqual(len(Car.get_car_list()), 1)

    def test_get_car(self):
        self.assertIsInstance(Car.get_car(1), Car)

    def tearDown(self):
        """
        Code à exécuter après chaque test
        """
        db_connection: sql.dbapi2.Connection = sql.connect("../database/bamboo_concess.db")
        cursor = db_connection.cursor()
        cursor.execute("delete from car where date_tech_control='3-2-2022TEST'; ")
        db_connection.commit()
        cursor.execute("delete from motor where name='3000TEST';")
        db_connection.commit()
        cursor.execute("delete from brand where name='ToyotaTest';")
        db_connection.commit()
        cursor.execute("delete from type where name='SUVTEST'")
        db_connection.commit()
        cursor.execute("update sqlite_sequence set seq = 0 where 1;")
        db_connection.commit()


if __name__ == '__main__':
    unittest.main()
