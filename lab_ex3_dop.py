x1 = int(input('Целое число'))
x2 = 0
while x1 > 0:
    x3 = x1%10
    x1 = x1//10
    x2 = x2*10
    x2 = x2 + x3
print('обратное число:', x2)