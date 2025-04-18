def reverse_string(s):
    return s[::-1]


print(f"Example of hello : {reverse_string("hello")}")
word=input("Enter the String to reverse :")
reversed_string=reverse_string(word)

print(f"Reversed string is : {reversed_string}")