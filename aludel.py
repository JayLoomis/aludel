# I'm going to start by making a basic D&D 5th edition character generator,
# which I'll then expand into fully-fledged classes and whatnot.

stats_def = (('str', 'strength'), ('dex', 'dexterity'), ('con', 'constitution'),
             ('int', 'intelligence'), ('wis', 'wisdom'), ('cha', 'charisma'))

my_stats = {}

for stat_def in stats_def:
    my_stats[stat_def[0]] = {'name': stat_def[1], 'val': 10, 'mod': 0}

print(my_stats['str']['name'])


# def print_stats(stats):
#     for stat in stats:
#         print('{} - {} ({})'.format(stat['name'], stat['val'], stat['mod']))
#
# print_stats(my_stats)

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
        pass

    def get_conditional_values(self):
        pass

    def has_conditional_mods(self):

    def get_ability_mod(self):
        pass

    def set_base_value(self, value, source):
        self.__base = {'value': value, 'source': source}

    def add_modifier(self, value, name, source):
        self.__mods.append({'value': value, 'name': name, 'source': source})

class Abilities:
    def __init__(self, ability_list):
        self.__abilities = []
        for ability in ability_list:
            self.__abilities.append(Ability(ability[0], ability[1]))







