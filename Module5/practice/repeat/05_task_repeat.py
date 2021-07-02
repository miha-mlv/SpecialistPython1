def pagination(num_items, items_on_page):
    a = num_items / items_on_page
    b = num_items % items_on_page
    q = num_items // items_on_page
    if b == 0:
        return "На последней странице будет отображено: " + str(items_on_page)
    else:
        c = q * items_on_page
        qw = num_items - c
        return "На последней странице будет отображено: " + str(qw)

num_items = int(input('num_items = '))
items_on_page = int(input("items_on_page = "))
print(pagination(num_items, items_on_page))
