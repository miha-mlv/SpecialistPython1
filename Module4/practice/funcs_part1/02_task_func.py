def palindrome(number):
    b = ''
    for i in str(number):
        b = i + b
    if int(b) == number:
        return str(number) + " - является"
    else:
        return str(number) + " - не является"




# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
