import logging
logging.basicConfig(level=logging.INFO)


def add(number_one, number_two):
    logging.info(f"Dodaje liczbe {number_one} i {number_two}")
    add_result = number_one + number_two
    print(f"Wynik to {add_result}")


def subtract(number_one, number_two):
    logging.info(f"Odejmuje liczbe {number_one} i {number_two}")
    subtract_result = number_one - number_two
    print(f"Wynik to {subtract_result}")


def multiply(number_one, number_two):
    logging.info(f"Mnozę liczbę {number_one} i {number_two}")
    multiply_result = number_one * number_two
    print(f"Wynik to {multiply_result}")


def divide(number_one, number_two):
    logging.info(f"Dzielę liczbę {number_one} i {number_two}")
    divide_result = number_one / number_two
    print(f"Wynik to {divide_result}")


if __name__ == "__main__":
    type_math_activity = int(input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie: "))
    number_one = float(input("Podaj składnik 1. "))
    number_two = float(input("Podaj składnik 2. "))

    if type_math_activity == 1:
        add(number_one, number_two)
    elif type_math_activity == 2:
        subtract(number_one, number_two)
    elif type_math_activity == 3:
        multiply(number_one, number_two)
    else:
        divide(number_one, number_two)
