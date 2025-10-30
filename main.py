#Вложенный цикл
for i in range(0,3,1): #i=0 0<3-- true; i=0+1 1<3--true; i=1+1 2<3--true; i=2+1 3<3--false;
    for j in range(0, 5, 1): #j=0 0<5 --true; j=0+1 1<5--true; j=1+1=2 2<5--true;
                             #2+1=3 3<5--true; j=3+1=4 4<5 --true; j4+1 5<5 -- false
        print("*", end="")
    print("\n")

# *****
#
# *****
#
# *****
#
'''
Методы строк
ФУнкции и методы
'''
#Индексы 0-14
lake = "Синявское озеро"
print(lake.count("о", 0, len(lake)))   #end = 14+1
print()


'''
FOR -
Пока i в диапазоне от  0 и выполняется условие что i<10,
то по умолчанию  шаг 1.
    1/ for i in range(0,10)

Пока i в диапазоне от  0 и выполняется условие что i<10,
шаг указан 3й цифрой
    2/ for i in range(0,10,1) start = 0, end = 9, step= 1

for each - читается, пока i не дошел до конца переменнолй строки line,
то есть в И будет присваиваться каждая буква из слова hello по очереди
       line = "hello"
    3/ for i in line:
'''
for i in range(0,10,2):  #2+2  2*2 2**2 = 4  4+2=6 6+2=8
    print(i)
print()
for i in range(1,9+1,2):  #1 3 5 7 9
    print(i)
print()

for i in range(5,1-1,-1): #5 4 3 2 1
    print(i, end ="")
print()

#for со счетчиком
for i in range(0,5,1):
    print(f"Цикл отработал {i+1}")
print()

count = 0
for i in range(5,0,-1):
    count += 1
    print(f"Цикл отработал {count}")

for i in range(11, 15, 2): # i=11 11<15;  11+2=13 13<15; 13+2=15 15<15 false
    print(i) #11 13

line = "баня в ёлках"
for i in line:
    print(i, end="")
print()
for i in line:
    if i!='а':
        print(i, end="")
print()
for i in line:
    if i!=' ':
        print(i, end="")
print()


