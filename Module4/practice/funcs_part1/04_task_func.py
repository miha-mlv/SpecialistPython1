def can_triangle(p1, p2, p3):
    a = math.sqrt(((p2[0] - p1[0]) ** 2) + (p2[1] - p1[1]) ** 2)
    b = math.sqrt(((p3[0] - p1[0]) ** 2) + (p3[1] - p1[1]) ** 2)
    c = math.sqrt(((p3[0] - p2[0]) ** 2) + (p3[1] - p2[1]) ** 2)

    if a + b > c or a + c > b or c + b > a:
        return "Можно"
    else:
        return "Нельзя"

# Пример вызова функции
print(can_triangle((10, 10), (10, 10), (10, 10)))
