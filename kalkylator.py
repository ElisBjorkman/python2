"""
nummer = input()   #Tar emot input från användaren
print("hej") # Skriver ut till terminalen
if 1 == 2 # Genföra 2 saker
int() #för att konvertera en sträng till ett nummer (integer) 
"""




miniräknare = int(input("för addiktion skriv 1 \n för subtraktion skriv 2 \n för multiplikation skriv 3 \n för division skriv 4\n"))

tal1 = int(input())
tal2 = int(input())

if miniräknare == 1:
    print("addiktion")
    
    summa = tal1 + tal2
    print(summa)


if miniräknare == 2:
    print("subtraktion")
   
    summa = tal1 - tal2
    print(summa)


if miniräknare == 3:
    print("multiplikation")
    
    summa = tal1 * tal2
    print(summa)

if miniräknare == 4:
    print("division")
    
    summa = tal1 / tal2
    print(summa)