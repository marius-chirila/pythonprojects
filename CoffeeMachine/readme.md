# Coffee Vending Machine app

Easy coffee vending machine code which offers 3 choices of beverages and operates by coins.
Coffee, Latte or Cappuccino. 

You can use it by typing the required beverage, type the number and type of coins inserted, and you'll receive the coffee and change if there are sufficient resources inside the coffee vending machine.
Type "report" to see the resources present.
Type "off" to shut down the vending machine.

## Example
```py
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
            dimes = int(input("How many quarters?: "))
            nickles = int(input("How many quarters?: "))
            pennies = int(input("How many quarters?: "))
            if(process_money(quarters, dimes, nickles, pennies, choice)):
                make_coffee(choice)
            else:
                turn_off = False
        else:
            turn_off = False
    else:
        print("You tried to order something not on the menu, try again.")
```