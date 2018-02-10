from pyexcel_ods import get_data
import re
import pickle

data = get_data("native_speakers.ods")["Sheet1"]

native_speakers_dict = {}
for language in data[1:]:
    language_name = str(language[1].split("(")[0]).strip()
    number_speakers = float(str(language[2]).split("(")[0].split("[")[0])
    native_speakers_dict[language_name] = number_speakers

print native_speakers_dict
# in millions
pickle.dump(native_speakers_dict,open("native_speakers_dict.p","wb"))
