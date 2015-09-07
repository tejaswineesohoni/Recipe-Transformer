#Crawler
import urllib2
import sys
from bs4 import BeautifulSoup

#Fetch ingredients
def scrapeIngredients(r_url):
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)
 
	name_list = []
	amount_list = []

	tags = soup.find_all("p",{"itemprop":"ingredients"})
	for tag in tags:
		children =  tag.findChildren() 
		if len(children) == 2:
			amount_list.append(children[0].string)
			name_list.append(children[1].string)
		elif len(children) == 1:
			amount_list.append('')
			name_list.append(children[0].string)	
	ingredient_dict = dict(zip(name_list, amount_list))
	return ingredient_dict	

#Fetch directions
def getDirections(r_url):
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)
	#finding directions 
	all_directions = soup.find_all("span",{"class":"plaincharacterwrap break"})
	#directions list
	dir_list = [] 
	for d in all_directions: 
		dir_list.append(d.string)
	return dir_list

#Fetch preparation time, rating, recipe title
#Only recipe title fetching works, so commented the remaining function
def getPrepTimeRating(r_url): 
	prepTime = ''
	readyTime = ''
	cookTime = ''
	rating = ''
	title = ''
	response = urllib2.urlopen(r_url)
	html_content = response.read()
	soup = BeautifulSoup(html_content)
	#Prep time 
	# prep_time = soup.find("span",{"id":"prepMinsSpan"})
	# if(prep_time):
	#  	prepTime = prep_time.string

	# #Ready-In
	# ready_time = soup.find("span",{"id":"totalMinsSpan"})
	# if(ready_time): 
	# 	readyTime  = ready_time.string 

	# #Cook time 
	# cook_time = soup.find("span",{"id":"cookHoursSpan"})
	# if(cook_time):
	# 	cookTime = cook_time.string

	#Ratings 
	#rating = soup.find("meta",{"itemprop":"ratingValue"})

	Title = soup.find("h1",id='itemTitle')
	title = Title.string

	heading = ''
	if(title != ''):
		heading = heading + title + "."
	print heading

#create a dictionary of tool names from Wikipedia
def populateTools():
	f = open('vocabulary/tools.txt','w');
	html_source = urllib2.urlopen("http://en.wikipedia.org/wiki/Category:Cooking_utensils")
	wikiPage = BeautifulSoup(html_source)
	div = wikiPage.find('div', id='mw-pages')
	alphabeticalList = div.findAll('ul')
	firstItemSkipped = False;
	for listIndex in alphabeticalList:
		if(firstItemSkipped == False):
			firstItemSkipped = True
			continue;
		hyperlinks = listIndex.findAll('a')
		for hyperlink in hyperlinks:
			utensilName = hyperlink.string.lower()
			utensilName = re.sub(r'\(.*\)',r'',utensilName)
			f.write(utensilName+'\n')
	f.close()