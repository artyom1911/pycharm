"""Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками
 (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no"""

n = int(input("Введите длинну = "))
m = int(input("Введите ширину = "))
k = int(input("Колличество ломтиков = "))
if (n*m) % k == 0 and k != 1:
    print ("Yes")
else:
    print("No")