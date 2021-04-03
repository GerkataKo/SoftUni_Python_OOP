def reverse_text(text):
    for i in range(len(text) - 1, -1, -1):
        yield text[i]


for char in reverse_text('step'):
    print(char, end='')
print()