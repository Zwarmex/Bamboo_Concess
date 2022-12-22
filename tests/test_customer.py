import unittest
from main_project.classes.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_init(self):
        # Test d'initialisation d'un objet Customer avec des valeurs par défaut
        customer = Customer()
        self.assertEqual(customer.id, 0)
        self.assertEqual(customer.first_name, "")
        self.assertEqual(customer.last_name, "")
        self.assertEqual(customer.phone, 0)
        self.assertEqual(customer.mail, "")
        self.assertEqual(customer.address, "")
        self.assertEqual(customer.counter, 0)
        self.assertEqual(customer.loyalty_since, "")

    def test_get_customer(self):
        # Test avec un id valide
        id_customer = 1
        customer = Customer.get_customer(id_customer)
        self.assertIsNotNone(customer)

        # Test avec un id non valide
        id_customer = -1
        customer = Customer.get_customer(id_customer)
        self.assertIsNone(customer)

    def test_insert_db(self):
        # Test d'insertion d'un nouveau client valide
        customer = Customer()
        customer.first_name = "John"
        customer.last_name = "Doe"
        customer.phone = 1234567890
        customer.mail = "john.doe@example.com"
        customer.address = "123 Main Street"
        self.assertTrue(customer.insert_db())

        # Test d'insertion d'un nouveau client avec des valeurs non valides
        customer = Customer()
        customer.first_name = ""
        customer.last_name = ""
        customer.phone = 1234567890
        customer.mail = "invalid.email@"
        customer.address = "123 Main Street"
        self.assertFalse(customer.insert_db())

    def test_name_table(self):
        # Test de récupération du nom de la table client
        self.assertEqual(Customer.name_table(), "customer")

    def test_id_column(self):
        # Test de récupération du nom de la colonne id de la table client
        self.assertEqual(Customer.id_column(), "id")


if __name__ == '__main__':
    unittest.main()
