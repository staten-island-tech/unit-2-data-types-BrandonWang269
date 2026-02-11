""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" values = [1,2.23,5,6,2,30,15]
print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" name = input("Mad Lib Project")
y = name.split( )
z = y[0]
print(y)
print(z)
 """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def evenorodd():
    x = int(input("give me a number"))
    if x % 2 == 0:
        print("even")
    if x % 2 == 1:
        print("odd")
evenorodd() """

""" bill = 100
tip_amount = int(input("Total is 100. How much tip"))
def tip_quality():
    print(f"Your total amount is{100+tip_amount}")
    if tip_amount <= 0:
        print("bad")
    elif tip_amount <= 15:
        print("okay")
    elif tip_amount <= 20:
        print("good")
    elif tip_amount <= 25:
        print("great")
tip_quality()
 """

""" def factor(x):
    print("the factors of", x, "are")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 1234567890

factor(num) """

import math
x = int(input("A number"))
y = int(input("Another number"))
print(math.gcd(x,y))