#Task 1
print('Task #1\n')

geo_logs = [{
    'visit1': ['Москва', 'Россия']
}, {
    'visit2': ['Дели', 'Индия']
}, {
    'visit3': ['Владимир', 'Россия']
}, {
    'visit4': ['Лиссабон', 'Португалия']
}, {
    'visit5': ['Париж', 'Франция']
}, {
    'visit6': ['Лиссабон', 'Португалия']
}, {
    'visit7': ['Тула', 'Россия']
}, {
    'visit8': ['Тула', 'Россия']
}, {
    'visit9': ['Курск', 'Россия']
}, {
    'visit10': ['Архангельск', 'Россия']
}]

for logs in reversed(geo_logs):
    for keys, values in logs.items():
        if values[1] != 'Россия':
            geo_logs.remove(logs)

print("\n".join(map(str, geo_logs)))

# Task 2
print('\nTask #2\n')

ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

print(f'{set(sum(ids.values(), []))}\n')

# Task 3
print("Task #3\n")
queries = [
    'одно', 'второе', 'смотреть сериалы онлайн', 'новости спорта',
    'афиша кино', 'курс доллара', 'сериалы этим летом', 'курс по питону',
    'сериалы про спорт'
]

total_request_quantity = len(queries)  # общее кол-во запросов

dct = {}  # Временный словарь куда пишем статистику своеобразная база данных

for query in queries:
    count = len(query.split())
    dct[count] = dct.get(count, 0) + 1

# Для каждого элемента словаря, т.е. для каждого кол-ва слов расчитываем процент и выводим на печать
for key in dct:
    percent_of_queries = round(dct[key] / total_request_quantity * 100)
    print(f'Кол-во слов в запросе {key}  - {percent_of_queries}')

#Task 4
print('\nTask #4\n')

stats = {
    'facebook': 55,
    'yandex': 120,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98
}

max_value = max(stats.values())

max_stats = {
    key.capitalize(): value
    for key, value in stats.items() if value == max_value
}

if len(max_stats) == 1:
    print(f'Максимальный объем продаж в слудющем канале: {"".join(max_stats.keys())}')
else:
    print(f'Максимальный объем продаж в слудющих каналах: {", ".join(max_stats.keys())}')

#Task 5
print('\nTask #5\n')

task_list = ['2018-01-01', 'yandex', 'cpc', 100]

result = task_list[-1]
del task_list[-1]
emp_dict = {}

for i in reversed(task_list):
    emp_dict.setdefault(i, result)
    result = emp_dict
    emp_dict = {}

print(result)
