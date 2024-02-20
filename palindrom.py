while True:
    ord = input("Testa ord som är en palindrom : ")

#längden som måstes användas för att fortsätas.
    if len(ord) > 1:
        break
    else:
        print("Det är inte tillåtet att bara använda en bokstav")

ord1 = ""

for x in reversed(ord):
    ord1 += x

if ord1.lower() == ord.lower():
    print("Grattis! Det är en palindom")

else:
    print("Tyvär! Det är inte en palindom")

