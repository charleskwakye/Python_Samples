# Ex 1
def degrees_celcius(celsius):
    return(float(celsius)*(9/5) + 32)
celsius = input("Degrees Celsius: ")
print(celsius, "degrees Celsius = ", degrees_celcius(celsius), "degrees Fahrenheit")
