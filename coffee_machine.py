def calculate_ingredients(cups_num=1):
    water = 200 * cups_num
    milk = 50 * cups_num
    beans = 15 * cups_num
    message = f"""
For {cups_num} cups of coffee you will need:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
"""
    print(message.strip())


def main():
    print("Write how many cups of coffee you will need: ")
    cups = int(input())
    calculate_ingredients(cups)


main()
