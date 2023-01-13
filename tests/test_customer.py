import unittest
from main_project.classes.customer import Customer
import sqlite3 as sql


class TestCustomer(unittest.TestCase):
    def setUp(self):
        """
        Code à exécuter avant chaque test
        """
        customer1 = Customer("SamuelTEST", "Lambert", "0495717736", "sam.f.lambert@gmail.com",
                             "Rue du village 2, 1450 Villeroux")
        customer1.insert_db()

    def test_get_customer(self):
        self.assertIsInstance(Customer.get_customer(1), Customer)

    def tearDown(self):
        """
        Code à exécuter après chaque test
        """
        db_connection: sql.dbapi2.Connection = sql.connect("../database/bamboo_concess.db")
        cursor = db_connection.cursor()
        cursor.execute("delete from customer where first_name = 'SamuelTEST'")
        db_connection.commit()
        cursor.execute("update sqlite_sequence set seq = 0 where 1;")
        db_connection.commit()


if __name__ == '__main__':
    unittest.main()
