import random
print("Skriv en fråga så kommer magic 8 ball ge dig ett svar!")
input()

Ja_lista = ("Ja", "Absolut", "självklart", "Untan Tvekan")

Nej_lista = ("Absolut Inte", "Nej Inte En Chans", "Nej", "Dra Åt HELVETE!!!")

kancke_lista = ("Det Kan Vara Möjligtvis", "OSäker", "Kancke")


result = random.randint(1, 3)

if result == 1:
    print(random.choice(Ja_lista))

elif result == 2:
    print(random.choice(kancke_lista))

else:
    print(random.choice(Nej_lista))



