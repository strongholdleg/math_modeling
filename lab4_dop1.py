def my(a, n):
    if n == 0:
        return 1
    d = my(a * a, n // 2)
    if n % 2:
        d *= a
    return d
a = float(input())
n = float(input())
print(my(a, n))




















































