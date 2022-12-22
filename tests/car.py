import unittest
from main_project.classes.car import Car


class TestCar(unittest.TestCase):
    def test_name_table(self):
        # Test de la méthode name_table
        self.assertEqual(Car.name_table(), "car")

    def test_id_column(self):
        # Test de la méthode id_column
        self.assertEqual(Car.id_column(), "idCar")

    def test_get_car_list(self):
        # Test de la méthode get_car_list
        car_list = Car.get_car_list()
        self.assertIsInstance(car_list, list)
        self.assertGreaterEqual(len(car_list), 0)

    def test_number_of_cars_stock(self):
        # Test de la méthode number_of_cars_stock
        nb_cars = Car.number_of_cars_stock()
        self.assertIsInstance(nb_cars, int)
        self.assertGreaterEqual(nb_cars, 0)

    def test_insert_db(self):
        # Test d'insertion valide
        car = Car()
        car.date_tech_control = "2022-01-01"
        car.price = 10000
        car.id_brand = 1
        car.id_type = 1
        car.id_motor = 1
        self.assertTrue(car.insert_db())


if __name__ == '__main__':
    unittest.main()
