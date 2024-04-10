
#sifrovanie cezarovou sifrou
ret = input("Zadaj retazec:")
posun = int(input("zadaj posun pre kodovanie:" ))
for i in range(len(ret)):
    # print(ret[i],ord(ret[i]))
    print(f'{ret[i]}:{ord(ret[i])}')
ret_kod = ""
for i in range(len(ret)):
    # print(f'{ret[i]}:{chr(ord(ret[i])+1)}')
    ret_kod += chr(ord(ret[i])+posun )


print(f'Zákodovaný retazec:{ret_kod}')
