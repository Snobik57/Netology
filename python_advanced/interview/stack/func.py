from class_stack import Stack


def func(some_string: str) -> str:
    opened_bkt = ['(', '[', '{']
    closed_bkt = [')', ']', '}']

    stack = Stack()

    for i in some_string:

        if i not in opened_bkt and i not in closed_bkt:
            return 'Неверный ввод'
        elif len(string) % 2 != 0:
            return 'Несбалансированно'
        elif string[0] in closed_bkt:
            return 'Несбалансированно'

        if i in opened_bkt:
            stack.push(i)

        if i in closed_bkt:
            result = stack.peek() + i

            if result == '()' or result == '[]' or result == '{}':
                stack.pop()

    if stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == "__main__":
    string = input('Введите скобочную последовательность: ')
    print(func(string))
