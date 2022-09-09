from func.iterator import FlatIterator
from func.generator import recurse

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

flat_list = [item for item in FlatIterator(nested_list)]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print("############################################")
    print(flat_list)
    print("############################################")
    for item in recurse(nested_list):
        print(item)
