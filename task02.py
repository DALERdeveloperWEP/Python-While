password = "python123"

print(
    'Parol tekshirish dasturi'
)

while True:
    user_password = input('Parol kiritng: ')

    if user_password == password:
        break
    else:
        print("Xato! Qayta urinib ko‘ring.")
print("Xush kelibsiz!")