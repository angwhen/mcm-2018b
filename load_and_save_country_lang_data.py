from pyexcel_ods import get_data
import re
import pickle

data = get_data("country_languages.ods")["Sheet1"]

country_lang_dict = {}
for country in data:
    country_name = str(country[0]).strip()
    main_language = re.split('[^a-zA-Z]',country[1].encode('ascii','ignore'))[0].strip()
    #print main_language
    if country_name == "China":
        main_language = "Mandarin" #because using the string parsing we get Standard
    country_lang_dict[country_name] = main_language

print country_lang_dict
pickle.dump(country_lang_dict,open("country_lang_dict.p","wb"))
