# Задание № 1
# ввод имени и вывод его на экран
"""
name = input("введите ваше имя:" )
print("меня зовут ", name)

a = input('твое имя: ')
print("тебя зовут:", a)

# Пользователь вводит числа для сложения и они выводятся на экран
num1 = float(input("numer one: "))
num2 = float(input("numer two: "))
num3 = num1+num2
print("ответ равен:", num3)
"""
""" 
# Задание № тест if/else/elif
a = float(input("введите ваш возраст:" ))
b = 18
if a >= b:
    print("вам можно покупать водку")
else:
    print("вам можно молоко")
a = input("вы любите животных да или нет:" )
b = "да"
if a == b:
    print("хорошо")
elif a != b:
    print ("вы любите собак?")
"""
""" 
# задание № 2
a = float(input("введите время в секундах: "))
b = a / 60  # время в минутах
c = b / 60  # время в часах
c1 = b // 60
c2 = c - c1  # целое количество часов
c3 = c2 * 60 * 60
c4 = c3 // 60  # целое количество минут
c5 = ((c3 / 60) - c4) * 60  # количество секунд
print("%.0f" % (c1),":","%.0f" % (c4),":","%.0f" % (c5))
"""
# задание № 3 сложить числа по формату установленному
""" 
a = int(input("введите число: "))
b = str(a)
c = str(a)

a1 = float(b)
a2 = float(c+c)
a3 = float(c+c+c)
a4 = a3 + a2 + a3
print(a1, "+", a2, "+", a3, "+", a4)
"""
"""  
# задание № 4 в числе найти найти наибльшую цифру и вывести ее, переписал с урока - не работает!!!
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print('ошибка ввода, это не число')

result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
        user_num //= 10

print(result)
"""
""" 
# задача про спортсмена

while True:
    user_a = input('введите целое число результат в первый день\n')
    if user_a.isdigit():
        user_a = int(user_a)
        break
    else:
        print('ошибка ввода, это не число')

while True:
    user_b = input('введите результат последнего дня')
    if user_b.isdigit():
        user_b = int(user_b)
        break
    else:
        print('ошибка ввода')

day = 1
tmp = user_a
while tmp < user_b:
    tmp *= 1.1
    day += 1
print(day)
"""
# финансовые показатели компании: прибыльность.рентабельность, прибыль на одного сотрудника
revenue = float(input('введите значение выручки: '))
expeses = float(input('введите значение затрат: '))
profit = revenue - expeses

print("profit:", profit)
if revenue > expeses:
    print("вы работаете с прибылью")
else:
    print("вы работаете с отрицательной рентабельностью")
a = float(input('введите количество сотрудников: '))
b = profit / a
print('прибыль на одного сотрудника: ', b)











































