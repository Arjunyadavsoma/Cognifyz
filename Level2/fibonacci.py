# Write a Python function that generates the Fibonacci sequence up to a given number of
# terms. The function should take an integer input from the user and display the
# Fibonacci sequence up to that number of terms

def fibonacci(number):
    start_number=0
    next_number=1
    add=0
    print("Fibonnacci series is : ",end='')
    for i in range (number):
        print(' ',start_number,end='')
        add=start_number+next_number
        start_number=next_number
        next_number=add
        
number=int(input("Enter the number of Fibonacci terms you need : "))
fibonacci(number)