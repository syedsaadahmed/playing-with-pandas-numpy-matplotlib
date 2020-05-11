import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plot



URL = 'https://simple.wikipedia.org/wiki/List_of_countries_by_continents'
material = requests.get(URL)
soup = BeautifulSoup(material.content, 'html.parser')


final_dict = {}
for tag in soup.find_all('span',class_="mw-headline"):
	if not any([tag.text=='Other websites',tag.text=='References',tag.text=='Antarctica']):
		countries_ul = tag.find_next('ul')
		coun = [li.find_next('a')['title'] for li in countries_ul.findAll('li')]
		final_dict.update({tag.text:coun})
final_dict.update({'Antarctica':['']})


# final_dict = {}
# for tag in soup.find_all('span',class_="mw-headline"):
# 	if not any([tag.text=='Other websites',tag.text=='References',tag.text=='Antarctica']):
# 		countries_ul = tag.find_next('ul')
# 		coun = [li.getText().split('-')[0].strip() for li in countries_ul.findAll('li')]
# 		final_dict.update({tag.text:coun})
# final_dict.update({'Antarctica':['']})


df = pd.DataFrame(columns=['Country or region','continent'])
for conti in final_dict.keys():
    for countr in final_dict[conti]:
        df = df.append({
             "Country or region":  countr,
             "continent": conti
              }, ignore_index=True)

URL_2 = 'https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report'
material_2 = requests.get(URL_2)
soup_2 = BeautifulSoup(material_2.content, 'html.parser')

tables = soup_2.find_all('table', class_='wikitable sortable')

for table in tables:
    ths = table.find_all('th')
    headings = [th.text.strip() for th in ths]
    if headings[:9] == ['Overall rank','Country or region','Score','GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption']:
    	break

df_2 = pd.DataFrame(columns=['Overall rank','Country or region','Score','GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption'])

for tr in table.find_all('tr'):
	tds = tr.find_all('td')
	if not tds:
		continue
	rank, country_name, score, GDP, social_support, healthy_life_expectancy,freedom_for_life_choice,generosity,perception_of_corruption = [td.text.strip() for td in tds[:9]]
	df_2 = df_2.append({
		'Overall rank': rank,
		'Country or region': country_name,
		'Score': score,
		'GDP per capita': GDP,
		'Social support': social_support,
		'Healthy life expectancy': healthy_life_expectancy,
		'Freedom to make life choices': freedom_for_life_choice,
		'Generosity': generosity,
		'Perceptions of corruption': perception_of_corruption
		}, ignore_index=True)


final_df = pd.merge(df, df_2, on='Country or region')
final_df = final_df.sort_values(by=['Score'], ascending=False)
final_df.to_csv('final_output.csv', index=False)


df_2['Score']=df_2['Score'].astype(float)
df_2.plot.bar(x='Country or region',y='Score', rot=90, title="Distribution of Happiness score per Country",legend=False);
plot.ylabel("Happiness Score")
plot.xlabel("Countries")
plot.show();

top_ten_happiest_countries = df_2[['Country or region','Score']].nlargest(10,'Score')

median_value = df_2["Score"].mean()

median_value = df_2["Score"].median()
below_median = df_2["Score"] < median_value
print(df_2[below_median][['Country or region','Score']])


final_df['Score']=final_df['Score'].astype(float)
final_df['Healthy life expectancy']=final_df['Healthy life expectancy'].astype(float)
final_df.plot.scatter(x='Score',y='Healthy life expectancy', rot=90, title="correlation plot for happiness score and Healthy life expectancy",legend=False);
plot.xlabel("Happiness Score")
plot.ylabel("Healthy life expectancy")
plot.show();

