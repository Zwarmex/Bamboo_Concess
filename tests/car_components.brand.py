import unittest
from main_project.classes.car_components import Brand

class TestMotor(unittest.TestCase):
    def test_name_table_on_class(self):
        # On vérifie que la méthode renvoie bien le nom de la table "motor"
        # lorsqu'elle est appelée sur la classe elle-même
        self.assertEqual(Brand.name_table(), "brand")

    def test_id_column_on_class(self):
        # On vérifie que la méthode renvoie bien le nom de la colonne "id"
        # lorsqu'elle est appelée sur la classe elle-même
        self.assertEqual(Brand.id_column(), "id")

    def test_name_table_on_instance(self):
        # On vérifie que la méthode renvoie bien le nom de la table "motor"
        # lorsqu'elle est appelée sur une instance de la classe
        brand = Brand()
        self.assertEqual(brand.name_table(), "brand")

    def test_id_column_on_instance(self):
        # On vérifie que la méthode renvoie bien le nom de la colonne "id"
        # lorsqu'elle est appelée sur une instance de la classe
        brand = Brand()
        self.assertEqual(brand.id_column(), "id")


if __name__ == '__main__':
    unittest.main()
