a = int(input('Введите сторону а = '))
b = int(input('Введите сторону b = '))
c = int(input('Введите сторону c = '))

if (a + b) > c or (a + c) > b or (b + c) > a:
    if a == b:
        print('yes')

    elif a == c:
        print('yes')

    elif b == c:
        print('yes')

    else:
        print('no')



else:
    print('Треугольника с такими сторонами не существует!!!')
