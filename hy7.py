def F(a):
    f = (a-32)/1.8
    print("Fahrenheit "+str(a) + "°is Celsius " + str(f)+"°.")
def C(a):
    c = a*1.8 + 32
    print("Celsius "+str(a) + "°is Fahrenheit" + str(c)+"°.")
a = input("Enter the Celsius temperature to convert:")
C(int(a))
a = input("Enter the Fahrenheit temperature to convert:")
F(int(a))