from csv import *

#db-словарь, в котором хранятся индексы мощностей, которые будут умножаться
db = {"усиление атаки": 3,
      "регенерация": 5,
      "дополнительный ход": 6
     }
with open("monster_game.csv", encoding="utf-8") as of:
    rdr = list(reader(of, delimiter='$', quotechar='"'))[1:]
    rew = []#rew-список в который складываются имена монстров с опытом за их убийство
    c = 0
    for el in rdr:
        exp = int(el[db[el[1]]]) * 1.5
        exp += sum(int(x) for x in el[3:] if x != el[db[el[1]]])
        rew.append([el[0], exp])
        if c < 10:
            print(rew[-1])
            c += 1

with open("4rew.txt", 'w') as wf:
    wf.write(str(rew))
