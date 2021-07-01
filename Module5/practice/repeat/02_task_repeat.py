def palindrome(number):
    b = ''
    for i in str(number):
        b = i + b
    if int(b) == number:
        return str(number) + " - является"
    else:
        return str(number) + " - не является"

number = int(input('number = '))
print(palindrome(number))
