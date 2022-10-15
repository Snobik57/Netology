from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        try:
            old_element = self.stack[-1]
            self.stack.pop()
            return old_element
        except IndexError:
            return f'IndexError: pop from empty Stack'

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return f'IndexError: peek from empty Stack'

    def size(self):
        return len(self.stack)


if __name__ == "__main__":

    stack = Stack()

    print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
