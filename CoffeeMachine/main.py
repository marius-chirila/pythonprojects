from data import MENU, resources
import os
from art import logo

def clear():
    os.system('cls' if os.name=="nt" else 'clear')

#making the coffee function 
def make_coffee(type):
    for i in MENU[type]["ingredients"]:
        resources[i] -= MENU[type]["ingredients"][i]
    return print(f"Here is your {type} ☕. Enjoy!")

# Processing the sum of coins inserted, and incrementing it to the vending machine resources
def process_money(type1, type2, type3, type4, type_of_coffee):
    total_money = (type1*0.25) + (type2*0.1) + (type3*0.05) + (type4*0.01)
    if total_money > MENU[type_of_coffee]["cost"]:
        resources["money"] += MENU[type_of_coffee]["cost"]
        rest = total_money - MENU[type_of_coffee]["cost"]
        print(f'Here is your ${round(rest,2)} in change.')
        return True
    elif total_money == MENU[type_of_coffee]["cost"]:
        resources["money"] += MENU[type_of_coffee]["cost"]
        rest = total_money - MENU[type_of_coffee]["cost"]
        print(f"You inserted the exact amount of money.")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
# listing the resources in the vending machine.
def report():
    for i in resources:
        if i == "water" or i == "milk":
            print(f'{i.title()}: {resources[i]}ml')
        elif i == "coffee":
            print(f'{i.title()}: {resources[i]}g')
        else:
            print(f'{i.title()}: ${resources[i]}')

# Checking if there are enough resources to make the selected coffee.
def check_resources(type):
    for i in MENU[type]["ingredients"]:
        if MENU[type]["ingredients"][i] <= resources[i]:
            True
        else:
            print(f"Sorry, there is not enough {i}.")
            return False
    return True

#main program
clear()
print(logo)
turn_off = False
while not turn_off:
    choice = input(" What would you like ? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        clear()
        turn_off = True
    elif choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            print(f'Please insert coins. A {choice} costs ${MENU[choice]["cost"]}')
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if(process_money(quarters, dimes, nickles, pennies, choice)):
                make_coffee(choice)
            else:
                turn_off = False
        else:
            turn_off = False
    else:
        print("You tried to order something not on the menu, try again.")
        
        