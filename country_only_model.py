import pickle

countries_pop_dict = pickle.load(open("countries_pop_dict.p","rb"))
countries_lang_dict = pickle.load(open("country_lang_dict.p","rb"))

# make language to population/year dict
lang_pop_dict = {}
countries_with_pop = countries_pop_dict.keys()
for country_name in countries_lang_dict.keys():
    country_name = country_name.replace("St.","Saint")
    country_name = country_name.replace(" (proposed state)","")
    country_name = country_name.replace(" (proposed)","")
    if "," in country_name:
        two_parts =  country_name.split(",")
        country_name = (two_parts[1]+" "+two_parts[0]).strip()
    if country_name not in countries_with_pop:
        close_names = [s for s in countries_with_pop if country_name in s]
        if len(close_names) > 0:
            country_pop_name = close_names[0]
        elif country_name == "Sao Tome and Principel":
            country_pop_name = "S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe"
        elif country_name == "Palestinian State":
            country_pop_name = "State of Palestine"
        else:
            continue # can't match
    else:
        country_pop_name = country_name
    curr_lang = countries_lang_dict[country_name]
    if curr_lang not in lang_pop_dict:
        
