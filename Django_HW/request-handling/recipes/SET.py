
children = int(input())
salary = input()
insurance = input()

base_rate = 10

if children >= 3:
    base_rate = base_rate - 1
else:
    base_rate = 10
if salary == 'да':
    base_rate = base_rate - 0.5
else:
    pass
if insurance == 'да':
    base_rate = base_rate - 1.5
else:
    pass

print('Ваша процентная ставка', base_rate, '%')
