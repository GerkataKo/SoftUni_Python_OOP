from itertools import permutations


def possible_permutations(sequence):
    for i in permutations(sequence):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]