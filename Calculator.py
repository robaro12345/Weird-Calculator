no_variable = int(input("Hello \n What is the number of variables you will like to calculate? "))

value = int(input("What would you first variable be ?")) 
no_variable -= 1
while no_variable != 0 :
    calculable_amount = int(input("What is the number you will like  operate with? "))
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

