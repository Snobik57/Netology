def recurse(arr):
    for item in arr:
        if isinstance(item, list):
            yield from recurse(item)
        else:
            yield item


if __name__ == '__main__':
    pass