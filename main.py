# CLASSES
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# -------------------------------------------------------------------------------------------------- #

# OBJECTS
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# -------------------------------------------------------------------------------------------------- #

# GLOBAL VARIABLES
ON = True

# -------------------------------------------------------------------------------------------------- #

while ON:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        ON = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)