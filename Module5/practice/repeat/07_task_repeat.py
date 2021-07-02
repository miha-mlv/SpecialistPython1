def deposit(x, a, n):
    q = x / 100
    w = q * a
    qw = w * n
    ans = x + qw
    return ans


x = int(input("x = "))
a = int(input("a = "))
n  = int(input("n = "))
print(deposit(x, a, n))
