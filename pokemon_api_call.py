# create pokedex dictionary

import requests
import requests_cache

requests_cache.install_cache('demo_cache')
#dewott = requests.get("https://pokeapi.co/api/v2/pokemon/502/")
#print(dewott.json())

# log response.from_cache
# https://stackoverflow.com/questions/47665450/is-there-a-way-i-can-log-when-python-requests-cache-hits-the-cache

# requests_cache works, and the response is being cached
# print(dewott.from_cache)
# print(dewott.from_cache)

# make sure that the request is not cached on the first call, then it is cached for all subsequent calls
oshawott = requests.get("https://pokeapi.co/api/v2/pokemon/501/")
#print(oshawott.json())

# first run - false, false
# second run - true, true
print(oshawott.from_cache)
# print(oshawott.from_cache)

# first, test to make sure requests.get will work with pokemon name, not just number
turtwig = requests.get("https://pokeapi.co/api/v2/pokemon/turtwig/") # it works

print(turtwig.from_cache)

turtwig_json = turtwig.json()
#print(turtwig)

# print(turtwig.from_cache) # first true, then false

# import json to parse it into easily understood python data structures

import json

#print(torterra_json['moves'])
turtwig_moves = turtwig_json['moves']
print(turtwig_moves)
print(len(turtwig_moves)) # 69 - goes through 0 to 68

def print_move_dict(moves, genInput='ultra-sun-ultra-moon'): # default most recent
    # the first gen the pokemon appears in is the first version group
    # turtwig - dp, pt, hg/ss, bw, b2w2, ...
    # to find which learnset, we need to change the version group
    # the key is the second numerical index

    # find a way to ask what generation is desired
    # convert that into a number
    # and then put it into json
    #

    learnset_dict = {}
    learnset_list = []
    length_of_moves_json = len(moves)

    # ask which generation
    # some pokemon have different learnsets in the same generation (e.g. riolu in bw/b2w2)
    # for html, use radio buttons, & for android, use touch screen
    # python test can use text input - for the sake of exploration, use foolproof input, then figure out error checking

    """
    1 - red-blue
    1 - yellow
    2 - gold-silver
    2 - crystal
    3 - ruby-sapphire
    3 - emerald
    4 - diamond-pearl
    4 - platinum
    4 - heartgold-soulsilver
    5 - black-white
    5 - black-2-white-2
    6 - x-y
    6 - omega-ruby-alpha-sapphire
    7 - sun-moon
    7 - ultra-sun-ultra-moon
    """

    all_generations = ['red-blue', 'yellow', 'gold-silver', 'crystal', 'ruby-sapphire',
                       'emerald', 'diamond-pearl', 'platinum', 'heartgold-soulsilver',
                       'black-white', 'black-2-white-2', 'x-y', 'omega-ruby-alpha-sapphire',
                       'sun-moon', 'ultra-sun-ultra-moon']

    #if genInput ==

    for i in range(0, length_of_moves_json):
        len_group = len(moves[i]['version_group_details'])
        for j in range(0, len_group):

            move_learn_method = moves[i]['version_group_details'][j]['move_learn_method']['name']
            move_name = moves[i]['move']['name']
            level_learned = moves[i]['version_group_details'][j]['level_learned_at']
            gen_json = moves[i]['version_group_details'][j]['version_group']['name']

        if move_learn_method == "level-up":
            learnset_dict[move_name] = [level_learned, gen_json]
            learnset_list.append(learnset_dict)
            #learnset_dict[move_name] = level_learned

    import operator

    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    #learnset_dict = dict(sorted(learnset_dict.items(), key=lambda item: item[1][0]))
    learnset_dict = dict(sorted(learnset_dict.items(), key=lambda item: item[1]))
    print("gen: ", gen_json, end=' ')
    #print(learnset_list)

    #learnset_list = sorted(learnset_list, key=lambda x: x[0][level_learned])
    #learnset_list.sort(key=operator.itemgetter(level_learned))
    print(learnset_list)

    #print(learnset_dict)


for i in range(0, 69):
    print(turtwig_moves[i]['move']['name'], turtwig_moves[i]['version_group_details'][0]['move_learn_method']['name'])

print('\n')

