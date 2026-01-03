print("*" * 50)
print("      خوش اومدی به تولیدکننده پروفایل شخصی!")
print("*" * 50)

# گرفتن اطلاعات از کاربر
name = input("اسمت چیه؟ ")
age = int(input("چند سالته؟ "))
city = input("شهرت کجاست؟ ")
favorite_num = int(input("عدد مورد علاقه‌ت چنده؟ "))
python_like = input("پایتون دوست داری؟ (yes/no) ")

# پردازش و قشنگ کردن اطلاعات
name_nice = name.title()
city_nice = city.upper()
name_length = len(name)
total_power = age * favorite_num
name_reverse = name[::-1]

# ساخت پیام بر اساس علاقه به پایتون (با ترفند یه خطی)
python_msg = "عااالی! تو یکی از آینده‌دارهای پایتون هستی 🚀" if python_like.lower() == "yes" else "پایتون خیلی باحاله، حتماً امتحان کن! 😊"

# چاپ پروفایل نهایی
print("\n" + "=" * 50)
print(f"پروفایل {name_nice}")
print("=" * 50)
print(f"سن: {age} سال")
print(f"شهر: {city_nice}")
print(f"طول اسم: {name_length} حرف")
print(f"قدرت جادویی (سن × عدد مورد علاقه): {total_power}")
print(f"اسم برعکس: {name_reverse}")
print(f"علاقه به پایتون: {python_msg}")
print("=" * 50)
print("ممنون که پروفایل ساختی! موفق باشی 🌟")