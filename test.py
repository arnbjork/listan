alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

print(alfabet)
nyckel = 1

print = "vad vill du göra"
print="----"*20
print="vill du kryptera något"
if input == "j":
    print="vad vill du kryptera"
    input = "meddelande"
    printOrd = ""
    for bokstav in "meddelande":
        bokstav_position = alfabet.index(bokstav)
        print_Ord += str(alfabet[bokstav_position+nyckel])
    print(print_Ord)

else:
    print = "vill du ut kryptera något"
    if input == "j":
        print = "vad vill du kryptera ut"
        input = "krypterat"
        for nyckel in range(0, len(alfabet)):  
            dekrypterat = ""
            for bokstav in "krypterat":
                dekrypterat += alfabet[alfabet.index(bokstav) - nyckel % 29]
            print (dekrypterat)


















