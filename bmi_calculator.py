# گرفتن اطلاعات از کاربر
# چون ورودی‌های کاربر به صورت متن هستن، با float اون‌ها رو به عدد اعشاری تبدیل می‌کنیم
age = float(input("Lotfan sen khod ra vared konid: "))
weight = float(input("Lotfan vazn khod ra vared konid (kg): "))
height = float(input("Lotfan ghad khod ra vared konid (meter - masalan 1.75): "))

# محاسبه BMI
# از تابع pow که یاد گرفتی برای توان ۲ استفاده می‌کنیم
bmi = weight / pow(height, 2)

# نمایش نتیجه BMI با دو رقم اعشار
print("BMI shoma dar amade ast:", round(bmi, 2))

# بخش شرطی برای بررسی وضعیت (این همون بخش جدیده!)
if bmi < 18.5:
    print("Vaziate shoma: Laghar")
elif 18.5 <= bmi <= 24.9:
    print("Vaziate shoma: Normal")
elif 25 <= bmi <= 29.9:
    print("Vaziate shoma: Ezafe Vazn")
else:
    print("Vaziate shoma: Chagh")