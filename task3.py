"""Задача 3: Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no"""

g = int(input("Введите номер билета = "))

a = g // 1000
b = g % 1000
d = (a % 10) + (a // 10 % 10) + (a // 100)
f = (b % 10) + (b // 10 % 10) + (b // 100)
if d == f:
    print("Yes")
else:
    print("No")

