#string data type

#literal assignments
first = 'Jake'
last = 'Stoltz'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#construction function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation
FullName = first + " " + last
print(FullName)

FullName += "!"

#casting a number to a string
decade = str(1980)

print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

#multiple lines
multiline = '''
Hey, how are you?

I was just checking in.

                        All good?

'''

print(multiline)

#escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#string methods

print(first.lower())
print(first.upper())
print(first)

print(multiline.title)
print(multiline.replace("good","okay"))
print(multiline)

print(len(multiline))
multiline += "                           "
multiline = "                           " +multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheesecake".ljust(16,".") + "$4".rjust(4))

#string index values
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("J"))
print(first.endswith("Z"))

#Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#numeric data type

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type

gpa = 3.28
y = float(1.14)
print(type(gpa))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = '10001'
Zip_Value = int(zipcode)
print(type(Zip_Value))

