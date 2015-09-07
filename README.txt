RECIPE TRANSFORMER
EECS 337 - Project 2
Group 4
Members: Tejaswinee Sohoni, Zach Straight, Harsh Sarin, Surabhi Ravishankar

Prerequisites:

This source uses the following libraries:
- urllib2 and BeautifulSoup for web scraping.
- re: library to use Regular Expressions.
- nltk: Natural Language ToolKit for tokenizing words, sentences and using parts of speech
	tagging.
- json: to read from the JSON files.

These packages can be downloaded from the pip repository

Running the code:

To run the code navigate to the ‘source’ folder in the terminal. Then run the following command:
-> python main.py
When prompted by the following message:
‘Enter the URL of the recipe you want to explore:’ - enter the recipe URL within ‘ ’ block

Suggestion: 

Our implementation works well for the following URLs:
—>’http://allrecipes.com/Recipe/Jambalaya-II/Detail.aspx?soid=recs_recipe_3'
—>’http://allrecipes.com/Recipe/Homemade-Chicken-Enchiladas/Detail.aspx?evt19=1&referringHubId=201’
—>’http://allrecipes.com/Recipe/Honey-Mustard-Grilled-Chicken/Detail.aspx?event8=1&prop24=SR_Thumb&e11=grilled%20chicken&e8=Quick%20Search&event10=1&e7=Recipe&soid=sr_results_p1i2’
—>’http://allrecipes.com/Recipe/Easy-Garlic-Broiled-Chicken/'

To run the autograder, navigate to ‘source’ folder and run the following command:
- python autograder.py

To understand how the ingredient information is stored, and how the transformations work, navigate to the documents folder and read the “Recipe Representation and Transformations.pdf”.