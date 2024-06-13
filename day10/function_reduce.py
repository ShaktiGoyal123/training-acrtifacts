from functools import reduce

def add(x:int,y:int):
    return x+y

numbers = [10,30,40,60,70]

sumofno = reduce(add,numbers,5)
print(sumofno)

numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), numbers)
