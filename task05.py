count = 0

while True:
    user = input('Matn kiritng: ')
    if user.lower() == 'stop':
        break
    else:
        count += 1
print("Siz", count, "marta matn kiritdingiz.")