#Contains methods to transform cuisines and to/from veg/non-veg/vegan transforms

import RecipeRepresentation
import HelperMethods
import scraper
import userInput
import main
import re
import nltk
import json
import random 


ingData = open('vocabulary/ingredientTypes2.json')
json_data = json.load(ingData)


def TrandformationVegNonVeg():  
	print "1. Transform to Vegan"
	print "2. Transform to Non Vegetarian"
	print "3. Transform to Vegetarian"
	choice_number = input("Enter your choice: ")
	#choice_number = raw_input()
	return choice_number 

def TransformationCuisine():
	#print "Enter your options",
	print "1. Transform to Indian"
	print "2. Transform to Mexican"
	print "3. Transform to Italian"
	print "4. Transfrom to East Asian"
	print "5. Transform to French"
	choice_number = input("Enter your choice: ")
	#choice_number = raw_input()
	return choice_number 

# French, Mexican, American Chinese, Indian, Itallian, Middle East 
def TranformToIndian(nameType_dict): 
	#print "### Transfroming to Indian ####"
	new_ing_list = []
	flag = 0
	count = 0 
	#print len(nameType_dict)
	for old_ing,ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_Indian() 
		#print count
		#print(old_ing)
		#print(ing_type)
		ingObject.m_originalIng = old_ing
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
					ingObject.m_IngName = "unknown"
	 				flag = 1
	 		if flag == 0: 
	 			new_type = random.choice(json_data["spices"]["indian"]);  
	 			ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "breads"): 
	 		new_type = random.choice(json_data["indianBreads"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["indianHerbs"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["indianCurry"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	else:
	 		ingObject.m_IngName = "unknown"
	 		new_ing_list.append(ingObject)
	 	count = count+1
	return new_ing_list

def TransformToMexican(nameType_dict):
	#print "### Transfroming to Mexican ####"
	flag = 0
	count = 0
	new_ing_list = [] 
	for old_ing,ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_Mexican() 
		#print count
		#print old_ing 
		ingObject.m_originalIng = old_ing
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
	 				#print "Not changed","\n"
	 				ingObject.m_IngName = "unknown"
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["mexican"])
	 				ingObject.m_IngName = new_type
	 				#print "changed to ", new_type,"\n"
	 		new_ing_list.append(ingObject)		
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["sauces"]["mexican"]) 
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "roots" or ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["beans"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "breads"): 
	 		#new_type = random.choice(json_data["beans"])  
	 		ingObject.m_IngName = "tortillas"
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["MexicanHerbs"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	else:
	 		ingObject.m_IngName = "unknown"
	 		new_ing_list.append(ingObject)
	 	count = count + 1
	return new_ing_list
	# print "#############"
	# print new_ing_list 

def TransformToItalian(nameType_dict):
	#print "### Transfroming to Mexican ####"
	flag = 0
	count = 0 
	new_ing_list = []
	for old_ing,ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_Italian() 
		#print count
		#print old_ing
		ingObject.m_originalIng = old_ing
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
					ingObject.m_IngName = "unknown"
	 				#print "Not changed","\n"
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["italian"])
	 				ingObject.m_IngName = new_type
	 				#print "changed to ", new_type,"\n"
	 			new_ing_list.append(ingObject)	
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["sauces"]["italian"]) 
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["beans"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "breads"): 
	 		new_type = random.choice(json_data["italianBreads"]) 
	 		ingObject.m_IngName = new_type 
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["italianHerbs"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	else:
	 		ingObject.m_IngName = "unknown"
	 		new_ing_list.append(ingObject)
	 	count = count + 1
	return new_ing_list

def TransformToFrench(nameType_dict):
	#print "### Transfroming to Mexican ####"
	flag = 0
	count = 0 
	new_ing_list = []
	for old_ing,ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_French() 
		#print count
		#print old_ing
		ingObject.m_originalIng = old_ing
		if(ing_type == "spices"): 
			for i in json_data["spices"]["general"]: 
				if i == old_ing: 
					ingObject.m_IngName = "unknown"
	 				#print "Not changed","\n"
	 				flag = 1  
	 			if flag == 0: 
	 				new_type = random.choice(json_data["spices"]["french"])
	 				ingObject.m_IngName = new_type
	 				#print "changed to ", new_type,"\n"
	 			new_ing_list.append(ingObject)	
	 	elif(ing_type == "sauces"): 
	 		new_type = random.choice(json_data["sauces"]["french"]) 
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
	 		new_type = random.choice(json_data["proteins"]["french"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "breads"): 
	 		new_type = random.choice(json_data["frenchBreads"]) 
	 		ingObject.m_IngName = new_type 
	 		new_ing_list.append(ingObject)
	 	elif(ing_type == "herbs"): 
	 		new_type = random.choice(json_data["frenchHerbs"])  
	 		ingObject.m_IngName = new_type
	 		new_ing_list.append(ingObject)
	 	else:
	 		ingObject.m_IngName = "unknown"
	 		new_ing_list.append(ingObject)
	 	count = count + 1
	return new_ing_list


def TransformToEastAsian(nameType_dict):
    #print "### Transfroming to Mexican ####"
    flag = 0
    count = 0
    new_ing_list = []
    for old_ing,ing_type in nameType_dict.items():
        #print count
        #print old_ing
        ingObject = RecipeRepresentation.Transformed_EastAsian()
        ingObject.m_originalIng = old_ing
        if(ing_type == "spices"):
            for i in json_data["spices"]["general"]:
                if i == old_ing:
                	ingObject.m_IngName = "unknown"
                    #ingObject.m_IngName = i
                    #print "Not changed","\n"
                	flag = 1
                if flag == 0:
                 	new_type = random.choice(json_data["spices"]["eastasian"])
                	ingObject.m_IngName = new_type
            	new_ing_list.append(ingObject)   	
                	#print "changed to ", new_type,"\n"
        elif(ing_type == "sauces"):
            new_type = random.choice(json_data["sauces"]["eastasian"]) 
            ingObject.m_IngName = new_type
            new_ing_list.append(ingObject) 
            #print "changed to ", new_type,"\n"
        elif(ing_type == "roots" or ing_type == "tubers" or ing_type == "squash" or ing_type == "radish" or ing_type == "regular"): 
            new_type = random.choice(json_data["proteins"]["beans"])  
            ingObject.m_IngName = new_type
            new_ing_list.append(ingObject) 
            #print "changed to ", new_type,"\n"
        elif(ing_type == "poultry"): 
            new_type = random.choice(json_data["proteins"]["seafood"]) 
            ingObject.m_IngName = new_type
            new_ing_list.append(ingObject)  
            #print old_ing, "changed to ", new_type,"\n"
        elif(ing_type == "herbs"): 
            new_type = random.choice(json_data["eastasianHerbs"])  
            ingObject.m_IngName = new_type
            new_ing_list.append(ingObject) 
            #print old_ing, "changed to ", new_type,"\n"
        else:
            ingObject.m_IngName = "unknown"
            new_ing_list.append(ingObject) 
            #print "Not changed","\n"
        count = count + 1
    #new_ing_list.append(ingObject.m_IngName)
    return new_ing_list

def TransformToLowFat(ingredientsDict):
	print "Transform to Low Fat"
	#Find all the ingredients that are fatty 

def TransformToVegetarian(nameType_dict):
	#Find any meat and egg components of the recipe and add vegetables in place of them
	
	#print "### Transforming to Vegetarian ###"
	# ing = old_ing
	new_ing_list = [] 
	for ing, ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_Vegetarian()
		ingObject.m_originalIng =  ing
		if(ing_type == "meats" or ing_type == "poultry" or ing_type == "eggs" or ing_type == "seafood"):
			new_type=random.choice(json_data["proteins"]["vegetarian"])
			ingObject.m_IngName = new_type
			#print "Changed to ",new_type,"\n"
		else:
			ingObject.m_IngName = "unknown"
		new_ing_list.append(ingObject)
	return new_ing_list	


def TransformToVegan(nameType_dict):
	#Find meat, eggs, and dairy components and replace them with appropriate ingredients
	#print "### Transforming to Vegan ###" 
	new_ing_list = [] 
	count = 0 
	for ing, ing_type in nameType_dict.items():
		#print ing
		ingObject = RecipeRepresentation.Transformed_Vegan()
		ingObject.m_originalIng = ing
		#print count 
		if(ing_type == "meats" or ing_type == "poultry" or ing_type == "eggs" or ing_type == "seafood"):
			new_type=random.choice(json_data["proteins"]["beans"])
			ingObject.m_IngName = new_type
			#print "Changed to ",new_type,"\n"
		elif(ing_type == "dairy"):
			new_type = "soy milk"
			ingObject.m_IngName = new_type
			#print "Changed to ", new_type
		else:
			ingObject.m_IngName = "unknown"
			#print "Not changed"
		count = count + 1 
		new_ing_list.append(ingObject)
	return new_ing_list	

def TransformToNonVegetarian(nameType_dict):
	#Find vegetarian products and replace with meat or eggs
	new_ing_list = [] 
	count = 0
	for ing, ing_type in nameType_dict.items():
		ingObject = RecipeRepresentation.Transformed_NonVegetarian()
		ingObject.m_originalIng = ing
		#print ing
		#print count
		if (ing_type == "regular" or ing_type == "onions" or ing_type == "roots" or ing_type == "radish" or ing_type == "squash" or ing_type == "tubers"):
			list_picker=["meats","eggs","poultry","seafood"]
			picked=random.choice(list_picker)
			new_type=random.choice(json_data["proteins"][picked])
			ingObject.m_IngName = new_type
			#print "Changed to ",new_type,"\n"
		else:
			ingObject.m_IngName = "unknown"
			#print "Not changed."
		count = count + 1
		new_ing_list.append(ingObject)
	return new_ing_list	



