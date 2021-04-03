def vowel_filter(func):
    vowels = set('aeiou' + 'aeiou'.upper())

    def wrapper():
        result = func()
        return [c for c in result if c in vowels]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
