import logging
logging.basicConfig(level=logging.INFO)

def add(number_one, number_two):
    logging.info("Dodaje liczbe " + str(number_one) + " i " + str(number_two))
    add_result = number_one + number_two
    print("Wynik to " + str(add_result))
    
def subtract(number_one, number_two):
    logging.info("Odejmuje liczbe " + str(number_one) + " i " + str(number_two))
    subtract_result = number_one - number_two
    print("Wynik to " + str(subtract_result))

def multiply(number_one, number_two):
    logging.info("Mnozę liczbę " + str(number_one) + " i " + str(number_two))
    multiply_result = number_one * number_two
    print("Wynik to " + str(multiply_result))
    
def divide(number_one, number_two):
    logging.info("Mnozę liczbę " + str(number_one) + " i " + str(number_two))
    divide_result = number_one / number_two
    print("Wynik to " + str(divide_result))

if __name__ == "__main__":    
    type_math_activity = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie: "))
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
