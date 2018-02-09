import urllib2
import re
import pickle

# LOADING THE COUNTRIES POPULATION DATA FROM WIKIPEDIA
response = urllib2.urlopen("https://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population")
pop_page_source = response.read()
countries_pop_dict = {} #units of population in thousands

# get the 1950 to 1980 data
start = "<th>1950</th>"
end = "<th>1985</th>"
text_between = (pop_page_source.split(start))[1].split(end)[0]
each_country = text_between.split("title=\"")
for country_text in each_country[1:-2]:
    curr_country = country_text.split("\">")[0]
    if curr_country not in countries_pop_dict:
        countries_pop_dict[curr_country] = {}
    nums = country_text.split("<td>")
    pop1950 = nums[1].split("</td>")[0].replace(',', '')
    pop1955 = nums[2].split("</td>")[0].replace(',', '')
    pop1960 = nums[4].split("</td>")[0].replace(',', '')
    pop1965 = nums[6].split("</td>")[0].replace(',', '')
    pop1970 = nums[8].split("</td>")[0].replace(',', '')
    pop1975 = nums[10].split("</td>")[0].replace(',', '')
    pop1980 = nums[12].split("</td>")[0].replace(',', '')
    countries_pop_dict[curr_country][1950] = int(pop1950)
    countries_pop_dict[curr_country][1955] = int(pop1955)
    countries_pop_dict[curr_country][1960] = int(pop1960)
    countries_pop_dict[curr_country][1965] = int(pop1965)
    countries_pop_dict[curr_country][1970] = int(pop1970)
    countries_pop_dict[curr_country][1975] = int(pop1975)
    countries_pop_dict[curr_country][1980] = int(pop1980)
    
# get the 1985 to 2015 data
start = "<th>1985</th>"
end = "<th>2020</th>"
text_between = (pop_page_source.split(start))[1].split(end)[0]
each_country = text_between.split("title=\"")
for country_text in each_country[1:-2]:
    curr_country = country_text.split("\">")[0]
    if curr_country not in countries_pop_dict:
        countries_pop_dict[curr_country] = {}
    nums = country_text.split("<td>")
    pop1985 = nums[1].split("</td>")[0].replace(',', '')
    pop1990 = nums[3].split("</td>")[0].replace(',', '')
    pop1995 = nums[5].split("</td>")[0].replace(',', '')
    pop2000 = nums[7].split("</td>")[0].replace(',', '')
    pop2005 = nums[9].split("</td>")[0].replace(',', '')
    pop2010 = nums[11].split("</td>")[0].replace(',', '')
    pop2015 = nums[13].split("</td>")[0].replace(',', '')
    countries_pop_dict[curr_country][1985] = int(pop1985)
    countries_pop_dict[curr_country][1990] = int(pop1990)
    countries_pop_dict[curr_country][1995] = int(pop1995)
    countries_pop_dict[curr_country][2000] = int(pop2000)
    countries_pop_dict[curr_country][2005] = int(pop2005)
    countries_pop_dict[curr_country][2010] = int(pop2010)
    countries_pop_dict[curr_country][2015] = int(pop2015)

# get the 1985 to 2015 data
start = "<th>2020</th>"
end = "</table"
text_between = (pop_page_source.split(start))[1].split(end)[0]
each_country = text_between.split("title=\"")
for country_text in each_country[1:-2]:
    curr_country = country_text.split("\">")[0]
    if curr_country not in countries_pop_dict:
        countries_pop_dict[curr_country] = {}
    nums = country_text.split("<td>")
    pop2020 = nums[1].split("</td>")[0].replace(',', '')
    pop2025 = nums[3].split("</td>")[0].replace(',', '')
    pop2030 = nums[5].split("</td>")[0].replace(',', '')
    pop2035 = nums[7].split("</td>")[0].replace(',', '')
    pop2040 = nums[9].split("</td>")[0].replace(',', '')
    pop2045 = nums[11].split("</td>")[0].replace(',', '')
    pop2050 = nums[13].split("</td>")[0].replace(',', '')
    countries_pop_dict[curr_country][2020] = int(pop2020)
    countries_pop_dict[curr_country][2025] = int(pop2025)
    countries_pop_dict[curr_country][2030] = int(pop2030)
    countries_pop_dict[curr_country][2035] = int(pop2035)
    countries_pop_dict[curr_country][2040] = int(pop2040)
    countries_pop_dict[curr_country][2045] = int(pop2045)
    countries_pop_dict[curr_country][2050] = int(pop2050)

# saving final data
print countries_pop_dict
pickle.dump(countries_pop_dict,open("countries_pop_dict.p","wb"))
