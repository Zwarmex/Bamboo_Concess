import unittest
from main_project.classes.deal import Deal
from main_project.classes.car_components import *
from main_project.classes.car import Car
from main_project.classes.customer import Customer
import sqlite3 as sql


class TestDeal(unittest.TestCase):
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
        customer1 = Customer("SamuelTEST", "Lambert", "0495717736", "sam.f.lambert@gmail.com", "Rue du village 2, "
                                                                                               "1450 Villeroux")
        customer1.insert_db()
        deal1 = Deal(1, 1, True, "3/4/1950", duration_days_rent=1)
        deal1.insert_db()

    def test_name_table(self):
        self.assertEqual(Deal.name_table(), "deal")

    def test_id_column(self):
        self.assertEqual(Deal.id_column(), "id")

    def test_get_all(self):
        self.assertEqual(len(Deal.get_all()), 1)
        self.assertIsInstance(Deal.get_all(), list)

    def test_insert_db(self):
        deal1 = Deal(1, 1, True, "3/4/1950", duration_days_rent=1)
        self.assertTrue(deal1.insert_db(), True)
        self.assertTrue(deal1.remove_db(), True)

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
        cursor.execute("delete from customer where first_name = 'SamuelTEST'")
        db_connection.commit()
        cursor.execute("delete from deal where date_start_rent = '3/4/1950'")
        db_connection.commit()
        cursor.execute("delete from historic_deal where date_start_rent = '3/4/1950'")
        db_connection.commit()
        cursor.execute("update sqlite_sequence set seq = 0 where 1;")
        db_connection.commit()


if __name__ == '__main__':
    unittest.main()
