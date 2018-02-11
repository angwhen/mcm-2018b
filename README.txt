Instructions for Single Language Country Only Model
1. download countries_pop_dict.p from angel. load_and_save_pop_data.py script scrapes from wikipedia page which may be changed at any time.
2. run load_and_save_country_lang_data.py to get pickle file for language of each country (will need country_languages.ods from angel)
3. run make_and_save_lang_pop_data.py to get pickle file of dict matching each langauge to the population over time
4. run country_only_model_graphs.py to view visualizations of languages over time as measured country pop

Instructions for Correlating Country to Native Speakers
1. run load_and_save_native_speakers.py to get dict of language to 2007 estimates of total speakers (will need native_speakers.ods from angel) - data in millions
2. run correlate_native_speakers_country_pop.py to get a graph comparing the estimates gotten from interpolating #of speakers from population of country (2010), and the native speakers (2007) data from wikipedia. Also saves language_native_prop_dict.py with proportion (native/country) for each language
 - also hope to do some statistics thing to see how strong the relationship/prediction factor is ...

Instructions for Correlating Country to L1 and L2 Speakers
1.run load_and_save_all_speakers.py to get dict of language to l1 and l2 estimates from wikipedia (will need all_speakers.ods from angel) - data in millions
2. run correlate_all_speakers_country_pop.py to:
   a. get graphs comparing country interpolation (2010) with actual l1 and l2 data
   b. save language_l12_prop_dict with every index as language, and every value a [l1_prop, l2_prop] (l12/country total) based on country est to wikipedia data
3. run country_proportions_model_graphs.py to get graphs of l1/l2 speakers over time as measured by assuming l1/l2 speakers grow proportional to country population (at proportion measured by previous steps)
 - hope to be able to add "confidence interval" or something, based on comparing l1 to native speaker proportions

Libraries you may need to install:
1. matplotlib
2. pyexcel_ods
