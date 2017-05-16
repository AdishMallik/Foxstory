import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt
from urlparse import urlparse

#Method to parse the URL
def parse(url):
   try:
       parse_url = urlparse(url) 
       domain = parse_url.netloc
       return domain
   except IndexError:
       print("URL format error")

#Method to show the results in a tabular format
def analyse(results):

    	plt.bar(range(len(results)), results.values(), align='edge')
        plt.xticks(rotation=20)
	plt.xticks(range(len(results)), results.keys())

	plt.show()

	
data_path = os.path.expanduser('~')+"/.mozilla/firefox/7xov879d.default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'places.sqlite')#Path of the sqlite database

#Connect to the database 
c = sqlite3.connect(history_db)
cursor = c.cursor()

#Select all from the database
select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
cursor.execute(select_statement)

results = cursor.fetchall()

sites_count = {}

#Calculate the count for each site
for url, count in results:
      url = parse(url) 
         if url in sites_count:
            sites_count[url] += 1
         else:
            sites_count[url] = 1 
	
	
sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True)[:10])#Statement to sort and find the top 10 visited sites

analyse(sites_count_sorted)


