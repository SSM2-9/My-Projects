import math
from math import sqrt

print("Welcome to the Quadratic Equation Calculator! \n")
print("Enter your values for a, b, and c to solve ax^2 + bx + c : \n")

#Value of 'a' being determined
a = input("a = ")

while not a.startswith('-') and a.isnumeric() == False:
  print("Please enter a number!"),
  a = (input("a = "))

else:
    a = int(a)


#Value of 'b' being determined
b = (input("b = "))

while not b.startswith('-') and b.isnumeric() == False:
  print("Please enter a number!")
  b = (input("b = "))

else:
    b = int(b)


#Value of 'c' being determined
c = (input("c = "))

while not c.startswith('-') and c.isnumeric() == False:
  print("Please enter a number!"),
  c = (input("c = "))

else:
    c = int(c)

discriminant = int(b**2 - 4*a*c)

if discriminant > 0:
  print("This equation has two real solutions and they are as follows: ")

  x_1 = (-b + math.sqrt(discriminant)) / 2*a
  x_2 = (-b - math.sqrt(discriminant)) / 2*a

  print(x_1, x_2)


elif discriminant == 0:
  print("This equation has only one real solutions and it is as follows: ")

  x_1 = (-b + math.sqrt(discriminant)) / 2*a

  print(x_1)


elif discriminant < 0:
  print("This equation has two imaginary solutions and therefore cannot produce the output")
