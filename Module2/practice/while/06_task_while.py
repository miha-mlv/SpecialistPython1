number = int(input('Введите цело число = '))
ans = 0
sum = 0
for a in range(number):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum > a:
        for i in range(1, sum):
            ans = 0
            if sum % i == 0:
                ans += i
        if ans == a:
            print(ans, sum)
