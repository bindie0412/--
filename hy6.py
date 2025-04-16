def area(a):
    print("The area of the circle is: " + str(3.14 * a * a))
def cir(a):
    print("The circumference of the circle is: " + str(2 * 3.14 * a))
a = input("Enter the radius of the circle:")
area(int(a))
cir(int(a))