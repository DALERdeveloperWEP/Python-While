ball = 0

print(
    'To‘plangan ball o‘yini'
)

while True:
    user_operator = input('Amal kiritng( +,stop ): ')

    if user_operator == '+':
        ball+=10
    elif user_operator == 'stop':
        break
    else:
        print("Faqat + yoki stop yozing!")
print(f'sizmig umumiy ballingiz {ball}')