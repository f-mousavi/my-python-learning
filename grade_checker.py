nomre = float(input("نمره‌ت چنده؟ (۰-۲۰) "))
if nomre < 0 or nomre > 20:
    print("نمره نامعتبر!")
elif nomre >= 19:
    print("A+ 🏆")
elif nomre >= 17:
    print("A ⭐")
elif nomre >= 14:
    print("B 👍")
elif nomre >= 10:
    print("C")
else:
    print("fail 😔")