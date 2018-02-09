import pickle

# this dict has each key as a language name
# and each value is an array
# with the first index (0) being the population at 1950
# and the last index (20) being the population projected at 2050
lang_pop_dict = pickle.load(open("lang_pop_dict.p","rb"))


