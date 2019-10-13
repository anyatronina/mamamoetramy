import random


class War():
    health = random.randint(100, 150)
    attack = random.randint(20, 30)
    name = ''

    def __init__(self, name):
        self.name = name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def damage(self, x):
        self.health -= x
        if self.health > 0:
            print(self.name, 'получил', x, 'урона. Осталось ', self.health, 'здоровья')
        else:
            print(self.name, 'получил', x, 'урона и погиб.')


class WarShield(War):
    defence = random.randint(5, 10)

    def damage(self, x):
        self.health -= x - self.defence
        if self.health > 0:
            print(self.name, 'получил', x - self.defence, 'урона. Осталось ', self.health, 'здоровья')
        else:
            print(self.name, 'получил', x - self.defence, 'урона и погиб.')


class WarBerserk(War):
    def getAttack(self):
        return random.choice([self.attack, self.attack, self.attack, self.attack, 2*self.attack])


'''war1 = War('war1')
print(war1.name)
print(war1.getAttack())

war2 = WarShield('war2')
print(war2.name)
print(war2.getAttack())

war3 = WarBerserk('war3')
print(war3.name)
print(war3.getAttack())

print(war1.health, '', war3.health)'''


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


#fight(war3, war1)


