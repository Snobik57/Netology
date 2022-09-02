# Task 1
from pprint import pprint
from string import punctuation as punc

print('Служба знакомств PY-58.\nПодберем идеальную пару!\n')

while True:
    boys = [i for i in input('Введите имена мальчиков: ').split()]
    girls = [i for i in input('Введите имена девочек: ').split()]
    if len(boys) != len(girls):
        print(' \nКто-то останется без пары! Повторите ввод!')
    else:
        boys.sort()
        girls.sort()
        break

print('\nИдеальные пары: \n')

for boy, girl in zip(boys, girls):
    print(f"""{boy.strip(punc)} и {girl.strip(punc)}""")

print(f" \n{50 * '#'}\n")

# Task 2

person = int(input('Введите количество персон: '))

cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]

for name, dish in cook_book:
    print(f'\n{name.capitalize()}:')
    for reag, mass, meas in dish:
        mass *= person
        if mass >= 1000:
            mass /= 1000
            if meas == 'гр.':
                meas = 'кг.'
            elif meas == 'мл.':
                meas = 'л.'
        else:
            x = ''
        print(f'{reag}, {mass}{meas}')

pprint(cook_book)