MESSAGES = {
    "WATER": "Write how many ml of water the coffee machine has:",
    "MILK": "Write how many ml of milk the coffee machine has:",
    "BEANS": "Write how many grams of coffee beans the coffee machine has:",
    "CUPS": "Write how many cups of coffee you will need:"
}


def calculate_cups(ingredients):
    dividers = (200, 50, 15)
    return min(map(lambda ingredient, divider: ingredient // divider, ingredients, dividers))


# Get ingredient amount from user. Return integer
def get_amount(message):
    print(message)
    return int(input())


def can_create_coffee(available_cups=0, ordered_cups=0):
    remainder_cups = available_cups - ordered_cups
    if remainder_cups < 0:
        print(f"No, I can make only {available_cups} cup(s) of coffee")
    elif remainder_cups == 0:
        print("Yes, I can make that amount of coffee")
    else:
        print(f"Yes, I can make that amount of coffee (and even {remainder_cups} more than that)")


def main():
    water = get_amount(MESSAGES['WATER'])
    milk = get_amount(MESSAGES['MILK'])
    beans = get_amount(MESSAGES['BEANS'])
    ordered_cups = get_amount(MESSAGES['CUPS'])
    available_cups = calculate_cups((water, milk, beans))
    can_create_coffee(available_cups=available_cups, ordered_cups=ordered_cups)


main()
