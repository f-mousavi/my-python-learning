import math

x = input("yek vorodi vared konid? ")

if x.isdigit():
    num = float(x)
    
    if num > 0:
        result = math.sqrt(num) 
        print("Jazr:", result)
    else:
        result = num ** 2
        print("Tavan 2:", result)
    
    y = result > 100
    print(f"Aya natije az 100 bozorgtare? {y}")
else:
    print("In yek addad sahih mosbat nist!")