class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.count - 1:
            raise StopIteration

        value = self.step * self.counter
        self.counter += 1
        return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

