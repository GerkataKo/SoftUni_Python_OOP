from collections import deque


class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj=dict_obj
        self.keys=deque(self.dict_obj.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys:
            key = self.keys.popleft()
            value = self.dict_obj[key]
            return key, value
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
