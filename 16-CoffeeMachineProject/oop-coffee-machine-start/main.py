from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


buka = True
uang = MoneyMachine()
buatkopi = CoffeeMaker()
menu = Menu()

uang.report()
buatkopi.report()


while buka:
    pilih = input(f"Mau minum apa? ({menu.get_items()}): ")
    if pilih == "off":
        buka = False
    elif pilih == "report":
        uang.report()
        buatkopi.report()
    else:
        order = menu.find_drink(pilih)

        ada = buatkopi.is_resource_sufficient(order)
        if ada:
            acc = uang.make_payment(order.cost)
            if acc:
                buatkopi.make_coffee(order)

