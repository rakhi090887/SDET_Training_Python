print("Hello World")
#Variable Section
print(" ########### Variable Section ###########")
myvariable=5
print(myvariable)

#Python Number
""" Python has 3 type of numbers
int, float, complex """
print(" ########### Type of numbers ###########")
a=8
b=2.7
c=1j
print(a , b , c)

# Type of the variable using type() function
print(" ########### Type of the variable ###########")
print(type(a))
print(type(b))
print(type(c))

"""  Pythn Strings : Strings is seqance of text. 
that must be surrounded by either single quote or double quote. """
print(" ########### String ###########")
print("HI Rakhi")
print('Hi Rakhi')

# Assigning string to variable
print(" ########### Assigning string to variable ###########")
a="Welcome"
print(a)

# Multiline string
print(" ########### Multiline string ###########")
a="""This is Python.
Welcome to Python"""
print(a)

# Strings in Pyhton works like Array. Array starts from 0 index
print(" ########### String works like Array ###########")
a= "Welcome to India"
print("char value in string array: "+a[2])

# String slicing: return range of char using slicing syntax variable(startindex:endindex)
print(" ########### String slicing ###########")
a="Welcome to IBM"
print("slicing Of a: "+a[2:5])

# Lenth function
print(" ########### String Lenth function ###########") 
a = "Hello, world"
print(len(a))

# String upper and lower
print(" ########### String Upper and Lower ###########")
a='Welcome'
print("Upper of a: "+a.upper())
print("Lower of a: "+a.lower())

# String replace and split
print(" ###### String replace and split ###########")
a="Welcome to India"
print(a.replace('India','IBM')) #Replace
print(a.split( ))

# check String
print(" ###### check String ####### ")
txt="The rain in spain stays mainly in the plain"
x= "ain" in txt
y = "ain" not in txt
print(x , y)

# Stirng concatination : 
print( "#### Stirng concatination #### " )
a="Hello" 
txt1=" world"
c=a + txt1
print(c)

# String format tHIS WILL GIVE ERROR
print( "####### String format ######## ") 
age=36
#txt="My name is John, I am "+ age
#print(txt)
# TO DO SO
txt1="My name is John, I am {}"
print(txt1.format(age))

quantity=3
itemno = 567
proce=49.95
myorder = "I want {} piece if item {} for {} dollars."
print(myorder.format(quantity,itemno,proce))
myorder1="I want to pay {2} dollars {0} for piece of item {1}"
print(myorder1.format(quantity,itemno,proce))




