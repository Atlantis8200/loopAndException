'''
Циклы - набор повторяющихся действий
while - условие:
    действие1

for x in range (0,10,1):
    action1
'''
#1 - start
#6 - end - not included
#1 - step
for x in range(1, 6, 1):
    print(f"x= {x}")

print()



#цикл со счетчиком. Переменная number1 показывает сколько раз выполнится цикл
number1 = 1
while number1 <= 5:
    print(f"{number1}")
    number1 = number1 + 1



'''
+ Исключения -try... except убирает критическую ошибку
'''
try:
    num3 = float(input("enter 1 number : "))
    num4 = int(input("enter 2 number : "))
    print(num3+num4)
except ValueError:
#except  ZeroDivisionError: #отлавливает определенное исключение
#except: #отлавливает все исключения
    print("enter integer(int) number")

try:
    num1 = 5
    num2 = 0
    print(num1/num2)
except:
    print("change the second value")
