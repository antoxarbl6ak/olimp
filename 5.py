from csv import *

ht = {}#ht-хэш таблица в виде словаряю имя монстра-ключ, атака- значение
with open("monster_game.csv", encoding="utf-8") as of:
    rdr = list(reader(of, delimiter='$', quotechar='"'))[1:]
    for el in rdr:
        ht[el[0]] = ht.get(el[0], 0) + int(el[3])

c = 0
with open("5ht.txt", 'w') as wf:
    for k in ht:
        if c < 10:
            print(k, ht[k])
            c += 1
            wf.write(f"{k}, {ht[k]}\n")