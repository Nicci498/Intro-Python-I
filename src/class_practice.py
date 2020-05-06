class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

sam = Person('just', 'sam')
print(sam)


class Character(Person):
    def __init__(self, first_name, last_name, author, book, home):
        super().__init__(first_name, last_name)
        self.author = author
        self.book = book
        self.home = home
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is a character from {self.home} in {self.book} by {self.author}'
Bode = Character('Bode', 'Cauthorn', 'Robert Jordan', 'Wheel of Time', 'The Two Rivers')
print(Bode)

class Magic_Wielder(Character):
    def __init__(self, first_name, last_name, author, book, home, power):
        super().__init__(first_name, last_name, author, book, home)
        self.power = power
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is a {self.power} from {self.home} in {self.book} by {self.author}'
Nyn = Magic_Wielder('Nynaeve', 'Al Meara', 'Robert Jordan', 'a Wisdom and Aes Sedai', 'The Wheel of Time',  'The Two Rivers')
print(Nyn)

class Radient(Magic_Wielder):
    def __init__(self, first_name, last_name, author, book, home, power, order, spren):
        super().__init__(first_name, last_name, author, book, home, power)
        self.order = order
        self.spren = spren
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is a {self.order} with {self.power} bonded to {self.spren} from {self.home} in {self.book} by {self.author}'
Kal = Radient('Kaladin', 'Stormblessed', 'Brandon Sanderson', 'Stormlight Archives', 'Kholinar', 'flying and surgebinding powers', 'Windrunner', 'Syl')
print(Kal)

class Ruler(Character):
    def __init__(self, first_name, last_name, author, book, home, title):
        super().__init__(first_name, last_name, author, book, home)
        self.title = title
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is a {self.title} from {self.home} in {self.book} by {self.author}'
        
Morgase = Ruler('Morgase', 'Trakand', 'Robert Jordan', 'The Wheel of Time', 'Camelyn', 'Queen of Andor')
print(Morgase)


class Magical_Ruler(Ruler):
    def __init__(self, first_name, last_name, author, book, home, title, power):
        super().__init__(first_name, last_name, author, book, home, title)
        self.power = power
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is a {self.power} from {self.home} in {self.book} by {self.author}'

Egwene = Magical_Ruler('Egwene', 'Al Vere', 'Robert Jordan', 'Wheel of Time', 'channeler of the One Power', 'The Two Rivers', 'Amyriln')
print(Egwene)