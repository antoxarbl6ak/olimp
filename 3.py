from csv import *

with open("monster_game.csv", encoding="utf-8") as of:
    rdr = list(reader(of, delimiter='$', quotechar='"'))[1:]
    inp = input()
    while inp != "мир":
        for el in rdr:
            if el[0] == inp:
                print(f"{el[0]}: {el[3]}, {el[4]}, {el[5]}, {el[6]}")
                break
        else:
            print("Ого, вам попался новый монстр! БЕГИТЕ!")
        inp = input()
