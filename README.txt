Instructions for Single Language Country Only Model
1. download countries_pop_dict.p from angel. load_and_save_pop_data.py script scrapes from wikipedia page which may be changed at any time.
2. run load_and_save_country_lang_data.py to get pickle file for language of each country
3. run make_and_save_lang_pop_data.py to get pickle file of dict matching each langauge to the population over time
4. run country_only_model_graphs.py to view visualizations of languages over time as measured country pop

Libraries you may need to install:
1. matplotlib
2. pyexcel_ods
