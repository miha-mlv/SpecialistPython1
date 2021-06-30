item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12
a = float(item["price"])
a1 = dollar_rate * a
b = int(item["count"])
c = a1 * b
print(c)
