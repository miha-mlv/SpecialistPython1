first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
i = 0
for a in range(first_number, second_number + 1):
    if a % 3 == 0:
        i += 1
        print(str(i) + '.', str(a))
    else:
        continue
