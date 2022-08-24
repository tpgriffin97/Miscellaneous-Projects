# Lambda Function

def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 95


func3 = lambda x, y: x + y
print(func3(98, 2))

print(func(5))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x + 20, a))
print(newList)

newList2 = list(filter(lambda x: x % 2 == 0, a))
print(newList2)
