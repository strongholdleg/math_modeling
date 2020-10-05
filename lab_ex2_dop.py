q = int(input("q = "))
b = int(input("b = "))
c = int(input("c = "))
 
if q + b <= c or q + c <= b or b + c <= q:
    print ("Треугольника нет")
elif q != b and q != c and b != c:
    print ("Разносторонний")
elif q == b == c:
    print ("Равносторонний")
else:
    print ("Равнобедренный")












































