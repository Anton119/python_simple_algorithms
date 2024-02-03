#1) Треугольник с катетом у полей
for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()    
#2) Треугольник с гипотенузой от полей
for i in range(5):
    print()
    for k in range(4-i):
        print(" ", end=" ")
    for j in range(i):
       print("*", end=" ")
#3) Ёлка
print()
for i in range (5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
################# циклы с while / for 
#1) Треугольник с катетом у полей
j=0
while j < 4:
    j+=1
    print()
    i=0
    while i < j:
        i+=1
        print("* ",end="")        
print()
#2) Треугольник с гипотенузой от полей
j=0 
while j < 4:
    j+=1
    print()
    i=0
    while i < (5-j):
        i+=1
        print(" ",end=" ")
    k=0
    while k < (j):
        k+=1
        print("*",end=" ")
print()
#3) Ёлка
i=0
while i < 4:
    i+=1
    print()
    j=0
    while j < (5-i):
        j+=1
        print(" ",end="")
    k=0
    while k < i:
        k+=1
        print("* ", end="")




    
