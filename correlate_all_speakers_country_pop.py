import pickle
import matplotlib.pyplot as plt
import numpy as np

all_speakers_dict = pickle.load(open("all_speakers_dict.p","rb"))
lang_pop_dict = pickle.load(open("lang_pop_dict.p","rb"))

l1_speakers_num_dict = {}
l2_speakers_num_dict = {} 
lang_pop_2010_num_dict = {}

country_langs = lang_pop_dict.keys()
# print country_langs
# print all_speakers_dict.keys()

for language in all_speakers_dict.keys(): 
    if language == "Wu" or language == "Yue":
        country_language = "Chinese"
    elif language == "Bengali":
        country_language = "Bangla"
    elif language == "Hindustani":
        country_language = "Hindi"
    elif language not in country_langs:
        print language
        continue
    else:
        country_language = language

    lang_pop_2010_num_dict[country_language] = lang_pop_dict[country_language][12]
    if country_language not in l1_speakers_num_dict:
        l1_speakers_num_dict[country_language] = all_speakers_dict[language][0]*1000
        l2_speakers_num_dict[country_language] = all_speakers_dict[language][1]*1000
    else:
        l1_speakers_num_dict[country_language] += all_speakers_dict[language][0]*1000
        l2_speakers_num_dict[country_language] += all_speakers_dict[language][1]*1000

print l1_speakers_num_dict.keys()

# make lists where each index is a language(no specification which) and the value is thousands of speakers
# chinese and mandarin must be merged because weirdly seperated
l1_speakers_list = []
l2_speakers_list = []
lang_pop_list = []
language_names_list = []
for language in l1_speakers_num_dict.keys():
    if language == "Chinese" or language == "Mandarin":
        continue
    language_names_list.append(language)
    l1_speakers_list.append(l1_speakers_num_dict[language])
    l2_speakers_list.append(l2_speakers_num_dict[language])
    lang_pop_list.append(lang_pop_2010_num_dict[language])

language_names_list.append("Chinese")
l1_speakers_list.append(l1_speakers_num_dict["Chinese"]+l1_speakers_num_dict["Mandarin"])
l2_speakers_list.append(l2_speakers_num_dict["Chinese"]+l2_speakers_num_dict["Mandarin"])
lang_pop_list.append(lang_pop_2010_num_dict["Chinese"]+lang_pop_2010_num_dict["Mandarin"])

# graph bars comparing each language amount by native data and country data
indices = range(0,2*len(lang_pop_list),2)
width = np.min(np.diff(indices))/3.0

fig = plt.figure()
plt.title("Country Interpolated Predictions vs L1/L2 Speakers Data (2010, undated)")
ax = fig.add_subplot(111)
p1 = ax.bar(indices-width,lang_pop_list,width,color='b',label='-Ymin')
p2 = ax.bar(indices,l1_speakers_list,width,color='r',label='Ymax')
p3 = plt.bar(indices, l2_speakers_list, width,
             bottom=l1_speakers_list)

ax.set_xlabel('Language')
plt.legend((p1[0], p2[0],p3[0]), ('Country Interpolation', 'L1 Speakers Data','L2 Speakers Data'))
plt.xticks(indices, language_names_list,rotation=45)
plt.show()

# save dictionary
language_l12_prop_dict = {} #each key is a language, each value is [l1 prop, l2 prop], prop are prop over total
for language in language_names_list:
    language_l12_prop_dict[language] = [float(l1_speakers_num_dict[language])/float(lang_pop_2010_num_dict[language]), float(l2_speakers_num_dict[language])/float(lang_pop_2010_num_dict[language])]

print language_l12_prop_dict
pickle.dump(language_l12_prop_dict,open("language_l12_prop_dict.p","wb"))
