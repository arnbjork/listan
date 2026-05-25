# en sträng med alla bokstäver i det svenska alfabetet
alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

# meddelandet som ska krypteras
# nyckeln är antalet positioner varje bokstav ska flyttas
nyckel = 1
# variabel för att lagra det krypterade meddelandet
resultat = ""

# UPPDRAG: Skriv en loop som skriver ut "ifk"
# Tips: Använd .index() och []
#
#   morot = "e"
#    gurka = "j"
#    egg_p = alfabet.index(egg) 
#    morot_p = alfabet.index(morot)
#    gurka_p = alfabet.index(gurka)
#    print (egg_plats + nyckel)
#    print (alfabet[egg_p+nyckel], alfabet[morot_p+nyckel], alfabet[gurka_p+nyckel])

print=("vad vill du göra")
print=("----")*20
print="vill du kryptera något"
if input == ("j"):
    print="vad vill du kryptera"
    input = ("meddelande")
    printOrd = ""
    for bokstav in "meddelande":
        #print (bokstav)
        bokstav_position = alfabet.index(bokstav)
        #print(bokstav_position)
        print_Ord += str(alfabet[bokstav_position+nyckel])
    print(print_Ord)
else:
    print = "vill du ut kryptera något"
    if input == ("j"):
        print = "vad vill du kryptera ut"
        input = ("krypterat")
        for nyckel in range(0, len(alfabet)):  
            dekrypterat = ""
            for bokstav in ("krypterat"):
                dekrypterat += alfabet[alfabet.index(bokstav) - nyckel % 29]
            print(dekrypterat)
            # räkna ut ny position
                # skriva ut bokstaven på den nya positionen
        
#frank = "f"
#frank_plats = alfabet.index(frank)
#print (meddelande[frank_plats])
#for:
#    print (meddelande[frank_plats+nyckel])
#att seta in en lop (
# index+1)