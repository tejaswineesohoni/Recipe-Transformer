#Classes used to define various attributes of a recipe

#Class to store ingredient information 
class Ingredients:
	def __init__(self):
		self.m_IngName = '' #ingredient name
		self.m_IngType = '' #ingredient type
		self.m_IngQuantity = '' #quantity
		self.m_IngMeasurement = '' #measurement
		self.m_IngDescriptor = [] #descriptor
		self.m_IngPreparation = [] #preparation
		self.m_IngPrepDescriptor = [] #preparation description
		self.m_quantAutoGrade = 0.0 #quantity in float, for the autograder

#Class to store Tools
class Tools:
	def __init__(self):
		self.m_ToolName = '' #tool name
		self.m_ToolQuantity = 0 #tool quantity

class Methods:
	def __init__(self):
		self.m_MethodName = [] #Method name
		self.m_MethodType = '' #Cooking method type - Primary or Secondary
		self.m_ingredientUsed = [] #Ingredient on which the method has to be applied
		self.m_toolsUsed = [] #Tools used for this method
		self.m_time = 0 #Time consumed by this method

#Classes that hold information about various transformations
#Class for transformed cooking methods
class TransformMethods:
	def __init__(self):
		self.m_methodName = [] #list of new cooking methods suggested
		self.m_ingredient = '' #ingredient in which this change has to be applied
		self.m_originalMethod = '' #the origianl method name

#Classes to hold information about new cuisines transformation	
class Transformed_Indian: 
	def __init__(self): 
		self.m_IngName = '' #new ingredient name
		self.m_originalIng = '' #original ingredient name
#This pattern applies to all the remaining classes		

class Transformed_Italian: 
	def __init__(self): 
		self.m_IngName = ''
		self.m_originalIng = ''

class Transformed_Mexican: 
	def __init__(self): 
		self.m_IngName = ''
		self.m_originalIng = ''

class Transformed_Vegetarian:  
	def __init__(self): 
		self.m_IngName = ''
		self.m_originalIng = ''

class Transformed_NonVegetarian:  
	def __init__(self): 
		self.m_IngName = ''
		self.m_originalIng = ''

class Transformed_Vegan:  
	def __init__(self): 
		self.m_IngName = ''
		self.m_originalIng = ''

class Transformed_EastAsian:
    def __init__(self):
        self.m_IngName = ''
        self.m_originalIng = ''

class Transformed_French:
    def __init__(self):
        self.m_IngName = ''
        self.m_originalIng = ''




