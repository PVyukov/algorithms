from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 250, 0.0, 100)
print(hero_1[3])


class Person:
    def __init__(self, name, race, health, mana, armor):
        self.armor = armor
        self.mana = mana
        self.health = health
        self.name = name
        self.race = race

    def __str__(self):
        return f'name={self.name}'

    def do_it(self):
        print('working')


hero_2 = Person('Aaz', 'Izverg', 250, 0.0, 100)
print(hero_2.mana)
print(hero_2)
hero_2.do_it()


def do_it():
    print('I am working')


PersonNew = namedtuple('PersonNew', 'name, race, health, mana, armor, do_it')
hero_3 = PersonNew('Aaz', 'Izverg', 250, 0.0, 100, do_it)
print(hero_3.mana)
print(hero_3)
hero_3.do_it()

# hero_3.mana = 100
hero_3 = hero_3._replace(mana=100)
print(hero_3)
print(hero_3._fields)
