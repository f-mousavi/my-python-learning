x=float(input("shoa ra vared konid:"))
y=input("mohit ya masahat?")
from math import pi
match y:
    case "mohit":
        print(round(2*pi*x,3))
    case "masahat":
        print(round(pi * pow(x, 2), 3))
    case _:
        print("Wrong Choice")