a = input("type in a frikin paragraph!")
b = list(a)
c = 0
d = 0
e = 0


def rettel_count(b, c, d):
    for x in range(0, len(b)):
        if b[x] != " ":
            c = c + 1
        else:
            d = d + 1
    print("the number of alphabets are ", c)
    print("the number of spaces are ", d)


rettel_count(b, c, d)
