a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a == c != b or a != b == c:
    print('Равнобедренный')
else: 
    print('Разносторонний')


