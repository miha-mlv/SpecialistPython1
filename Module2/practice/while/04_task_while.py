kir = 1
ans = 0
lvl = int(input('Сколько уровней у пирамиды: '))
while kir <= lvl:
    ans = ans + kir
    kir += 1
print('Сумма чисел написанных на кирпичах = ' + str(ans))
