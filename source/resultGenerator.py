import RecipeRepresentation
import HelperMethods
import scraper
import pdb

def autograde(url):
	ingredientsDict = scraper.scrapeIngredients(url)
	directionsList = scraper.getDirections(url)
	HelperMethods.identifyIngredients(ingredientsDict)
	HelperMethods.identifyTools(directionsList)
	HelperMethods.identifyCookingMethods(directionsList)
	result = {'url':url, 'ingredients':[]}
	numOfIngredients = 0
	numOfCookMethods = 0
	numOfTools = 0
	numOfPrimMethods = 0
	for ingObject in HelperMethods.ingredientList:
		#These lists hold names, desciptors, preparation and preparation description
		#for each ingredient. These will be directly pushed to the dictionary.
		nameList = []
		descriptorList = []
		preparationList = []
		prepDescList = []
		#Push different combinations of ingredient names (ingredient name + descriptor(s))
		name = ingObject.m_IngName
		nameList.append(name)
		for descriptor in ingObject.m_IngDescriptor:
			name = descriptor + " " + name
			#Push all descriptors in descriptor list
			descriptorList.append(descriptor)
			nameList.append(name)
		#Push all preparations in preparation list
		for preparation in ingObject.m_IngPreparation:
			preparationList.append(preparation)
		#Push all preparation descriptors in preparation description list	
		for prepDesc in ingObject.m_IngPrepDescriptor:
			prepDescList.append(prepDesc)	 	
		entry = {}
		entry['name'] = nameList
		entry['quantity'] = ingObject.m_quantAutoGrade
		entry['measurement'] = ingObject.m_IngMeasurement
		entry['descriptor'] = ' '.join(descriptorList)
		entry['preparation'] = ' '.join(preparationList)
		entry['prepDescList'] = ' '.join(prepDescList)
		result['ingredients'].append(entry)
		numOfIngredients = numOfIngredients + 1

	result['primary cooking method'] = ''
	#Add cooking methods
	methodsList = []
	for methodObj in HelperMethods.cookingMethodsList:
		if(len(methodObj.m_MethodName)>0):
			for index in range(0,len(methodObj.m_MethodName)):	
				methodsList.append(methodObj.m_MethodName[index])
				numOfCookMethods = numOfCookMethods + 1
				retVal = checkMethodType(methodObj.m_MethodName[index])
				if retVal == True:
					result['primary cooking method'] = methodObj.m_MethodName[index]
	#print methodsList		
	result['cooking methods'] = ' '.join(methodsList)
	#Add cooking tools	
	toolsList = []
	for toolObj in HelperMethods.toolsList:
		toolsList.append(toolObj.m_ToolName)
		numOfTools = numOfTools + 1
	result['cooking tools'] = ' '.join(toolsList)
	#result['max'] = {'ingredients':numOfIngredients, 'primary cooking method':numOfPrimMethods, 'cooking tools':numOfTools, 'cooking methods':numOfCookMethods}
	return result


def checkMethodType(name):
	fprimary = open('vocabulary/primaryMethods.txt', 'r')
	primaryCookingMethods = []
	for line in fprimary:
		primaryCookingMethods.append(line.replace('\n',''))
	if name in primaryCookingMethods:
		return True	
	fprimary.close()	
