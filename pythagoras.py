
print("skriv för A^2+B^2=C^2")


print("Tall för A^2")
A = int(input())
summa = A**2


print("Tall för B^2")
B = int(input())
summa += B**2


print("Summa för C^2 är A^2+B^2")
C = int(input())

if summa == C**2:
    print("Det stämmer!")


    print("Talet är!", C**2)


else:
    print("Det stämmer inte!")



