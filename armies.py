from game import War, WarShield, WarBerserk
from random import choice


def fight(w1, w2):  # бой между двумя воинами
    a = True
    i = 1
    while a:
        if i%2 == 1:
            w2.damage(w1.getAttack())
            if w2.getHealth() <= 0:
                a = False
                print('Победил ', w1.name)
        else:
            w1.damage(w2.getAttack())
            if w1.getHealth() <= 0:
                a = False
                print('Победил ', w2.name)
        i += 1


warrior1 = War('warrior1')
warrior2 = War('warrior2')
warrior3 = War('warrior3')
warrior4 = War('warrior4')
warrior5 = WarShield('warrior5')
warrior6 = WarShield('warrior6')
warrior7 = WarShield('warrior7')
warrior8 = WarShield('warrior8')
warrior9 = WarBerserk('warrior9')
warrior10 = WarBerserk('warrior10')

army1 = [warrior1, warrior2, warrior3, warrior4, warrior5, warrior6, warrior7, warrior8, warrior9, warrior10]

warrior11 = War('warrior11')
warrior12 = War('warrior12')
warrior13 = War('warrior13')
warrior14 = War('warrior14')
warrior15 = WarShield('warrior15')
warrior16 = WarShield('warrior16')
warrior17 = WarShield('warrior17')
warrior18 = WarShield('warrior18')
warrior19 = WarBerserk('warrior19')
warrior20 = WarBerserk('warrior20')

army2 = [warrior11, warrior12, warrior13, warrior14, warrior15, warrior16, warrior17, warrior18, warrior19, warrior20]

i = 1
while army1 != [] and army2 != []:
    war1 = choice(army1)
    war2 = choice(army2)
    if i%2 == 1:
        fight(war1, war2)
    else:
        fight(war2, war1)
    if war1.health <= 0:
        army1.remove(war1)
    elif war2.health <= 0:
        army2.remove(war2)
    i += 1

if not army1:
    print('Выиграла армия 2.')
else:
    print('Выиграла армия 1.')

