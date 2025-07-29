#Variables in Python
#Python Numeric Data type
num1 = 55
num2 = 5.3
print(num1)
print(num2) 
#int - holds signed integers of non-limited length.
#float - holds floating decimal points and it's accurate up to 15 decimal places.

#Access List Items
languages = ["Python", "Dart", "Web", 23]
print(languages[1])

#To access items from a list, we use the index number (0, 1, 2 ...). For example
#In the above example, we have used the index values to access items from the languages list.
#languages[0] - access the first item from languages i.e. Python
#languages[2] - access the third item from languages i.e. Web

#Python Tuple Data Type
products = ('XBox', 499.99, "Habibi", 23)
print(products)
#In Python, we use the parentheses () to store items of a tuple
#Access Tuple Items
#Similar to lists, we use the index number to access tuple items in Python. For example
products = ('XBox', 499.99, "Habibi", 23)
print(products[2])

#Python String Data Type
#String is a sequence of characters represented by either single or double quotes.
site_name = "Power Learn Project"
print(site_name)

#Python Set Data Type
#The Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }.
student_ids = {112, 114, 117, 113}
print(student_ids)

#Python Dictionary Data Type
#Python dictionary is an ordered collection of items. It stores elements in key/value pairs.
#Here, keys are unique identifiers that are associated with each value.
capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
print(capital_city)