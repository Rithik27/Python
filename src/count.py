a = input("type in a frikin paragraph!")
b = list(a)
c = 0
d = 0
e = 0


def number_count(b, c, d, e):
    for x in b:
        if x.isdigit():
            e = e + 1
        else:
            if x == " ":
                d = d + 1
            else:
                c = c + 1
    print("the number of numbers are ", e)
    print("the number of alphabets are ", c)
    print("the number of spaces are ", d)


number_count(b, c, d, e)
