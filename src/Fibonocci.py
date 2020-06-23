a = input("enter a number.")
b = [1, 1]
c = int(a)
for x in range(0, c - 2):
    e = b[-1]
    f = b[-2]
    b.append(e + f)
print(b)
