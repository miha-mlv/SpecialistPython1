def average(*args):
    a = 0
    k = 0
    for i in args:
        k = i + k
        a += 1
    q = k / a
    return q




print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
