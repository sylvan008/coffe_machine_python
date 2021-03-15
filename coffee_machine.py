MESSAGES = {
    "WATER": "ml of water",
    "MILK": "ml of milk",
    "BEANS": "grams of coffee beans",
    "CUPS": "disposable cups of coffee"
}

ESPRESSO = '1'
LATTE = '2'
CAPPUCCINO = '3'
FILL = 'fill'
TAKE = 'take'
BUY = 'buy'


def calc_remainder_ingredients(ingredients, required_ingredients):
    return tuple(map(lambda ingredient, required: ingredient - required, ingredients, required_ingredients))


# ingredients: (water, milk, beans, cups)
def coffee_order(variant, ingredients, money):
    if variant == ESPRESSO:
        required_ingredients = (250, 0, 16, 1)
        return calc_remainder_ingredients(ingredients, required_ingredients), money + 4
    elif variant == LATTE:
        required_ingredients = (350, 75, 20, 1)
        return calc_remainder_ingredients(ingredients, required_ingredients), money + 7
    elif variant == CAPPUCCINO:
        required_ingredients = (200, 100, 12, 1)
        return calc_remainder_ingredients(ingredients, required_ingredients), money + 6
    else:
        return ingredients, money


def buy(ingredients, money):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    variant = input()
    return coffee_order(variant, ingredients, money=money)


def fill_ingredient(operation):
    print(f"Write how many {MESSAGES[operation]} do you want to add:")
    return int(input())


def fill(ingredients):
    operations = ['WATER', 'MILK', 'BEANS', 'CUPS']
    added_ingredients = [fill_ingredient(operation) for operation in operations]
    return tuple(map(lambda was, add: was + add, ingredients, added_ingredients))


def take(money=0):
    print(f"I gave you ${money}")
    return 0


def get_action(ingredients, money):
    print("Write action (buy, fill, take):")
    action = input()
    if action == BUY:
        return buy(ingredients, money)
    elif action == FILL:
        return fill(ingredients), money
    elif action == TAKE:
        return ingredients, take(money)


def print_report(water=0, milk=0, beans=0, cups=0, money=0):
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money
""")


def main(water=0, milk=0, beans=0, cups=0, money=0):
    ingredients = (water, milk, beans, cups)
    print_report(*ingredients, money=money)
    ingredients, money = get_action(ingredients, money)
    print_report(*ingredients, money=money)


main(water=400, milk=540, beans=120, cups=9, money=550)
