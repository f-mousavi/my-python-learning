adad1 = float(input("عدد اول: "))
adad2 = float(input("عدد دوم: "))
amalgard = input("عملگر (+ - * /): ")

if amalgard == "+":
    print(adad1 + adad2)
elif amalgard == "-":
    print(adad1 - adad2)
elif amalgard == "*":
    print(adad1 * adad2)
elif amalgard == "/":
    if adad2 == 0:
        print("تقسیم بر صفر ممکن نیست!")
    else:
        print(round(adad1 / adad2, 2))
else:
    print("عملگر اشتباه!")