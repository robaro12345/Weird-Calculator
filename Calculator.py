import math

def Calculate(Greating):
    standard_or_Trigo = input(f"{Greating} \nWhat would you like to calculate numbers or trignometric values ? Trigo or No ")
    if standard_or_Trigo == "No":
        no_variable = int(input(f"What is the number of variables you will like to calculate? "))
        value = 0
        value = input("What would you first variable be ?")
        if '.' in value:
            value = float(value)
        else:
            value = int(value)

        no_variable -= 1
        while no_variable != 0 :
            calculable_amount = input("What is the number you will like  operate with? ")
            if '.' in calculable_amount:
                calculable_amount = float(calculable_amount)
            else:
                calculable_amount = int(calculable_amount)
            operator = input("What would you like operator to be ? please mention from (plus, minus, multi or div).")
            if operator == "plus":
                value += calculable_amount
                no_variable -= 1
                print(f"the value now is {value} and the number of variable left are {no_variable}")
            elif operator == "minus":
                value -= calculable_amount
                no_variable -= 1
                print(f"the value now is {value} and the number of variable left are {no_variable}")
            elif operator == "multi":
                value *= calculable_amount
                no_variable -= 1
                print(f"the value now is {value} and the number of variable left are {no_variable}")
            elif operator == "div":
                value /= calculable_amount
                no_variable -= 1
                print(f"the value now is {value} and the number of variable left are {no_variable}")
    elif standard_or_Trigo == "Trigo":
        valuet = 0 
        toperator = input("Which operator would you like to you ? sin, cos, tan, cosec, sec or cot ")
        inputvalue = int(input("What angle would you like to take ? "))
        decimal = int(input("Till how many decimals would you  like your answers to be ? "))
        if toperator == "sin":
            print(f"The value of sin {inputvalue} is {round(math.sin(math.radians(inputvalue)), decimal)}")
        elif toperator == "cos":
            print(f"The value of cos {inputvalue} is {round(math.cos(math.radians(inputvalue)), decimal)}")
        elif toperator == "tan":
            print(f"The value of tan {inputvalue} is {round(math.tan(math.radians(inputvalue)), decimal)}")
        elif toperator == "cosec":
            print(f"The value of cosec {inputvalue} is {round(1/(math.sin(math.radians(inputvalue))), decimal)}")
        elif toperator == "sec":
            print(f"The value of sec {inputvalue} is {round(1/(math.cos(math.radians(inputvalue))), decimal)}")
        elif toperator == "cot":
            print(f"The value of cot {inputvalue} is {round(1/(math.tan(math.radians(inputvalue))), decimal)}")

Calculate(Greating="Hello")
redo = input("Do you want to perform any other calculation ? Yes or No ")
while redo == "Yes":
    Calculate(Greating="Hello again")
else:
    print("Then Goodbye")

input()
    