import random

exerciseformat = "{} {} {} ="

#generate number of math exercise
#substraction is true will include the substract opeartion
#number1 op number2
def generate_math_exericse(number_of_exercise = 50, substraction=True):
    number1_lower_bound = 5
    number1_upper_bound = 10
    number2_lower_bound = 1
    number2_upper_bound = 10
    generated = dict()
    for i in range(1,number_of_exercise):
        op = random.choice(["+"])
        if substraction:
            op = random.choice(["+", "-"])
        while True:
            a = random.randint(number1_lower_bound, number1_upper_bound)
            b = random.randint(number2_lower_bound, number2_upper_bound)
            exercise = exerciseformat.format(a,op,b)
            if "-" in op and a >= b and exercise not in generated:
                print exercise
                break
            if "+" in op:
                if exercise not in generated:
                    print exercise
                    break
            generated[exercise] = "1"

#default
generate_math_exericse()
#addtion only
generate_math_exericse(substraction=False)