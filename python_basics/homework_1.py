l_square = float(input('Введите длину стороны квадрата: '))

print()

p_square = l_square * 4
s_square = l_square ** 2
print('Периметр: ', p_square)
print('Площадь: ', s_square)

print()

l_rectangle = float(input('Введите длину прямоугольника: '))
w_rectangle = float(input('Введите ширину прямоугольника: '))

print()

p_rectangle = 2 * (l_rectangle + w_rectangle)
s_rectangle = l_rectangle * w_rectangle
print('Периметр: ', p_rectangle)
print('Площадь ', s_rectangle)

print()
token = input()
print()
print(token * int((p_square + s_rectangle)))
print()

pay = float(input('Введите заработную плату в месяц: '))
mortgage = float(input('Введите, какой процент(%) уходит на ипотеку: '))
life = float(input('Введите, какой процент(%) уходит на жизнь: '))

print()

y_pay = pay * 12
p_mortgage = mortgage / 100
p_life = life / 100

exp_life = y_pay * p_life
exp_mortgage = y_pay * p_mortgage

deposit = y_pay - (exp_life + exp_mortgage)

print(f'На ипотеку было потрачено: {exp_mortgage} рублей')
print(f'Было накоплено: {deposit} рублей')