b = 0
s = input()
lists = s.split(' ')
for a in lists:
    if int(a) >= 0:
        b = b + int(a)
    else:
        continue
print(b)
