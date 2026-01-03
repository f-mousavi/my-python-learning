print("=" * 50)
print("خوش اومدی به معرفی‌کننده شخصی!")

name = input("اسمت چیه؟ ")
age = int(input("چند سالته؟ "))
city = input("شهرت کجاست؟ ")
favorite_num = int(input("عدد مورد علاقه‌ت چنده؟ "))
python_like = input("پایتون دوست داری؟ (yes/no) ")

name_nice = name.title()
total = age * favorite_num

intro = f"""
سلام {name_nice} عزیز از {city.title()}! 
تو {age} سالته و عدد جادویی‌ت {favorite_num} هست.
{age}*{favorite_num} = {total} انرژی مثبت داری!
"""

python_msg = "عااالی! آینده روشنی تو پایتون داری 🚀" if python_like.lower() == "yes" else "پایتون خیلی باحاله — امتحان کن! "

print(intro)
print(python_msg)