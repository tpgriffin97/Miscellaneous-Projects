# Map Function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x ** x


newList = []
for x in li:
    newList.append(func(x))
print('First technique: ', newList)

print('Map() technique ', list(map(func, li)))

print('List comprehension,', [func(x) for x in li if x%2==0])