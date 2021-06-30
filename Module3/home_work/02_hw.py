ans = ''
i = 0
import random
numbers = []
while True:
    a = random.randint(-100, 100)
    i += 1
    numbers.append(a)
    if i % 5 == 0:
        print(numbers)
        print('Продолжить?')
        ans = input('Ответ: ')

    if ans == 'нет':
        break

print()
print()
print(numbers)
