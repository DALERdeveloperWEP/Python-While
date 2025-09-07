
print(
    ' Kalkulyator (oddiy versiya)'
)

while True:
    num1 = float(input('1 - son: '))    
    num2 = float(input('2 - son: '))
    operator = input("amal: ")

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)

    user = input("Davom etasizmi? (ha/yoq): ")

    if user == 'yoq':break