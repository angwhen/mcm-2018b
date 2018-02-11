from pyexcel_ods import get_data
import re
import pickle

data = get_data("all_speakers.ods")["Sheet1"]
print "loaded"

all_speakers_dict = {} #dict of lists with two indices [l1,l2], in millions
for language in data[1:]:
    language_name = str(language[0].split(" ")[0]).strip()
    l1_speakers = language[1]
    l2_speakers = language[2]
    if l2_speakers == "?":
        l2_speakers = 0
    else:
        l2_speakers = int(l2_speakers)
    all_speakers_dict[language_name] = [l1_speakers,l2_speakers]

print all_speakers_dict
# in millions
pickle.dump(all_speakers_dict,open("all_speakers_dict.p","wb"))
