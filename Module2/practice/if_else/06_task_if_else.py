age = int(input('Введите год = '))
if (age % 4) == 0 or (age % 400) == 0:
    print('Високосный')
else:
    print('обычный')
