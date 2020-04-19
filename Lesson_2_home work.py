# задание № 1
"""

a = ('a', 5, 7, 'f', 'b')

b = 0
while b < len(a):
    print(type(a[b]))
    b += 1
"""
""" 
# task 2 обмен значений соседних элементов

print('введите список: ')
a = list(input())

j = 0
for i in range(int(len(a) / 2)):
    a[j], a[j + 1] = a[j + 1], a[j]
    j += 2

print(a)
"""

""" 
# Task 3 месяц в виде числа, вывести сезон
seasons_list = ('winter',
                'spring',
                'summer',
                'fall',
                )
seasons_dict = {'winter': (12, 1, 2),
                'spring': (3, 4, 5),
                'summer': (6, 7, 8),
                'fall': (9, 10, 11),
                }

user_month_num = int(input('input month: '))

seasons_idx = user_month_num // 3 % 4

for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break

print(seasons_idx)
print(seasons_list[seasons_idx])

"""
""" 
 # Task 4
user_words = input()

for idx, word in enumerate(user_words.split(' ')):
    print(f'{idx}:{word[:10]}')
"""

# Task 5 реализовать рейтинг

a = [3, 5, 7, 2]
new_a = []
print(a)


b = int(input('введите свой рейтинг: '))
set

# for b in a:

idx = a.index(b)
print(idx)


a.insert(idx + 1, b)


print(a)




