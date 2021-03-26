import sys

MESSAGES = {
    0: "ml of water",
    1: "ml of milk",
    2: "grams of coffee beans",
    3: "disposable cups of coffee"
}

ERRORS = {
    0: "water",
    1: "milk",
    2: "beans",
    3: "coffee"
}

STATE = {
    'MAIN': 0,
    'BUY': 1,
    'FILL': 2,
    'FILL_WATER': 0,
    'FILL_MILK': 1,
    'FILL_BEANS': 2,
    'FILL_CUPS': 3,
    'FILL_END': 4
}

MAIN = 'MAIN'
ESPRESSO = '1'
LATTE = '2'
CAPPUCCINO = '3'
BACK = 'BACK'
FILL = 'FILL'
FILL_WATER = 'FILL_WATER'
FILL_MILK = 'FILL_MILK'
FILL_BEANS = 'FILL_BEANS'
FILL_CUPS = 'FILL_CUPS'
FILL_END = 'FILL_END'
TAKE = 'TAKE'
BUY = 'BUY'
REMAINING = 'REMAINING'
EXIT = 'EXIT'


def create_amount(water, milk, beans, cups, money):
    return water, milk, beans, cups, money


# 0 - espresso, 1 - latte, 2 - cappuccino
RECIPES = (
    create_amount(water=250, milk=0, beans=16, cups=1, money=-4),
    create_amount(water=350, milk=75, beans=20, cups=1, money=-7),
    create_amount(water=200, milk=100, beans=12, cups=1, money=-6)
)

COFFEES = (ESPRESSO, LATTE, CAPPUCCINO)


def calc_remainder_amount(amount, required_amount):
    return tuple(map(lambda ingredient, required: ingredient - required, amount, required_amount))


def get_action(coffee_machine):
    input_ = input().upper()
    coffee_machine.action(input_)


class CoffeeMachine:
    def __init__(self, amount):
        self.amount = amount
        self.state = 0
        self.fill_state = 0

    def __str__(self):
        return """
The coffee machine has:
{0} of water
{1} of milk
{2} of coffee beans
{3} of disposable cups
{4} of money
""".format(*self.amount)

    def get_message(self):
        if self.state == STATE[BUY]:
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.state == STATE[FILL]:
            return f"Write how many {MESSAGES[self.fill_state]} do you want to add:"
        return "Write action (buy, fill, take, remaining, exit):"

    def action(self, input_):
        if self.state == STATE[MAIN]:
            if input_ == REMAINING:
                self._remaining()
            elif input_ == FILL:
                self.state = STATE[FILL]
            elif input_ == TAKE:
                self.amount = self._take()
            elif input_ == BUY:
                self.state = STATE[BUY]
            elif input_ == BACK:
                self.state = STATE[MAIN]
            elif input_ == EXIT:
                self._switch_off()
        elif self.state == STATE[BUY]:
            remainder = self._buy(input_)
            self.amount = remainder
            self.state = STATE[MAIN]
        elif self.state == STATE[FILL]:
            self.amount = self._fill(filled=input_)

    def _fill(self, filled):
        added_amount = [*self.amount]
        added_amount[self.fill_state] += int(filled)
        state = self._get_next_fill()
        if state == STATE[FILL_END]:
            self.state = STATE[MAIN]
            self.fill_state = STATE[FILL_WATER]
        else:
            self.fill_state = state
        return tuple(added_amount)

    def _get_next_fill(self):
        if self.fill_state == STATE[FILL_WATER]:
            return STATE[FILL_MILK]
        elif self.fill_state == STATE[FILL_MILK]:
            return STATE[FILL_BEANS]
        elif self.fill_state == STATE[FILL_BEANS]:
            return STATE[FILL_CUPS]
        elif self.fill_state == STATE[FILL_CUPS]:
            return STATE[FILL_END]

    def _take(self):
        money = self.amount[-1]
        print(f"I gave you ${money}")
        return calc_remainder_amount(self.amount,
                                     create_amount(water=0, milk=0, beans=0, cups=0, money=money))

    def _remaining(self):
        print(self)

    def _buy(self, variant):
        if variant == BACK:
            return self.amount
        else:
            return self._coffee_order(coffee=variant, amount=self.amount)

    # amount: (water, milk, beans, cups)
    def _coffee_order(self, coffee, amount):
        if coffee in COFFEES:
            coffee = int(coffee) - 1
            error = self._check_amount(RECIPES[coffee][:-1])
            if error >= 0:
                print(f"Sorry, not enough {ERRORS[error]}!")
                return amount
            else:
                return calc_remainder_amount(amount, RECIPES[coffee])
        else:
            return amount

    def _check_amount(self, required_amount):
        for i in range(len(self.amount[:-1])):
            if self.amount[i] - required_amount[i] < 0:
                return i
            else:
                return -1

    def _switch_off(self):
        sys.exit(self)


def main():
    coffee_machine = CoffeeMachine(create_amount(water=400, milk=540, beans=120, cups=9, money=550))
    while coffee_machine:
        print(coffee_machine.get_message())
        get_action(coffee_machine)


main()
