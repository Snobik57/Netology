
class FlatIterator:
    def __init__(self, some_list):
        self.some_list = sum(some_list, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.some_list):
            raise StopIteration
        return self.some_list[self.cursor]


if __name__ == '__main__':
    pass
