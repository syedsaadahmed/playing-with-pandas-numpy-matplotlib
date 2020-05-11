from urllib.request import urlopen as request
import re, requests, time
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

import nltk
nltk.download('stopwords')

url = "http://quotes.toscrape.com/page/"

quotes_list = []
page_count = 1

def check_module():
	chk = len(parsed_html.body.findAll(text=re.compile("No quotes found!")))
	return chk

start_time = time.time()
#while loop for getting the exact page count and data on every page 
while page_count:
	# print('at Page no '+str(page_count))
	# print('---------------------------------------------------')
	request = requests.get(url + str(page_count))
	parsed_html = BeautifulSoup(request.text, "html.parser")
	if check_module() > 0:
		break
	else:
		quotes = parsed_html.findAll("div", {"class": "quote"})
		for quote in quotes:
			quotes_list.append({
				'quote': quote.find("span", {"class": "text"}).text,
				'author': quote.find("small", {"class": "author"}).text,
				'tags': [tag.text for tag in quote.find_all("a", {"class": "tag"})]
			})
		page_count += 1


#print("- %s seconds to crawl %s pages---" % (time.time() - start_time),%(page_count-1))

print("- "+str(time.time() - start_time)+" seconds to crawl "+str(page_count-1)+" pages")

#resutls of the valid page number and their data is inside quotes_list
print('- Valid number of page count is '+str(page_count-1))


df = pd.DataFrame(quotes_list)
print(df)

# plot for counting number of quotes per author
authors=[]
for i in quotes_list:
	authors.append(i['author'])

lists = dict(Counter(authors)).items()
x, y = zip(*lists)
plt.plot(x, y)
plt.xlabel ('Name of Authors')
plt.ylabel ('No of Quotes')
plt.title('Distribution of the number of quotes per author')
plt.show()


# plot for frequency distribution of the tags
# create a list of tags
tags_list = df['tags'].tolist()
temp = []
for tags in tags_list:
    for tag in tags:
        temp.append(tag)
        
tags_list = temp

freq_dist = nltk.FreqDist(tags_list)
tags_count_df = pd.DataFrame(list(freq_dist.items()), columns=['tag', 'count'])
tags_count_df = tags_count_df.sort_values('count', ascending = False)
tags_count_df.set_index('tag', drop=False, inplace=True)

# plot frequency using matplotlib
def plot_freq(df, metric):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.gca()
    df['count'][:60].plot(kind='bar', ax=ax)
    ax.set_title('Frequency of the most common ' + metric + 's')
    ax.set_ylabel('Frequency of Tags')
    ax.set_xlabel('Tags Avaiable')
    plt.show()

plot_freq(tags_count_df, 'Tag')
