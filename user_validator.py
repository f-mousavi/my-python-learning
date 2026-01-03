name=input("name khod ra vared konid:")
if len(name)>=5 and name.lower().startswith("a" or "A"):
    print(name.upper(), "Access Granted")
else:
    print("Invalid Username")