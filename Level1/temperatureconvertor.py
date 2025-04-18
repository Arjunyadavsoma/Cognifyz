def celsius_to_fahrenheit(Celsius):
    return (Celsius*9/5)+32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

#Task invovles only Celsius and fahrenheit Conversion 
#but for pratice i have written additional convertions too

def kelvin_to_celsius(Kelvin):
    return Kelvin-273.15

def celsius_to_kelvin(Celsius):
    return Celsius+273.15

def fahrenheit_to_kelvin(Fahrenheit):
    celsius=fahrenheit_to_celsius(Fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fehrenheit(Kelvin):
    celsius=kelvin_to_celsius(Kelvin)
    return celsius_to_fahrenheit(celsius)


print("Choose any one below suitable option:\n1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius\n3.Kelvin to Celsius\n4.Celsius to Kelvin")
print("5.fahrenheit to Kelvin\n6.Kelvin to Fahrenheit")
choice=int(input("Enter the option : "))

if(choice==1):
    Celsius=float(input("Coverting from Celsius to Fahrenheit \n Enter the value in Celsius : "))
    print(celsius_to_fahrenheit(Celsius))

elif(choice==2):
    Fahrenheit=float(input("Converting from Fahrenheit to Celsius \n Enter the value in Fahrenheit : "))
    print(fahrenheit_to_celsius(Fahrenheit))

elif(choice==3):
    Kelvin=float(input("Converting from Kelvin to Celsius \n Enter the value in Kelvin : "))
    print(kelvin_to_celsius(Kelvin))

elif(choice==4):
    Celsius=float(input("Converting from Celsius to Kelvin \n Enter the value in Celsius : "))
    print(celsius_to_kelvin(Celsius))

elif(choice==5):
    Fahrenheit=float(input("Converting from Fahrenheit to Kelvin \n Enter the value in Fahrenheit : "))
    print(fahrenheit_to_kelvin(Fahrenheit))

elif(choice==6):
    Kelvin=float(input("Converting from Kelvin to Fahrenheit \n Enter the value in Kelvin : "))
    print(kelvin_to_fehrenheit(Kelvin))

else:
    print("Enter a valid option.")