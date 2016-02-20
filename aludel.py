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
