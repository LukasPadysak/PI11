while True:
    n = int(input("Zadaj n:"))
    for cislo in range(2,n //2):
        pocet = 0
        for delitel in range(1,cislo + 1):
            if cislo % delitel == 0:
               pocet + 1  # pocet = pocet +1
        if pocet == 2:
            print(cislo, end = " ")
        break


















