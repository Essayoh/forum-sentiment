import requests
import bs4
import shutil
import os
from time import strftime
from string import punctuation
import urllib

date = strftime("%Y-%m-%d")
page_count = 1
words_used = []
positive_counter = 0
negative_counter = 0
total_words = 0

download_path='http://www.unc.edu/~ncaren/haphazard/'
files=['negative.txt','positive.txt']
for filename in files:
	urllib.urlretrieve(download_path+filename, filename)

pos_words = open('positive.txt').read()
pos_words = pos_words.split("\n")

neg_words = open('negative.txt').read()
neg_words = neg_words.split("\n")


print("Please paste the URL of the topic to be analyzed:")

root_url = raw_input()

print("How many pages long is this thread?")

number_of_pages = raw_input()

sep = "?"
root_url = root_url.rsplit(sep, 1)[0] #splitting on the ?
root_url = root_url + "/page/" + str(page_count)


response = requests.get(root_url)
soup = bs4.BeautifulSoup(response.text)

for topic in soup.find_all(class_="post"):
   		words_used.append(topic.get_text().encode('utf-8'))

words_used = '\n'.join(words_used)
words_used = words_used.lower()

for p in list(punctuation):
	words_used = words_used.replace(p,'')

for word in words_used.split():
	if word in pos_words:
		positive_counter = positive_counter+1
		total_words = total_words+1
	elif word in neg_words:
		negative_counter = negative_counter+1
		total_words = total_words+1
	else:
		total_words = total_words+1

print("Positive Count is " + str(positive_counter) + ", Negative Count is " + str(negative_counter) + ", and the total wordcount is " + str(total_words))
