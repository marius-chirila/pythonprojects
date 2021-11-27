from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def clear():
    os.system('cls' if os.name=="nt" else 'clear')


menu = Menu()
coffee_maker = CoffeeMaker()
menu_items = menu.get_items()
moneyReport = MoneyMachine()



# clear()
turn_off = False
while not turn_off:
    choice = input(f" What would you like ? {menu_items}:").lower()
    if choice == "off":
        clear()
        turn_off = True
    elif choice == "report":
        coffee_maker.report()
        moneyReport.report()
    elif menu.find_drink(choice):
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
            if moneyReport.make_payment(menu.find_drink(choice).cost):
                coffee_maker.make_coffee(menu.find_drink(choice))
    else:
        turn_off = True
