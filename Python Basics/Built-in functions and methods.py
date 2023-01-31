# Built-in functions + methods
# https://www.w3schools.com/python/python_ref_string.asp
# https://docs.python.org/3/library/functions.html

greet = "hellllooo"
print(len(greet))

print(greet[0:len(greet)]) 

quote = "to be or not to be"

print(quote.upper()) # TO BE OR NOT TO BE
print(quote.capitalize()) # To be or not to be
print(quote.find("be")) # on index 3
print(quote.replace("be", "kill")) # :D

print(quote) # string are immutable!