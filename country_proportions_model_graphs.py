import pickle
import matplotlib.pyplot as plt


def graph_english_chinese_1950_to_2050(lang_pop_dict,title):
    english_speakers = lang_pop_dict["English"]
    chinese_speakers = lang_pop_dict["Chinese"]

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.plot(xrange(1950,2055,5),english_speakers,"b")
    ax.plot(xrange(1950,2055,5),chinese_speakers,"r")
    ax.set_xlim(1950,2050)
    ax.set_ylabel("Speakers in Thousands")
    ax.set_xlabel("Year")
    plt.show()

# this dict has each key as a language name
# and each value is an array
# with the first index (0) being the population at 1950
# and the last index (20) being the population projected at 2050
lang_pop_dict = pickle.load(open("lang_pop_dict.p","rb"))
# combing lang_pop_dict chinese and mandarin, from now on ONLY going to use Chinese designation
lang_pop_dict["Chinese"] = [e1+e2 for e1,e2 in zip(lang_pop_dict["Chinese"],lang_pop_dict["Mandarin"])] 
language_l12_prop_dict = pickle.load(open("language_l12_prop_dict.p","rb"))

print language_l12_prop_dict.keys()

l1_lang_pop_dict = {}
l2_lang_pop_dict = {}
for language in language_l12_prop_dict.keys():
    
    l1_prop_arr = [language_l12_prop_dict[language][0]*float(el) for el in lang_pop_dict[language]]
    l2_prop_arr = [language_l12_prop_dict[language][1]*float(el) for el in lang_pop_dict[language]]
    l1_lang_pop_dict[language] = l1_prop_arr
    l2_lang_pop_dict[language] = l2_prop_arr


graph_english_chinese_1950_to_2050(l1_lang_pop_dict,"English Chinese L1 Speakers")
#graph_english_spanish_1950_to_2050(lang_pop_dict)
