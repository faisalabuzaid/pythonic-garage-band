
class Musician:
    """Parent class to all musicians."""

    members = []

    def __init__(self, role, instrument):
        self.role = role
        self.instrument = instrument
        members.append(self)

    def __str__(self):
        return f'I am a {self.role}'


    def __repr__(self):
        return self.role

    def play_solo(self):
        return f'{self.role} is playing solo on the {self.instrument}'


    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass



class Band:

    all = []

    def __init__(self, name, members):
   
        self.name = name
        self.members = members
        all.append(self)


    def play_solos(self):

        solos = ''
        for element in self.members:
            solos += f'{element.play_solo()}\n'
        return solos[:-1]


    def __str__(self):
        return ("We are the " + self.name)

    def __repr__(self):
        return ("This is the " + self.name)

    @classmethod
    def to_list(cls):
        return cls.all

    
