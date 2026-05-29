alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

print(alfabet)

nyckel = 1

print(nyckel)
cesar_chifer=True
while cesar_chifer == True: 
    print("vad vill du göra")
    print("----"*20)
    svar=input("vill du kryptera något j/n ")
    if svar == "j":
        meddelande=input("vad vill du kryptera ")
        printOrd = ""
        for bokstav in meddelande:
            bokstav_position = alfabet.index(bokstav)
            printOrd += str(alfabet[bokstav_position+nyckel])
        print(printOrd)


    vall=input("vill du ut kryptera något j/n ")
    if vall == "j":
        krypterat=input("vad vill du kryptera ut ")
        for nyckel in range(0, len(alfabet)):  
            dekrypterat = ""
            for bokstav in krypterat:
                dekrypterat += alfabet[alfabet.index(bokstav) - nyckel % 29]
            print (dekrypterat)
    avslut=input("vill du ändra något j/n ")
    if avslut == "n":
        cesar_chifer=False

















