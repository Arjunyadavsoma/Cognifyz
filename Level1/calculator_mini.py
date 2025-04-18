def calculator(number1,number2,operator):
    if(operator=='+'):
        print(f"Addition of {number1} and {number2} is {number1+number2}") 

    elif(operator=='-'):
        print(f"Subtraction of {number1} and {number2} is {number1-number2}") 

    elif(operator=='*'):
        print(f"Multiplication of {number1} and {number2} is {number1*number2}")

    elif(operator=='/'):
        if number2 != 0:
            print(f"Division of {number1} by {number2} is {number1 / number2}")
        else:
            print("Error: Division by zero is not allowed.")
    elif(operator=='%'):
        if number2 != 0:
            print(f"Modulus of {number1} and {number2} is {number1 % number2}")
        else:
            print("Error: Modulus by zero is not allowed.")

operator=input("Enter the operation to perform (+, -, *, /, %) : ")
operator_list="+-*/%"
if operator not in operator_list:
    print("Enter a valid operator from (+, -, *, /, %)")
else:
    number1=float(input("Enter the first number : "))
    number2=float(input("Enter the second number : "))
    calculator(number1,number2,operator)
