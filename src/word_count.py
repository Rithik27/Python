a = input("type in a frikin paragraph!")
b = list(a)


def word_count():
    for x in b:
        z = x.split()
        print(z)


word_count()
