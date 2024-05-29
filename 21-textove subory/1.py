fmena = open('mena.txt','r',encoding='utf-8') #otvori subor mena.txt na citanie , w je na zapis,encoding je kodovanie 
# fmena = open('C:/dokumenty/mena.txt','r') absolutna cesta k suboru

while True:
    riadok = fmena.readline()
    if riadok == '':
        break

    print(riadok[:-1])  # vypise vsetky znaky od nulteho po predposledny





fmena.close()   # zatvorenie suboru, vzdy treba !!!!