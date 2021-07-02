def pagination(num_items, items_on_page):
    a = num_items / items_on_page
    b = num_items % items_on_page
    if b == 0:
        return a
    else:
        c = math.ceil(a)
        return c

num_items = int(input('num_items = '))
items_on_page = int(input("items_on_page = "))
print(pagination(num_items, items_on_page))
