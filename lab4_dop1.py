def my(a, n):
    if n == 0:
        return 1
    res = my(a * a, n // 2)
    if n % 2:
        res *= a
    return res
 
a = float(input())
n = float(input())
print(my(a, n))




















































