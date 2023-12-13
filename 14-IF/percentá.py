max_bodov = 30
pocet_bodov = int(input("Zadaj počet bodov:"))
percentá = (pocet_bodov / max_bodov) * 100
print(f"Získal si {round(percentá,  2)}%")
# if percentá >= 90:
#     print("Výborný")
# else:
#     if percentá >=75:
#         print("Chválitebný")
#     else:
#         if percentá >= 50:
#             print("Dobrý")
#         else:
#             if percentá >=30:
#                 print("Dostatočný")
#             else:
#                 print("Nedostatočný")

if percentá >=90:
    print("Výborný , známka 1")
elif 75<= percentá <90:
        print("Chválitebný,známka2")
elif 50<= percentá < 75:
    print("Dobrý,známka 3")
elif 30<= percentá <75:
    print("Dostatočný,známka 4")
else:
    print("Nedostatočný,známka 5")


