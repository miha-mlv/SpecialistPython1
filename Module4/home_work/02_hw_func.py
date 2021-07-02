def dis(x1, y1, x2, y2, x3, y3):
    a = math.sqrt(((y1 - y2) ** 2) + (x1 - x2) ** 2)
    b = math.sqrt(((y1 - y3) ** 2) + (x1 - x3) ** 2)
    c = math.sqrt(((y2 - y3) ** 2) + (x2 - x3) ** 2)
    if a > c and c > b:
        q = 'BC'
        return q
    elif c > a and a > b:
        q = "AB"
        return q
    else:
        q = "AC"
        return q


x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

x3 = int(input("x3 = "))
y3 = int(input("y3 = "))

print("Самый короткий отрезок:", dis(x1, y1, x2, y2, x3, y3))
