import operator
import random


def generate_math_exericse(number_of_exericse = 10, substraction=True):
    number1 = 10
    number2 = 10
    for i in range(1,number_of_exericse):
        op = random.choice(["+", "-"])
        if "-" in op:
            while True:
                a = random.randint(1, number1)
                b = random.randint(1, number2)
                if a >= b:
                    print random.randint(1, number1), op, random.randint(1, number2), " ="
                    break
        else:
            print random.randint(1, number1), op, random.randint(1, number2)," ="

generate_math_exericse()