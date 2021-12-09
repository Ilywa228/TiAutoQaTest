from math import sqrt

coordinates = []
names_of_dots = ["A", "B", "C"]
for i in names_of_dots:
    x = float(input(f"Enter coordinate x of dot {i}: "))
    y = float(input(f"Enter coordinate y of dot {i}: "))
    coordinates.extend((x, y))

x1, x2, x3 = [j for i,j in enumerate(coordinates) if i % 2 == 0]
y1, y2, y3 = [j for i,j in enumerate(coordinates) if i % 2 == 1]

a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
print("Length of AB is: ", a)
print("Length of BC is: ", b)
print("Length of AC is: ", c)

if (a == b) and (b == c) and (a == c):
    print("Triangle is Equailateral")
else:
    print("Triangle is Not Equailateral")

if (a == b) or (a == c) or (b == c):
    print("Triangle is Isosceles")
else:
    print("Triangle is Not Isosceles")

if not round(((a ** 2 + b ** 2) - c ** 2) * ((a ** 2 + c ** 2) - b ** 2) * ((c ** 2 + b ** 2) - a ** 2)):
    print("Triangle is Right")
else:
    print("Triangle is Not Right")

per = a + b + c
print("Perimeter: ", per)

print([i for i in range(int(per + 1)) if i % 2 == 0])