f = input('f=')
f = int(f)
d = input('d=')
d = int(d)
F = input('F=')
F = int(F)
if F < d < 2*F:
    print('зображение действительное, перевернутое, увеличенное')
else: 
    if d<F:
        print('изображение мнимое, прямое, увеличенное, находится с той же стороны от линзы, что и сам предмет, но дальше предмета')
    else: 
            if d>2*F:
                print(' изображение действительное, перевернутое, уменьшенное')























