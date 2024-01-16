import random

def spel():
    val = ["sten", "sax", "påse"]
    max_poang = 3

    while True:
        poang_spelare = 0
        poang_dator = 0

        while poang_spelare < max_poang and poang_dator < max_poang:
            dator_val = random.choice(val)

            spelare_val = input("Välj sten, sax eller påse: ").lower()

            print(f"Datorn valde: {dator_val}")

            if spelare_val in val:
                if spelare_val == dator_val:
                    print("Det blev oavgjort!")
                
                
                elif (spelare_val == "sten" and dator_val == "sax") or \
                     (spelare_val == "sax" and dator_val == "påse") or \
                     (spelare_val == "påse" and dator_val == "sten"):
                    print("Du vann!")
                    poang_spelare += 1
                    poang_dator = 0
                else:
                    print("Datorn vann!")
                    poang_dator += 1
                    poang_spelare = 0


            
            
            else:
                print("Ogiltigt val. Välj sten, sax eller påse.")

            print(f"Poäng - Spelare: {poang_spelare}, Dator: {poang_dator}\n")

        
        if poang_spelare == max_poang:
            print("Grattis! Du har vunnit!")
        
        else:
            print("Datorn har vunnit! Bättre lycka till nästa gång.")

        
        nollstall = input("Vill du spela igen? (ja/nej): ").lower()
        if nollstall != 'ja':
            
            break

spel()
