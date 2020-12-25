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
print(len(turtwig_moves)) # 69

def print_move_dict(moves):
    learnset_dict = {}
    length_of_moves_json = len(moves)

    for i in range(0, length_of_moves_json):
        if moves[i]['version_group_details'][0]['move_learn_method']['name'] == "level-up":
            learnset_dict[moves[i]['move']['name']] = moves[i]['version_group_details'][0]['level_learned_at']

    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    learnset_dict = dict(sorted(learnset_dict.items(), key=lambda item: item[1]))
    print(learnset_dict)


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

