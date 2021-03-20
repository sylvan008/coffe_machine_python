import sys

MESSAGES = {
    "WATER": "ml of water",
    "MILK": "ml of milk",
    "BEANS": "grams of coffee beans",
    "CUPS": "disposable cups of coffee"
}

ERRORS = {
    0: "water",
    1: "milk",
    2: "beans",
    3: "coffee"
}

ESPRESSO = '1'
LATTE = '2'
CAPPUCCINO = '3'
BACK = 'back'
FILL = 'fill'
TAKE = 'take'
BUY = 'buy'
REMAINING = 'remaining'
EXIT = 'exit'


def create_amount(water, milk, beans, cups, money):
    return water, milk, beans, cups, money


# 0 - espresso, 1 - latte, 2 - cappuccino
RECIPES = (
    create_amount(water=250, milk=0, beans=16, cups=1, money=-4),
    create_amount(water=350, milk=75, beans=20, cups=1, money=-7),
    create_amount(water=200, milk=100, beans=12, cups=1, money=-6)
)


def calc_remainder_amount(amount, required_amount):
    return tuple(map(lambda ingredient, required: ingredient - required, amount, required_amount))


def check_amount(amount, required_amount):
    for i in range(len(amount)):
        if amount[i] - required_amount[i] < 0:
            return i
        else:
            return -1


# amount: (water, milk, beans, cups)
def coffee_order(variant, amount):
    variants = (ESPRESSO, LATTE, CAPPUCCINO)
    if variant in variants:
        variant_ = int(variant) - 1
        error = check_amount(amount[:-1], RECIPES[variant_][:-1])
        if error >= 0:
            print(f"Sorry, not enough {ERRORS[error]}!")
            return amount
        else:
            return calc_remainder_amount(amount, RECIPES[variant_])
    else:
        return amount


def buy(amount):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    variant = input()
    if variant == BACK:
        return amount
    else:
        return coffee_order(variant, amount)


def fill_ingredient(operation):
    print(f"Write how many {MESSAGES[operation]} do you want to add:")
    return int(input())


def fill(amount):
    operations = ['WATER', 'MILK', 'BEANS', 'CUPS']
    added_amount = [fill_ingredient(operation) for operation in operations]
    added_amount = create_amount(*added_amount, money=0)
    return tuple(map(lambda was, add: was + add, amount, added_amount))


def take(amount):
    money = amount[-1]
    print(f"I gave you ${money}")
    return calc_remainder_amount(amount,
                                 create_amount(water=0, milk=0, beans=0, cups=0, money=money))


def get_action(amount):
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == BUY:
        return buy(amount)
    elif action == FILL:
        return fill(amount)
    elif action == TAKE:
        return take(amount)
    elif action == REMAINING:
        remaining(*amount)
        return amount
    elif action == EXIT:
        sys.exit()
    else:
        print("Unknown action!")
        sys.exit()


def remaining(water=0, milk=0, beans=0, cups=0, money=0):
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money
""")


def main(water=0, milk=0, beans=0, cups=0, money=0):
    amount = create_amount(water, milk, beans, cups, money)
    while True:
        amount = get_action(amount)


main(water=400, milk=540, beans=120, cups=9, money=550)
