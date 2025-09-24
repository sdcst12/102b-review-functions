import random


def getRandomXY():
    x1 = random.randint(1, 100)
    y1 = random.randint(1, 100)
    return x1, y1


x,y = getRandomXY()
print(f"x is {x} and y is {y}")


# Note that when you have multiple return values, you can capture them individually as shown above, or you can capture them as a list or tuple as shown here:

listVal = getRandomXY()
print(listVal)
print(f"x is {listVal[0]} and y is {listVal[1]}")
