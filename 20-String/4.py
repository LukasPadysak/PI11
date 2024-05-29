a = input("Zadaj vetu:")
samohláska = 0
for znak in a:
    if znak in "aeiyou":
        samohláska += 1
print(f'Počet samohlások je {samohláska}')






