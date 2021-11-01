# coffeeMaker.py
#
# Python Bootcamp Day 16 - Coffee Maker Redeux
# Usage:
#      Create software for a hypothetical coffee machine using OOP.
#
# Marceia Egler October 11, 2021


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_maker():

    machine_on = True
    coffee = CoffeeMaker()
    menu = Menu()
    money = MoneyMachine()

    while machine_on:
        place_order = input(f"What would you like? ({menu.get_items()}): ")
        if place_order == "off":
            return False
        elif place_order == 'report':
            coffee.report()
            money.report()
            continue
        order = menu.find_drink(place_order)
        if menu.find_drink(place_order):
            if coffee.is_resource_sufficient(order) and money.make_payment(order.cost):
                coffee.make_coffee(order)
            else:
                machine_on = False


coffee_maker()
