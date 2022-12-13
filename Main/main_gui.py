import tkinter.font as font
from tkinter import *
from tkcalendar import DateEntry as tkCal
import math
import re
from datetime import datetime
from Main.CommonCode.function_common import *
from Main.Class.brand import Brand
from Main.Class.customer import Customer
from Main.Class.deal import Deal
from Main.Class.motor import Motor
from Main.Class.type import Type
from Main.Class.car import Car
from Main.Class.historic_deal import HistoricDeal


class ApplicationGUI:
    """
    It manages all the methods for the graphic application utilities
    """

    def __init__(self) -> None:
        """
        It will initialise a new object window
        """
        self.window: Tk | None = None
        self.button_add_car: Button | None = None
        self.button_deal: Button | None = None
        self.button_rent: Button | None = None
        self.button_history: Button | None = None
        self.button_stock: Button | None = None
        self.button_add_customer: Button | None = None
        self.frame_buttons: Frame | None = None
        self.frame_details: Frame | None = None
        self.frame_display: Frame | None = None
        self.frame_sort: Frame | None = None
        self.label_column: Label | None = None
        self.label_details: Label | None = None
        self.value_check_button_order: IntVar | None = None
        self.space_display: int = 4
        self.row_number_rent: int = 5
        self.row_number_selling: int = 3
        self.row_number_add_car: int = 7
        self.row_number_add_customer: int = 6
        self.lcm_row_number_display: int = math.lcm(self.row_number_rent, self.row_number_selling,
                                                    self.row_number_add_car,
                                                    self.row_number_add_customer)
        self.police: str = "courier 15"
        self.title: str = "BAMBOO CONCESS"
        self.rent_list: list = []
        self.car_list_free: list = []
        self.car_list_stock: list = []
        self.deal_list: list = []
        self.historic_deal_list: list = []
        self.reset_car_lists()
        self.brand_list: list = Brand.get_all()
        self.motor_list: list = Motor.get_all()
        self.type_list: list = Type.get_all()
        self.customer_list: list = Customer.get_all()
        self.create_basic_window()

    def create_basic_window(self) -> None:
        """
        It set the window and all the widget for it
        """
        self.window: Tk = Tk()
        self.window.title(self.title)
        self.window.attributes('-fullscreen', True)
        self.window.option_add("*Font", self.police)
        self.window.config(bg="white")
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=2)
        self.window.columnconfigure(2, weight=1)
        for i in range(6):
            self.window.rowconfigure(i, weight=1)
        self.window.rowconfigure(7, weight=2)
        self.frame_buttons: Frame = Frame(self.window)
        self.frame_buttons.grid(column=0, row=1, rowspan=5, sticky=NSEW)
        for i in range(6):
            self.frame_buttons.rowconfigure(i, weight=1)
        self.frame_buttons.columnconfigure(0, weight=1)
        self.button_stock: Button = Button(self.frame_buttons, text="Display Stock",
                                           command=self.display_window_stock)
        self.button_stock.grid(column=0, row=0, sticky=NSEW)
        self.button_history: Button = Button(self.frame_buttons, text="Display History",
                                             command=self.display_window_history)
        self.button_history.grid(column=0, row=1, sticky=NSEW)
        self.button_rent: Button = Button(self.frame_buttons, text="Rent a car",
                                          command=self.display_window_rent)
        self.button_rent.grid(column=0, row=2, sticky=NSEW)
        self.button_deal: Button = Button(self.frame_buttons, text="Make a deal",
                                          command=self.display_window_selling)
        self.button_deal.grid(column=0, row=3, sticky=NSEW)
        self.button_add_car: Button = Button(self.frame_buttons, text="Add a car in stock",
                                             command=self.display_window_add_car)
        self.button_add_car.grid(column=0, row=4, sticky=NSEW)
        self.button_add_customer: Button = Button(self.frame_buttons, text="Add a customer",
                                                  command=self.display_window_add_customer)
        self.button_add_customer.grid(column=0, row=5, sticky=NSEW)
        frame_title: Frame = Frame(self.window, highlightthickness=2, highlightbackground="black")
        frame_title.grid(column=1, row=0, sticky=NSEW)
        frame_title.rowconfigure(0, weight=1)
        frame_title.columnconfigure(0, weight=1)
        label_title: Label = Label(frame_title, text=self.title)
        label_title.grid(column=0, row=0, sticky=NSEW)
        self.frame_sort: Frame = Frame(self.window, highlightthickness=1, highlightbackground="black")
        self.frame_sort.grid(column=1, row=1, sticky=NSEW)
        for i in range(5):
            self.frame_sort.rowconfigure(i, weight=1)
        for i in range(2):
            self.frame_sort.columnconfigure(i, weight=1)
        self.frame_sort.pack_propagate(False)
        self.frame_sort.grid_propagate(False)
        self.frame_display: Frame = Frame(self.window)
        self.frame_display.grid(column=1, row=2, rowspan=6, sticky=NSEW)
        for i in range(self.lcm_row_number_display):
            self.frame_display.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.frame_display.grid_columnconfigure(i, weight=1)
        self.frame_display.pack_propagate(False)
        self.frame_display.grid_propagate(False)
        self.frame_details: Frame = Frame(self.window, highlightthickness=2, highlightbackground="black")
        self.frame_details.grid(column=2, row=1, rowspan=7, sticky=NSEW)
        self.frame_details.grid_propagate(False)
        for i in range(2):
            self.frame_details.rowconfigure(i, weight=1)
        self.frame_details.columnconfigure(0, weight=1)
        label_title_details: Label = Label(self.frame_details, text="DETAILS", anchor="s",
                                           font=self.police + " underline")
        label_title_details.grid(column=0, row=0, sticky='wesn')
        self.label_details: Label = Label(self.frame_details, text="", justify="left", anchor='nw')
        self.label_details.grid(column=0, row=1, sticky=NSEW)
        frame_exit: Frame = Frame(self.window)
        frame_exit.grid(column=2, row=0, sticky=NSEW)
        frame_exit.rowconfigure(0, weight=1)
        frame_exit.columnconfigure(0, weight=1)
        button_exit: Button = Button(frame_exit, text="Exit", command=self.window.destroy, font=font.Font(
            family='Helvetica', size=15, weight='bold'))
        button_exit.grid(column=0, row=0, sticky=NSEW)
        self.display_window_stock()
        self.window.mainloop()

    def display_car_listbox(self, list_car: list, listbox: Listbox, dict_space: dict, list_str: list) -> None:
        """
        It displays the list of cars or deals in the listbox
        :param list_str: The list of string to print in the title of the listbox
        :param dict_space: The dictionary of space for each string
        :param listbox: The list where the list sorted will be display
        :param list_car: The list will be sort
        """
        for car_or_historical_deal in list_car:
            if type(list_car[0]) == Car:
                car_or_historical_deal: Car
                rented: str = ""
                for deal in self.rent_list:
                    if deal.id_car == car_or_historical_deal.id:
                        rented: str = "Rented"
                        break
                listbox.insert(END, f"{str(car_or_historical_deal.id):{dict_space[list_str[0]]}}"
                                    f"{car_or_historical_deal.brand.name:{dict_space[list_str[1]]}}"
                                    f"{car_or_historical_deal.type.name:{dict_space[list_str[2]]}}"
                                    f"{str(car_or_historical_deal.price):{dict_space[list_str[3]]}}{rented}")
                listbox.bind('<<ListboxSelect>>', self.display_details_stock)
            else:
                car_or_historical_deal: HistoricDeal
                listbox.insert(END, f"{str(car_or_historical_deal.car.id):{dict_space[list_str[0]]}}"
                                    f"{car_or_historical_deal.car.brand.name:{dict_space[list_str[1]]}}"
                                    f"{car_or_historical_deal.car.type.name:{dict_space[list_str[2]]}}"
                                    f"{str(car_or_historical_deal.car.price):{dict_space[list_str[3]]}}"
                                    f"{car_or_historical_deal.customer.first_name[0]}."
                                    f"{car_or_historical_deal.customer.last_name}")
                listbox.bind('<<ListboxSelect>>', self.display_details_history)

    def sort_display(self, value_sorting: str) -> None:
        """
        It sorts the listbox and display the good window
        """
        if value_sorting:
            if self.button_stock["state"] == DISABLED:
                self.car_list_stock.sort(key=lambda x: getattr(x, value_sorting),
                                         reverse=bool(self.value_check_button_order.get()))
                self.display_window_stock()
            else:
                self.historic_deal_list.sort(key=lambda x: getattr(x.car, value_sorting),
                                             reverse=bool(self.value_check_button_order.get()))
                self.display_window_history()

    def display_frame_sort(self) -> None:
        """
       It displays the sorting frame
       """
        if self.value_check_button_order is None:
            self.value_check_button_order = IntVar()
        label_info_sorting: Label = Label(self.frame_sort, text="Sorting by : ")
        label_info_sorting.grid(column=0, row=0, rowspan=5)
        button_id: Button = Button(self.frame_sort, text="Id", command=lambda: self.sort_display("id"))
        button_id.grid(column=1, row=0, sticky=NSEW)
        button_price: Button = Button(self.frame_sort, text="Price", command=lambda: self.sort_display("price"))
        button_price.grid(column=1, row=1, sticky=NSEW)
        if self.button_stock["state"] == DISABLED:
            button_date_stock: Button = Button(self.frame_sort, text="Date stock",
                                               command=lambda: self.sort_display("date_stock"))
            button_date_stock.grid(column=1, row=2, sticky=NSEW)
            button_date_control: Button = Button(self.frame_sort, text="Date control",
                                                 command=lambda: self.sort_display("date_tech_control"))
            button_date_control.grid(column=1, row=3, sticky=NSEW)
            button_promo: Button = Button(self.frame_sort, text="Promo", command=lambda: self.sort_display("promo"))
            button_promo.grid(column=1, row=4, sticky=NSEW)
        check_button_order: Checkbutton = Checkbutton(self.frame_sort, text="Descending ?",
                                                      variable=self.value_check_button_order)
        check_button_order.grid(column=0, row=3, rowspan=2, sticky=NSEW)

    def display_window_stock(self) -> None:
        """
        It shows you all of your cars you have in your stock. It is displayed by default.
        """
        self.reset_display_and_sort_frames(self.button_stock)
        self.display_frame_sort()
        if not self.car_list_stock:
            label_info: Label = Label(self.frame_display, text="There are no cars in your stock.")
            label_info.pack()
            return
        str_list: list = ["Id", "Brand", "Type", "Price (€)", "Status"]
        space_dict: dict = {
            str_list[0]: len(str(max(self.car_list_stock, key=lambda x: len(str(x.id))).id)) + self.space_display,
            str_list[1]: len(max(self.car_list_stock, key=lambda x: len(x.brand.name)).brand.name) + self.space_display,
            str_list[2]: len(max(self.car_list_stock, key=lambda x: len(x.type.name)).type.name) + self.space_display,
            str_list[3]: len(str(max(self.car_list_stock, key=lambda x: len(str(x.price))).price)) + self.space_display}
        title_column: str = ""
        for i in range(len(space_dict)):
            title_column += f"{str_list[i]}" + " " * (space_dict[str_list[i]] - len(f"{str_list[i]}"))
        title_column += f"{str_list[4]}"
        label_title_column: Label = Label(self.frame_display, text=title_column)
        label_title_column.pack(anchor=NW)
        frame_list_box_scroll: Frame = Frame(self.frame_display)
        frame_list_box_scroll.pack(expand=True, fill=BOTH, anchor=W)
        scrollbar: Scrollbar = Scrollbar(frame_list_box_scroll)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox_stock: Listbox = Listbox(frame_list_box_scroll)
        listbox_stock.pack(expand=True, fill=BOTH, anchor=W)
        self.display_car_listbox(self.car_list_stock, listbox_stock, space_dict, str_list)
        listbox_stock.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=listbox_stock.yview)

    def display_details_stock(self, event: Event) -> None:
        """
        When you click a row to show more information about the car you selected
        :param event: The event create when a click is performed on the listbox
        """
        car: Car = self.car_list_stock[event.widget.curselection()[0]]
        rented_deal: None = None
        for deal in self.rent_list:
            if deal.id_car == car.id:
                rented_deal: Deal = deal
                break
        print_details: str = (f"Brand : {car.brand.name}\nType : {car.type.name}\nMotor : {car.motor.name}\n"
                              f"Price : {car.price}€\nPromo : {car.promo}%\nIn stock since : {car.date_stock}\n"
                              f"Next control : {car.date_tech_control}\n")
        if rented_deal:
            print_details += (f"The rent starts : {rented_deal.date_start_rent}\n"
                              f"Duration : {rented_deal.duration_days_rent} days")
        self.label_details.configure(text=print_details)

    def display_window_history(self) -> None:
        """
        It will show you which car you sell.
        """
        self.reset_display_and_sort_frames(self.button_history)
        self.display_frame_sort()
        if not self.historic_deal_list:
            label_info: Label = Label(self.frame_display, text="There are no deals made before.")
            label_info.pack()
            return
        str_list: list = ["Id", "Brand", "Type", "Price (€)", "Customer"]
        space_dict: dict = {
            str_list[0]: len(str(
                max(self.historic_deal_list, key=lambda x: len(str(x.car.id))).car.id)) + self.space_display,
            str_list[1]: len(
                max(self.historic_deal_list, key=lambda x: len(x.car.brand.name)).car.brand.name) + self.space_display,
            str_list[2]: len(
                max(self.historic_deal_list, key=lambda x: len(x.car.type.name)).car.type.name) + self.space_display,
            str_list[3]: len(str(
                max(self.historic_deal_list, key=lambda x: len(str(x.car.price))).car.price)) + self.space_display}
        title_column: str = ""
        for i in range(len(space_dict)):
            title_column += f"{str_list[i]}" + " " * (space_dict[str_list[i]] - len(f"{str_list[i]}"))
        title_column += f"{str_list[4]}"
        label_title: Label = Label(self.frame_display, text=title_column, anchor="w")
        label_title.pack(anchor=W)
        frame_list_box_scroll: Frame = Frame(self.frame_display)
        frame_list_box_scroll.pack(expand=True, fill=BOTH)
        scrollbar: Scrollbar = Scrollbar(frame_list_box_scroll)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox_history: Listbox = Listbox(frame_list_box_scroll)
        listbox_history.pack(expand=True, fill=BOTH)
        self.display_car_listbox(self.historic_deal_list, listbox_history, space_dict, str_list)
        listbox_history.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=listbox_history.yview)

    def display_details_history(self, event: Event) -> None:
        """
        When you click a row to show more information about the car you selected
        :param event: The event create when a click is performed on the listbox
        """
        for i in range(2):
            self.frame_details.rowconfigure(i, weight=1)
        self.frame_details.columnconfigure(0, weight=1)
        historical_deal: HistoricDeal = self.historic_deal_list[event.widget.curselection()[0]]
        print_details: str = (f"Brand : {historical_deal.car.brand.name}\nType : {historical_deal.car.type.name}\n"
                              f"Motor : {historical_deal.car.motor.name}\nPrice : {historical_deal.car.price}€\n"
                              f"Promo : {historical_deal.car.promo}%\n"
                              f"In stock since : {historical_deal.car.date_stock}\n "
                              f"Next control {historical_deal.car.date_tech_control}\n"
                              f"The customer is : {historical_deal.customer.first_name} "
                              f"{historical_deal.customer.last_name}\n")
        if historical_deal.is_rent:
            print_details += (f"The rent starts : {historical_deal.date_start_rent}\n"
                              f"Duration : {historical_deal.duration_days_rent} days")
        self.label_details.configure(text=print_details)

    def display_window_rent(self) -> None:
        """
        It will help you to change the reservation's status for a particular car
        """
        self.reset_display_and_sort_frames(self.button_rent)
        rowspan: int = int(self.lcm_row_number_display / self.row_number_rent)
        if not self.car_list_free or not self.customer_list:
            label_no_free_places: Label = Label(self.frame_display, text="There are no cars to sell or customers")
            label_no_free_places.pack()
            return
        raw_deal: dict = {"id_car": StringVar(), "id_customer": StringVar(), "date_start_rent": StringVar(),
                          "duration_days_rent": StringVar(), "is_rent": 1}
        label_id_car: Label = Label(self.frame_display, text="Car id : ")
        label_id_car.grid(column=0, row=0, rowspan=rowspan, sticky=NSEW)
        dropdown_car_id: OptionMenu = OptionMenu(self.frame_display, raw_deal["id_car"],
                                                 *map(lambda x: f"{x.id} price : {x.price} promo : {x.promo}",
                                                      self.car_list_free))
        dropdown_car_id.grid(column=1, row=0, rowspan=rowspan, sticky=NSEW)
        label_id_customer: Label = Label(self.frame_display, text="Customer id : ")
        label_id_customer.grid(column=0, row=rowspan, rowspan=rowspan, sticky=NSEW)
        dropdown_id_customer: OptionMenu = OptionMenu(self.frame_display, raw_deal["id_customer"],
                                                      *map(lambda x: f"{x.id} {x.first_name[0]}.{x.last_name}",
                                                           self.customer_list))
        dropdown_id_customer.grid(column=1, row=rowspan, rowspan=rowspan, sticky=NSEW)
        label_date_start_rent: Label = Label(self.frame_display, text="Date of the rent : ")
        label_date_start_rent.grid(column=0, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        entry_date_start_rent: tkCal = tkCal(self.frame_display, textvariable=raw_deal["date_start_rent"],
                                             locale='fr_BE', date_pattern="dd/mm/yyyy")
        entry_date_start_rent.grid(column=1, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        label_duration_days_rent: Label = Label(self.frame_display, text="Duration days of the rent : ")
        label_duration_days_rent.grid(column=0, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        entry_duration_days_rent: Entry = Entry(self.frame_display, textvariable=raw_deal["duration_days_rent"])
        entry_duration_days_rent.grid(column=1, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        button_rent_a_car: Button = Button(self.frame_display, text="Make the rent",
                                           command=lambda: self.verify_deal(raw_deal))
        button_rent_a_car.grid(column=1, row=rowspan * 4, rowspan=rowspan, sticky=NSEW)

    def display_window_selling(self) -> None:
        """
        It will help you to sell a particular car.
        """
        self.reset_display_and_sort_frames(self.button_deal)
        rowspan: int = int(self.lcm_row_number_display / self.row_number_selling)
        if not self.car_list_free or not self.car_list_stock:
            label_no_free_places: Label = Label(self.frame_display, text="There are no cars to sell or customers")
            label_no_free_places.pack()
            return
        raw_deal: dict = {"id_car": StringVar(), "id_customer": StringVar(), "is_rent": False}
        label_id_car: Label = Label(self.frame_display, text="Car id : ")
        label_id_car.grid(column=0, row=0, rowspan=rowspan, sticky=NSEW)
        dropdown_car_id: OptionMenu = OptionMenu(self.frame_display, raw_deal["id_car"],
                                                 *map(lambda x: f"{x.id} price : {x.price} promo : {x.promo}",
                                                      self.car_list_free))
        dropdown_car_id.grid(column=1, row=0, rowspan=rowspan, sticky=NSEW)
        label_id_customer: Label = Label(self.frame_display, text="Customer id : ")
        label_id_customer.grid(column=0, row=rowspan, rowspan=rowspan, sticky=NSEW)
        dropdown_id_customer: OptionMenu = OptionMenu(self.frame_display, raw_deal["id_customer"],
                                                      *map(lambda x: f"{x.id} {x.first_name[0]}.{x.last_name}",
                                                           self.customer_list),
                                                      command=lambda: self.verify_customer_loyalty(
                                                          raw_deal["id_customer"].get().split()[0]))
        dropdown_id_customer.grid(column=1, row=rowspan, rowspan=rowspan, sticky=NSEW)
        button_make_deal: Button = Button(self.frame_display, text="Make the deal",
                                          command=lambda: self.verify_deal(raw_deal))
        button_make_deal.grid(column=1, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)

    def display_window_add_car(self) -> None:
        """
        This menu will help you to add a new car in your stock with a form.
        """
        self.reset_display_and_sort_frames(self.button_add_car)
        rowspan: int = int(self.lcm_row_number_display / self.row_number_add_car)
        if Car.number_of_cars_stock() > 40:
            label_no_free_places: Label = Label(self.frame_display, text="No free places")
            label_no_free_places.pack()
            return
        raw_car: dict = {"nameBrand": StringVar(), "nameType": StringVar(), "nameMotor": StringVar(),
                         "price": StringVar(), "promo": StringVar(), "dateTechControl": StringVar()}
        label_brand: Label = Label(self.frame_display, text="Brand : ")
        label_brand.grid(column=0, row=0, rowspan=rowspan, sticky=NSEW)
        entry_brand: Entry = Entry(self.frame_display, textvariable=raw_car["nameBrand"])
        entry_brand.grid(column=1, row=0, rowspan=rowspan, sticky=NSEW)
        label_type: Label = Label(self.frame_display, text="Type : ")
        label_type.grid(column=0, row=rowspan, rowspan=rowspan, sticky=NSEW)
        entry_type: Entry = Entry(self.frame_display, textvariable=raw_car["nameType"])
        entry_type.grid(column=1, row=rowspan, rowspan=rowspan, sticky=NSEW)
        label_motor: Label = Label(self.frame_display, text="Motor : ")
        label_motor.grid(column=0, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        entry_type: Entry = Entry(self.frame_display, textvariable=raw_car["nameMotor"])
        entry_type.grid(column=1, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        label_next_control: Label = Label(self.frame_display, text="Next tech control :")
        label_next_control.grid(column=0, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        entry_next_control: tkCal = tkCal(self.frame_display, textvariable=raw_car["dateTechControl"],
                                          locale='fr_BE', date_pattern="dd/mm/yyyy")
        entry_next_control.grid(column=1, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        label_price: Label = Label(self.frame_display, text="Price : ")
        label_price.grid(column=0, row=rowspan * 4, rowspan=rowspan, sticky=NSEW)
        entry_price: Entry = Entry(self.frame_display, textvariable=raw_car["price"])
        entry_price.grid(column=1, row=rowspan * 4, rowspan=rowspan, sticky=NSEW)
        label_promo: Label = Label(self.frame_display, text="Promo : ")
        label_promo.grid(column=0, row=rowspan * 5, rowspan=rowspan, sticky=NSEW)
        entry_promo: Entry = Entry(self.frame_display, textvariable=raw_car["promo"])
        entry_promo.grid(column=1, row=rowspan * 5, rowspan=rowspan, sticky=NSEW)
        button_add_car: Button = Button(self.frame_display, text="Add a car in stock",
                                        command=lambda: self.verify_car_insert(raw_car))
        button_add_car.grid(column=1, row=rowspan * 6, rowspan=rowspan, sticky=NSEW)

    def display_window_add_customer(self):
        """
        It displays a window to create a customer in the database
        """
        self.reset_display_and_sort_frames(self.button_add_customer)
        rowspan: int = int(self.lcm_row_number_display / self.row_number_add_customer)
        raw_customer: dict = {"firstName": StringVar(), "lastName": StringVar(), "phone": StringVar(),
                              "mail": StringVar(), "address": StringVar()}
        label_first_name: Label = Label(self.frame_display, text="Firstname : ")
        label_first_name.grid(column=0, row=0, rowspan=rowspan, sticky=NSEW)
        entry_first_name: Entry = Entry(self.frame_display, textvariable=raw_customer["firstName"])
        entry_first_name.grid(column=1, row=0, rowspan=rowspan, sticky=NSEW)
        label_last_name: Label = Label(self.frame_display, text="Lastname : ")
        label_last_name.grid(column=0, row=rowspan, rowspan=rowspan, sticky=NSEW)
        entry_last_name: Entry = Entry(self.frame_display, textvariable=raw_customer["lastName"])
        entry_last_name.grid(column=1, row=rowspan, rowspan=rowspan, sticky=NSEW)
        label_phone: Label = Label(self.frame_display, text="Phone : ")
        label_phone.grid(column=0, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        entry_phone: Entry = Entry(self.frame_display, textvariable=raw_customer["phone"])
        entry_phone.grid(column=1, row=rowspan * 2, rowspan=rowspan, sticky=NSEW)
        label_mail: Label = Label(self.frame_display, text="Email Address :")
        label_mail.grid(column=0, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        entry_mail: Entry = Entry(self.frame_display, textvariable=raw_customer["mail"])
        entry_mail.grid(column=1, row=rowspan * 3, rowspan=rowspan, sticky=NSEW)
        label_address: Label = Label(self.frame_display, text="Address : ")
        label_address.grid(column=0, row=rowspan * 4, rowspan=rowspan, sticky=NSEW)
        entry_address: Entry = Entry(self.frame_display, textvariable=raw_customer["address"])
        entry_address.grid(column=1, row=rowspan * 4, rowspan=rowspan, sticky=NSEW)
        button_add_customer: Button = Button(self.frame_display, text="Add a car in stock",
                                             command=lambda: self.verify_customer_insert(raw_customer))
        button_add_customer.grid(column=1, row=rowspan * 5, rowspan=rowspan, sticky=NSEW)

    def verify_customer_loyalty(self, id_customer: id):
        """
        It checks if this customer is loyal and can have a promo on his car
        :param id_customer: id to check in the db if this customer is loyal
        """
        customer: Customer = Customer.get_customer(id_customer)
        if customer.counter > 3 or (datetime.today() - datetime.strptime("2021-11-30", "%Y-%m-%d")).days >= 365:
            pass
            # TODO : change the promo field to customer

    def verify_customer_insert(self, customer_string_var: dict) -> None:
        """
        It verifies that the data entered are corrects
        :param customer_string_var: The dictionary that keep the raw information for the new customer
        :return:
        """
        text_info: str = ""
        new_customer: Customer = Customer()
        new_customer.first_name = customer_string_var["firstName"].get()
        if not new_customer.first_name or bool(re.search(r'\d', new_customer.first_name)):
            text_info += "- There is no firstname.\n"
        new_customer.last_name = customer_string_var["lastName"].get()
        if not new_customer.last_name or bool(re.search(r'\d', new_customer.last_name)):
            text_info += "- There is no lastname.\n"
        new_customer.phone = customer_string_var["phone"].get()
        if not (new_customer.phone.isdigit() and len(new_customer.phone) == 10):
            text_info += "- There is no phone number.\n"
        new_customer.mail = customer_string_var["mail"].get()
        if not (re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+\b', new_customer.mail)):
            text_info += "- There is no email address.\n"
        new_customer.address = customer_string_var["address"].get()
        if not re.fullmatch(r"[a-zA-Z0-9\s._%+-]+, [a-zA-Z0-9\s._%+-]+\b", new_customer.address):
            text_info += "- It's not a good address.\n"
        if not text_info:
            new_customer.insert_db()
            self.customer_list: list = Customer.get_all()
            self.display_window_stock()
        for widget in self.frame_sort.winfo_children():
            widget.destroy()
        label_error: Label = Label(self.frame_sort, text=text_info)
        label_error.pack()

    def verify_car_insert(self, car_string_var: dict) -> None:
        """
        It verifies the data are correct for the new car
        :param car_string_var: The dictionary of the raw car
        """
        text_info: str = ""
        car: Car = Car()
        car.id_brand = Brand.get_id(car_string_var["nameBrand"].get())
        if not car.id_brand:
            text_info += "- There is no brand name.\n"
        car.id_type = Type.get_id(car_string_var["nameType"].get())
        if not car.id_type:
            text_info += "- There is no type name.\n"
        car.id_motor = Motor.get_id(car_string_var["nameMotor"].get())
        if not car.id_motor:
            text_info += "- There is no motor name.\n"
        car.date_tech_control = car_string_var["dateTechControl"].get()
        if not car.date_tech_control:
            text_info += "- There is no date for the tech control.\n"
        car.price = car_string_var["price"].get()
        if not car.price or not check_number_input(str(car.price), 1):
            text_info += "- It's not a good price.\n"
        car.promo = car_string_var["promo"].get()
        if not car.promo or not check_number_input(str(car.promo), 0, 100):
            text_info += "- It's not a good promotion.\n"
        if not text_info:
            car.insert_db()
            self.reset_car_lists()
            self.display_window_stock()
        for widget in self.frame_sort.winfo_children():
            widget.destroy()
        label_error: Label = Label(self.frame_sort, text=text_info)
        label_error.pack()

    def verify_deal(self, deal: dict) -> None:
        """
        It verifies that the data entered are corrects
        :param deal: The deal that contains the raw information checked
        """
        text_info: str = ""
        new_deal: Deal = Deal()
        raw_id_car = deal["id_car"].get().split()[0]
        if not raw_id_car:
            text_info += "- There is no car id chosen.\n"
        raw_id_customer = deal["id_customer"].get().split()[0]
        if not raw_id_customer:
            text_info += "- There is no customer id chosen.\n"
        raw_is_rent = deal["is_rent"]
        if raw_is_rent:
            date_start_rent: str = deal["date_start_rent"].get()
            if not date_start_rent:
                text_info += "- There is no date for the rent.\n"
            duration_days_rent: str = deal["duration_days_rent"].get()
            if not check_number_input(duration_days_rent):
                text_info += "- There is no duration for the rent.\n"
            new_deal.date_start_rent = date_start_rent
            new_deal.duration_days_rent = duration_days_rent
        if not text_info:
            new_deal.id_car = raw_id_car
            new_deal.id_customer = raw_id_customer
            new_deal.is_rent = raw_is_rent
            new_deal.insert_db()
            self.reset_car_lists()
            if new_deal.is_rent:
                self.display_window_rent()
            else:
                self.display_window_selling()
        for widget in self.frame_sort.winfo_children():
            widget.destroy()
        label_error: Label = Label(self.frame_sort, text=text_info)
        label_error.pack()

    def reset_car_lists(self) -> None:
        """
        It resets the main lists used in the program
        """
        self.car_list_stock: list = Car.get_car_list()
        self.deal_list: list = Deal.get_all()
        self.historic_deal_list: list = HistoricDeal.get_all()
        self.rent_list: list = []
        self.car_list_free: list = []
        for deal in self.deal_list:
            if deal.is_rent:
                self.rent_list.append(deal)
        for car in self.car_list_stock:
            counter: int = 0
            found: bool = False
            while counter < len(self.rent_list) and not found:
                if car.id == self.rent_list[counter].id_car:
                    found: bool = True
                counter += 1
            if not found:
                self.car_list_free.append(car)

    def reset_display_and_sort_frames(self, button_to_disable: Button):
        """
        It reset the two main frames and up all the button but disable one
        :param button_to_disable: The button that has to be disabled
        """
        for widget in self.frame_display.winfo_children():
            widget.destroy()
        for widget in self.frame_sort.winfo_children():
            widget.destroy()
        for widget in self.frame_buttons.winfo_children():
            if widget.widgetName == "button":
                widget["state"] = NORMAL
        button_to_disable["state"] = DISABLED


# It will launch the application
# ApplicationGUI()
