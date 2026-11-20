num = int(input())
d = num % 10 
c = (num % 100) // 10 
b = (num % 1000) // 100
a = num // 1000
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')
