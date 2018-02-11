import pickle
import matplotlib.pyplot as plt
import numpy as np

native_speakers_dict = pickle.load(open("native_speakers_dict.p","rb"))
lang_pop_dict = pickle.load(open("lang_pop_dict.p","rb"))

native_speakers_2007_num_dict = {} 
lang_pop_2010_num_dict = {} 

native_speakers_langs = native_speakers_dict.keys()
for language in lang_pop_dict.keys():
    #some of the names are not quite matched, up so manually match them up
    if language == "Chinese":
        native_speaker_language_names = ["Jin","Southern Min", "Eastern Min", "Wu", "Gan Chinese", "Xiang","Yue","Northern Min", "Zhuang"]
    elif language == "Hindi":
        native_speaker_language_names = ["Hindi[a]","Bhojpuri"]
    elif language == "Mongolian":
        native_speaker_language = "Uzbek"
    elif language == "Bulgarian" or language == "Croatian" or language == "Serbian":
        native_speaker_language = "Serbo-Croatian"
    #elif language == "Catalan":
    #    native_speaker_language = "Spanish" #idk
    elif language == "Slovak":
        native_speaker_language = "Czech"
    elif language == "Filipino":
        native_speaker_language = "Hiligaynon/Ilonggo"
    elif language == "Tajik":
        native_speaker_language = "Persian"
    elif language not in native_speakers_langs:
        print "|%s| "%language, #languages that aren't matched
        continue
    else:
        native_speaker_language = language
    if language == "Chinese" or language == "Hindi":
        lang_pop_2010_num_dict[language] = lang_pop_dict[language][12]
        native_speakers_2007_num_dict[language] = 0
        for native_speaker_language in native_speaker_language_names:
            native_speakers_2007_num_dict[language]+=native_speakers_dict[native_speaker_language]
    else:
        lang_pop_2010_num_dict[language] = lang_pop_dict[language][12]
        native_speakers_2007_num_dict[language]=native_speakers_dict[native_speaker_language]

print len(native_speakers_2007_num_dict.keys())
print len(lang_pop_2010_num_dict.keys())

# make lists where each index is a language(no specification which) and the value is thousands of speakers
# chinese and mandarin must be merged because weirdly seperated
native_speakers_list = []
lang_pop_list = []
language_names_list = []
for language in native_speakers_2007_num_dict.keys():
    if language == "Chinese" or language == "Mandarin":
        continue
    language_names_list.append(language)
    native_speakers_list.append(int(native_speakers_2007_num_dict[language]*1000)) #to put in thousands
    lang_pop_list.append(lang_pop_2010_num_dict[language])

language_names_list.append("Chinese")
native_speakers_list.append(int(native_speakers_2007_num_dict["Chinese"]*1000+native_speakers_2007_num_dict["Mandarin"]*1000)) #to put in thousands
lang_pop_list.append(lang_pop_2010_num_dict["Chinese"]+lang_pop_2010_num_dict["Mandarin"])

print lang_pop_list
print native_speakers_list

# graph bars comparing each language amount by native data and country data
indices = range(0,2*len(lang_pop_list),2)
width = np.min(np.diff(indices))/3.0

fig = plt.figure()
plt.title("Country Interpolated Predictions vs Native Speakers Data (2010, 2007)")
ax = fig.add_subplot(111)
p1 = ax.bar(indices-width,lang_pop_list,width,color='b',label='-Ymin')
p2 = ax.bar(indices,native_speakers_list,width,color='r',label='Ymax')
ax.set_xlabel('Language')
plt.legend((p1[0], p2[0]), ('Country Interpolation', 'Native Speakers Data'))
plt.xticks(indices, language_names_list,rotation=45)
plt.show()

# save dict of proportions
print language_names_list
language_native_prop_dict = {}
for i in xrange(0,len(language_names_list)):
    language_native_prop_dict[language_names_list[i]] = float(native_speakers_list[i])/float(lang_pop_list[i])

print language_native_prop_dict
pickle.dump(language_native_prop_dict,open("language_native_prop_dict.p","wb"))



