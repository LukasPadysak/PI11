# while True:
#     cislo = int(input("Zadaj číslo:(pre ukoncenie zadaj nula):"))
#     if cislo == 0:
#         print("Číslo je nula")
#         break
#     else:
#         if cislo % 2 == 0:
#             print("párne")
#         else:
#             print("nepárne")

while True:
    cislo = int(input("Zadaj číslo:"))
    pocet1 = 0
    pocet2 = 2
    print("Delitele:" , end = " ")
    for delitel in range(1,cislo + 1):

        if cislo % delitel == 0:
            print (delitel,end = " ")
            pocet += 1  # pocet = pocet +1
    print()
    print("pocet delitelov je:", pocet)
    if cislo ==0:
        break