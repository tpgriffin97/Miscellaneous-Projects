# Filter Function

def add7(x):
    return x + 7


def isodd(x):
    return x % 2 != 0


def isEven(x):
    return x % 2 == 0


def isFish(x):
    return x == 'fish'


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a3 = ['fish', 'dish', 'squish']

b = list(filter(isodd, a))

c = list(filter(isEven, a2))

d = list(map(add7, filter(isodd, a)))

fish = list(filter(isFish, a3))

print(b)
print(c)
print(d)
print(fish)