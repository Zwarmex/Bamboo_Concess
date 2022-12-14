import sys
from Main.Class.car import Car
from Main.Class.brand import Brand
from Main.Class.type import Type
from Main.Class.motor import Motor
from Main.Class.deal import Deal
from Main.Class.customer import Customer
from datetime import datetime
import re
from Main.CommonCode.function_common import *

"""
import logging
import os
import logging.handlers
"""


class ApplicationConsole:
    """
    It manages all the methods for the console application utilities
    """

    def __init__(self) -> None:
        """
        It creates a new object ApplicationConsole
        """
        self.car_list_stock: list = Car.get_car_list()
        self.brand_list: list = Brand.get_all()
        self.motor_list: list = Motor.get_all()
        self.type_list: list = Type.get_all()
        deal_list: list = Deal.get_all()
        self.rent_list: list = []
        self.sold_list: list = []
        for deal in deal_list:
            if deal.is_rent:
                self.rent_list.append(deal)
            else:
                self.sold_list.append(deal)
        self.customer_list: list = Customer.get_all()
        self.space_display: int = 4
        print("Welcome to Bamboo Concess\n")
        self.menu_choice()

    def menu_choice(self) -> None:
        """
        This function display the basic menu for the user
        """
        menu_input: str = ""
        while not check_number_input(menu_input, 1, 5):
            menu_input = input("Where do you want to go now ?\n 1 : Show your stock.\n"
                               " 2 : Show your transaction history.\n 3 : Add a new car to your stock.\n"
                               " 4 : Add a customer\n 5 : Exit the program.\n-> ")
        menu_input: int = int(menu_input)
        if menu_input == 1:
            self.display_stock()
        elif menu_input == 2:
            self.display_history()
        elif menu_input == 3:
            self.add_car()
        elif menu_input == 4:
            self.add_customer()
        else:
            sys.exit()

    def add_customer(self) -> None:
        """
        This function asks the user to add a customer to the database with all his characteristics
        """
        new_customer: Customer = Customer()
        while not new_customer.first_name.isalpha():
            new_customer.first_name = input("What's the first name ?\n-> ")
        while not new_customer.last_name.isalpha():
            new_customer.last_name = input("What's the last name ?\n-> ")
        while not (new_customer.phone.isdigit() and len(new_customer.phone) == 10):
            new_customer.phone = input("What's the phone number (10 numbers)\n-> ")
        new_customer.phone = int(new_customer.phone)
        while not (re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+\b', new_customer.mail)):
            new_customer.mail = input("What's the email address ?\n-> ")
        while not re.fullmatch(r"[a-zA-Z0-9\s._%+-]+, [a-zA-Z0-9\s._%+-]+\b", new_customer.address):
            new_customer.address = input("What's the address ?\n-> ")
        if new_customer.insert_db():
            print("New customer added\n")
        else:
            print("The execution doesn't work\n")
        self.menu_choice()

    def display_stock(self) -> None:
        """
        This function display the stock from the database
        """
        str_list: list = ["Id", "Brand", "Type", "Price (€)"]
        space_dict: dict = {
            str_list[0]: len(str(max(self.car_list_stock, key=lambda x: len(str(x.id))).id)) + self.space_display,
            str_list[1]: len(max(self.car_list_stock, key=lambda x: len(x.brand.name)).brand.name) + self.space_display,
            str_list[2]: len(max(self.car_list_stock, key=lambda x: len(x.type.name)).type.name) + self.space_display}
        for i in range(len(str_list) - 1):
            if space_dict[str_list[i]] < len(str_list[i]):
                space_dict[str_list[i]]: int = len(str_list[i]) + self.space_display
        print(f"{str_list[0]}" + " " * (space_dict[str_list[0]] - len(f"{str_list[0]}")) +
              f"{str_list[1]}" + " " * (space_dict[str_list[1]] - len(f"{str_list[1]}")) +
              f"{str_list[2]}" + " " * (space_dict[str_list[2]] - len(f"{str_list[2]}")) + f"{str_list[3]}")
        for car in self.car_list_stock:
            car: Car
            print(f"{str(car.id):{space_dict[str_list[0]]}}"
                  f"{car.brand.name:{space_dict[str_list[1]]}}"
                  f"{car.type.name:{space_dict[str_list[2]]}}"
                  f"{str(car.price)}")
        next_step: str = ""
        while not check_number_input(next_step, 1, 5):
            next_step: str = input("\nWhat do you want to do next ?\n 1 : Return to the choice menu.\n"
                                   " 2 : See a car's details.\n 3 : Rent a car.\n 4 : Make a deal.\n"
                                   " 5 : Remove a car.\n-> ")
        next_step: int = int(next_step)
        if next_step == 1:
            self.menu_choice()
        elif next_step == 2:
            good_choice: bool = False
            while not good_choice:
                car_id: str = input("Which car do you want to see details from ?\n-> ")
                if car_id.isdigit():
                    car_id: int = int(car_id)
                    for car in self.car_list_stock:
                        car: Car
                        if car_id == car.id:
                            print(f"Brand : {car.brand.name}\nType : {car.type.name}\nMotor : {car.motor.name}\n"
                                  f"Price : {str(car.price)}€\nPromo : {str(car.promo)}%\n"
                                  f"In stock since : {car.date_stock}\nNext control : {car.date_tech_control}\n")
                            good_choice = True
                            break
        elif next_step == 3:
            self.do_transaction(True)
        elif next_step == 4:
            self.do_transaction(False)
        elif next_step == 5:
            good_car_id: bool = False
            while not good_car_id:
                car_id: str = input("Which car do you want to remove (n for quit this operation)?\n-> ")
                if car_id.lower() == "n":
                    good_car_id = True
                    print("Operation abandoned.\n")
                elif car_id.isdigit():
                    for car in self.car_list_stock:
                        car: Car
                        if car.id == int(car_id):
                            good_car_id = True
                            car.remove_db()
                            self.car_list_stock = Car.get_car_list()
                            print("Car removed\n")
        self.menu_choice()

    def display_history(self) -> None:
        """
        This function display the history of the user transaction from the database
r        """
        choice_history: str = ""
        while not check_number_input(choice_history, 1, 2):
            choice_history = input("\n 1 : Rent history display.\n 2 : Transaction history display.\n-> ")
        choice_history: int = int(choice_history)
        str_list: list = ["Id", "Date", "Duration", "Brand", "Type", "Price (€)"]
        space_dict: dict = {}
        list_to_display: list = self.sold_list
        if choice_history == 1:
            list_to_display = self.rent_list
        if not list_to_display:
            print("There are not deals in this category\n")
            self.menu_choice()
            return
        space_dict[str_list[0]]: int = len(str(
            max(list_to_display, key=lambda x: len(str(x.id))).id)) + self.space_display
        space_dict[str_list[1]]: int = len(
            max(list_to_display, key=lambda x: len(x.date_start_rent)).date_start_rent) + self.space_display
        space_dict[str_list[2]]: int = len(str(
            max(list_to_display, key=lambda x: len(str(x.duration_days_rent))).duration_days_rent)) + self.space_display
        space_dict[str_list[3]]: int = len(
            max(list_to_display, key=lambda x: len(x.car.brand.name)).car.brand.name) + self.space_display
        space_dict[str_list[4]]: int = len(
            max(list_to_display, key=lambda x: len(x.car.type.name)).car.type.name) + self.space_display
        for i in range(len(str_list) - 1):
            if space_dict[str_list[i]] < len(str_list[i]):
                space_dict[str_list[i]] = len(str_list[i]) + self.space_display
        print(f"\n{str_list[0]}" + " " * (space_dict[str_list[0]] - len(f"{str_list[0]}")) +
              f"{str_list[1]}" + " " * (space_dict[str_list[1]] - len(f"{str_list[1]}")) +
              f"{str_list[2]}" + " " * (space_dict[str_list[2]] - len(f"{str_list[2]}")) +
              f"{str_list[3]}" + " " * (space_dict[str_list[3]] - len(f"{str_list[3]}")) +
              f"{str_list[4]}" + " " * (space_dict[str_list[4]] - len(f"{str_list[4]}")) + f"{str_list[5]}")
        for deal in self.rent_list:
            deal: Deal
            print(f"{str(deal.id):{space_dict[str_list[0]]}}{deal.date_start_rent:{space_dict[str_list[1]]}}"
                  f"{str(deal.duration_days_rent):{space_dict[str_list[2]]}}"
                  f"{deal.car.brand.name:{space_dict[str_list[3]]}}"
                  f"{deal.car.type.name:{space_dict[str_list[4]]}}{str(deal.car.price)}")
        print("")
        self.menu_choice()

    def do_transaction(self, bool_rent: bool) -> None:
        """
        This function asks the user to make a deal between one car and one customer
        :param bool_rent: boolean to know if the transaction is a rent or a sold
        :type bool_rent: bool
        """
        deal: Deal = Deal()
        good_car_id: bool = False
        good_start_date: bool = False
        good_customer_id: bool = False
        deal.is_rent = bool(bool_rent)
        space_dict: dict = {}
        str_list: list = ["Id", "Name", "Phone"]
        while not good_car_id:
            deal.id_car = input("What is the car id ?\n-> ")
            if deal.id_car.isdigit():
                deal.id_car = int(deal.id_car)
                for car in self.car_list_stock:
                    if car.id == deal.id_car:
                        good_car_id = True
                        break
        space_dict[str_list[0]]: int = len(
            str(max(self.customer_list, key=lambda x: len(str(x.id))).id)) + self.space_display
        longest_customer: Customer = max(self.customer_list, key=lambda x: len(x.last_name))
        space_dict[str_list[1]]: int = len(
            f"{longest_customer.first_name[0]}.{longest_customer.last_name}") + self.space_display
        for i in range(len(str_list) - 1):
            if space_dict[str_list[i]] < len(str_list[i]):
                space_dict[str_list[i]]: int = len(str_list[i])
        print(f"List of customers : \n{str_list[0]}" + " " * (space_dict[str_list[0]] - len(f"{str_list[0]}")) +
              f"{str_list[1]}" + " " * (space_dict[str_list[1]] - len(f"{str_list[0]}")) + f"{str_list[2]}")
        for customer in self.customer_list:
            customer: Customer
            print(f"{str(customer.id):{space_dict[str_list[0]]}}"
                  f"{f'{customer.first_name[0]}.{customer.last_name}':{space_dict[str_list[1]]}}{customer.phone}")
        while not good_customer_id:
            deal.id_customer = input("What is the customer's id ?\n-> ")
            if deal.id_customer.isdigit():
                deal.id_customer = int(deal.id_customer)
                for customer in self.customer_list:
                    customer: Customer
                    if customer.id == deal.id_customer:
                        good_customer_id = True
                        break
        if deal.is_rent:
            while not good_start_date:
                deal.dateStart = input("When does the rent start ?\n-> ")
                try:
                    deal.dateStart = datetime.strptime(deal.dateStart, '%d/%m/%Y').strftime("%d/%m/%Y")
                    good_start_date = True
                except ValueError:
                    continue
            while not check_number_input(deal.durationDays, minimum=1):
                deal.durationDays = input("How many days will the rent spend ?\n-> ")
        deal.insert_db()
        self.menu_choice()

    def add_car(self) -> None:
        """
        This function asks the user to add a car to the database with all the characteristics
        :rtype: None
        """
        if Car.number_of_cars_stock() <= 40:
            car: Car = Car()
            name_brand: str = ""
            name_type: str = ""
            name_motor: str = ""
            good_date: bool = False
            while not name_brand:
                name_brand = input("What is the name of the brand ?\n-> ")
            while not name_type:
                name_type = input("What is the type ?\n-> ")
            while not name_motor:
                name_motor = input("What is the motor's name ?\n-> ")
            while not check_number_input(car.price, minimum=0):
                car.price = input("What is the price ?\n-> ")
            car.price = int(car.price)
            while not check_number_input(car.promo, 0, 100):
                car.promo = input("Any promotion (%) ?\n-> ")
            car.promo = int(car.promo)
            while not good_date:
                car.date_tech_control = input("What is the date of the tech control ?\n-> ")
                try:
                    car.date_tech_control = datetime.strptime(car.date_tech_control, '%d/%m/%Y').strftime("%d/%m/%Y")
                    good_date = True
                except ValueError:
                    continue
            car.id_brand = Brand.get_id(name_brand)
            car.id_type = Type.get_id(name_type)
            car.id_motor = Motor.get_id(name_motor)
            if car.insert_db():
                print("Executed\n")
            else:
                print("Not executed\n")
        else:
            print("No free places in stock.\n")
        self.menu_choice()


"""
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "/var/log/yourapp.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(ApplicationConsole())
except Exception:
    logging.exception("Exception in ApplicationConsole()")
    exit(1)
"""
# ApplicationConsole()
if __name__ == "__main__":
    ApplicationConsole()
