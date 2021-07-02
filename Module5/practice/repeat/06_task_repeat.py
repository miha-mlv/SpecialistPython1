def days_in_year(num_year):
    a = num_year % 100
    b = num_year % 4
    if a == 0 or b != 0:
        return "Обычный"
    else:
        return "високосный"



num_year = int(input("num_year = "))
print(days_in_year(num_year))
