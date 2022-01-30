#вводим слово для создания шифра
a = list(input())
b = list('abcdefghijklmnopqrstuvwxyz')
while len(a)<len(b):
    a.append(" ")
print(a)

