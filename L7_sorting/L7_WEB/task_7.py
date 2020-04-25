from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name}; age={self.age}'


p_1 = Person('Иван', 30)
p_2 = Person('Тариэл', 37)
p_3 = Person('Сергей', 49)
p_4 = Person('Антон', 33)
p_5 = Person('Сергей', 25)

people = [p_1, p_2, p_3, p_4, p_5]
print(people)

a = sorted(people, key=attrgetter('age'))
print(a)
b = sorted(a, key=attrgetter('name'))
print(b)

"""
sorted(people, key=attrgetter('отчество'))
sorted(people, key=attrgetter('имя'))
sorted(people, key=attrgetter('фамилия'))
"""

