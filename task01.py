from random import randint
random_num = randint(1,20)

print(
        "Raqam topish o‘yini\n"
        "--------O'yin shartlari--------\n"
        "PC random yani(1,20) son orali'gida tanlaydi"
        "foydalanuvchi raqam kiritadi\n"
        "PC random raqami bilan birxil bolsa\n"
        "(Siz yashirin raqam toptiz)\n"
        "Aks holdi\n"
        "(Katta son\\Kichik son);\n"
        "-----------------------------------------------------"
    )

while True:
    user_random = int(input('Raqam kiriting: '))

    if user_random > random_num:
        print('Kichik son')
    elif user_random < random_num:
        print('Katta son')
    elif user_random == random_num:
        break
print(f"Siz yashirin raqam toptiz \nYashirin raqam: {random_num}")