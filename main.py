from csv import *


db = {"усиление атаки": 3,
      "регенерация": 5,
     }
#db-словарь, который содержит индекс списка мощности, которую надо прибавить

with open("monster_game.csv", encoding="utf-8") as of:
    rdr = list(reader(of, delimiter='$', quotechar='"'))[1:]
    with open("monster_opportunity.csv", 'w', newline='', encoding="utf-8") as wf:
        wrt = writer(wf, delimiter='$', quotechar='"')
        wrt.writerow(["MonsterName", "opportunity", "power"])
        c = 0
        for el in rdr:
            power = 0#в эту переменную складываются значения мощности
            if el[1] == "дополнительный ход":
                power += sum(int(x) for x in el[3:])
            else:
                power += int(el[db[el[1]]])
            power *= int(el[2]) / 100
            wrt.writerow([el[0], el[1], round(power, 3)])
            if c < 5:
                print(round(power, 3))
                c += 1
