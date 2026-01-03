from math import pi

radius = float(input("شعاع دایره رو وارد کن: "))

mohit = 2 * pi * radius
masahat = pi * radius ** 2

print(f"محیط دایره: {round(mohit, 2)}")
print(f"مساحت دایره: {round(masahat, 2)}")