def gen_list(size, of, to):
    k = 0
    ls = []
    while True:
        a = random.randint(of, to)
        ls.append(a)
        k += 1
        if k == size:
            return ls
        else:
            continue

siz = int(input("size = "))
o = int(input("of = "))
t = int(input("to = "))
print(gen_list(siz, o, t))