turtwig_learnset_dict = {}
for i in range(0, len(turtwig_moves)):
    turtwig_move_obtain_method = turtwig_moves[i]['version_group_details'][0]['move_learn_method']['name']
    turtwig_move_name = turtwig_moves[i]['move']['name']
    turtwig_level_learned_at = turtwig_moves[i]['version_group_details'][0]['level_learned_at']

    if turtwig_move_obtain_method == "level-up":
        turtwig_learnset_dict[turtwig_move_name] = turtwig_level_learned_at
        print(turtwig_move_name, turtwig_level_learned_at)

#print(turtwig_learnset_dict)
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
turtwig_learnset_dict = dict(sorted(turtwig_learnset_dict.items(), key=lambda item: item[1]))
print(turtwig_learnset_dict)

# turtwig's learnset happens to be the same across gen iv, v, vi, vii
# try a pokemon that definitely differs, like riolu

#turtwig = requests.get("https://pokeapi.co/api/v2/pokemon/turtwig/") # it works
riolu = requests.get("https://pokeapi.co/api/v2/pokemon/riolu/")

riolu_json = riolu.json()
riolu_moves = riolu_json['moves']
print('\n')
#print(riolu_moves)

print_move_dict(turtwig_moves) # first gen turtwig appears in, gen 4
print_move_dict(riolu_moves) # this will give you the first gen riolu appears in, gen 4

oshawott_moves = oshawott.json()['moves']
print_move_dict(oshawott_moves) # gen 5, oshawott premieres in gen 4

# start exploring versionGroupDetails
# end goal is to access any pokemon learnset in any valid generation

# all gen's are x-y - what about anything post x-y?

# gen 7
litten = requests.get("https://pokeapi.co/api/v2/pokemon/litten/") # usum
print(litten.from_cache)
litten_moves = litten.json()['moves']

print_move_dict(litten_moves)

# into method, also provide what gen should be queried
# gen 1
charmander = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
print(charmander.from_cache)

charmander_moves = charmander.json()['moves']
print(charmander_moves)

print_move_dict(charmander_moves)

# examine pokemon natures

docile_nature = requests.get("https://pokeapi.co/api/v2/nature/docile")
print(docile_nature.from_cache)

docile_nature_json = docile_nature.json()
print(docile_nature_json)

print(docile_nature_json['names'][5]['name']) # if last index, accesses english name

"""
print(lonely_nature_json['increased_stat']['name'])
print(lonely_nature_json['pokeathlon_stat_changes'][0]['max_change'])

print(lonely_nature_json['pokeathlon_stat_changes'][0]['pokeathlon_stat']['name'])
"""

# no need for error checking - just for exploration

def get_pokemon_nature_details(nature_to_concat):
    nature_to_concat = nature_to_concat.lower()

    poke_nature = requests.get("https://pokeapi.co/api/v2/nature/" + nature_to_concat)
    print('cache:', poke_nature.from_cache)
    nature_json = poke_nature.json()

    #for i in range(len())
    nature_name = nature_json['names'][6]['name']

    # take care of natures that are neutral (e.g. docile)
    if not nature_json['increased_stat'] and not nature_json['decreased_stat']:
        plus_stat = None
        minus_stat = None
    else:
    # from nature, find the +10% stat, -10% stat, pokeathlon details
        plus_stat = nature_json['increased_stat']['name']
        minus_stat = nature_json['decreased_stat']['name']

    pokeathlon_plus = nature_json['pokeathlon_stat_changes'][0]
    pokeathlon_minus = nature_json['pokeathlon_stat_changes'][1]

    pokeathlon_plus_tuple = (pokeathlon_plus['max_change'], pokeathlon_plus['pokeathlon_stat']['name'])
    pokeathlon_minus_tuple = (pokeathlon_minus['max_change'], pokeathlon_minus['pokeathlon_stat']['name'])

    # if neutral nature, just print out pokeathlon
    # else, also print out stat changes

    print('\n')
    print(nature_name)
    if not nature_json['increased_stat'] and not nature_json['decreased_stat']:
        print(pokeathlon_plus_tuple)
        print(pokeathlon_minus_tuple)
    else:
        print(plus_stat, pokeathlon_plus_tuple)
        print(minus_stat, pokeathlon_minus_tuple)
    print('\n')

get_pokemon_nature_details("lonely")
get_pokemon_nature_details("adamant")
get_pokemon_nature_details("hasty")
get_pokemon_nature_details("docile")
