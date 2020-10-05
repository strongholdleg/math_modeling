print(' Введите коэфиценты:')
a = float(input('a = '))
c = float(input('c = '))
l = float(input('l = '))
D = c**2-4 * a * l;
print(D)
if D > 0:
    x1 = (-c + D**1/2) / (2 * a)
    x2 = (-c - D**1/2) / (2 * a)
    print(x1,x2)
elif D == 0:
    x = -c / (2 * a)
    print(x)
else:
    print('нет корней')    
























































