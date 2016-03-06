# I'm going to start by making a basic D&D 5th edition character generator,
# which I'll then expand into fully-fledged classes and whatnot.


standard_ability_list = [('strength', 'str'), ('dexterity', 'dex'),
                         ('constitution', 'con'), ('intelligence', 'int'),
                         ('wisdom', 'wis'), ('charisma', 'cha')]


class Ability:
    def __init__(self, ability_name, short_name):
        self.__name = ability_name
        self.__short_name = short_name
        self.__base = None
        self.__mods = []

    def get_regular_value(self):
        reg_val = self.__base

        for mod in self.__mods:
            if mod['type'] != 'conditional':
                reg_val += mod['value']

        return reg_val

    def get_conditional_values(self):
        pass

    def has_conditional_mods(self):
        for mod in self.__mods:
            if mod['type'] == 'conditional':
                return True

        return False

    @property
    def get_ability_mod(self):

        # Can use instead of the big block:
        return (self.get_regular_value() - 10) // 2

    def set_base_value(self, value, source):
        self.__base = {'value': value, 'source': source}

    def add_modifier(self, value, name, source):
        self.__mods.append({'value': value, 'name': name, 'source': source})


class Abilities:
    def __init__(self, ability_list):
        self.__abilities = []
        for ability in ability_list:
            self.__abilities.append(Ability(ability[0], ability[1]))







