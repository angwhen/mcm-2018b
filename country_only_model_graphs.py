import pickle
import matplotlib.pyplot as plt


def graph_english_chinese_1950_to_2050(lang_pop_dict):
    english_speakers = lang_pop_dict["English"]
    #add together chinese and mandarin speakers, not sure why the website used both these terms, but ok
    chinese_speakers = [sum(x) for x in zip(lang_pop_dict["Chinese"],lang_pop_dict["Mandarin"])]
    print english_speakers
    print chinese_speakers

    fig, ax = plt.subplots()
    ax.set_title("Chinese and English Speakers")
    ax.plot(xrange(1950,2055,5),english_speakers,"b")
    ax.plot(xrange(1950,2055,5),chinese_speakers,"r")
    ax.set_xlim(1950,2050)
    ax.set_ylabel("Speakers in Thousands")
    ax.set_xlabel("Year")
    plt.show()

def graph_english_spanish_1950_to_2050(lang_pop_dict):
    english_speakers = lang_pop_dict["English"]
    spanish_speakers = lang_pop_dict["Spanish"]

    fig, ax = plt.subplots()
    ax.set_title("Spanish and English Speakers")
    ax.plot(xrange(1950,2055,5),english_speakers,"b")
    ax.plot(xrange(1950,2055,5),spanish_speakers,"g")
    ax.set_xlim(1950,2050)
    ax.set_ylabel("Speakers in Thousands")
    ax.set_xlabel("Year")
    plt.show()
    

# this dict has each key as a language name
# and each value is an array
# with the first index (0) being the population at 1950
# and the last index (20) being the population projected at 2050
lang_pop_dict = pickle.load(open("lang_pop_dict.p","rb"))
print lang_pop_dict.keys()
#graph_english_chinese_1950_to_2050(lang_pop_dict)
graph_english_spanish_1950_to_2050(lang_pop_dict)
