# Strings
#piece of text

'hi there'
"hi there"
print(type("hi"))

username = "supercoder"
password = "supersecret"
long_string = ''' 
WOW
0 0 
 I
---
'''

first_name = "Kristyna"
last_name = 'Parker'
full_name = first_name + " " + last_name
print(full_name)

# String Concatenation

print("Hello" + " Kristy")

# Type Conversion

print(type(str(100)))

a = str(100)
b = int(a)
c = type(b)

print(c)


# Escape Sequence

#weather = "It"s sunny"
#weather = "It's sunny"
weather = "It\'s \"kind of\" sunny"
print(weather)

# special tricks
# \t add a tab
# \n a new line


#Formatted strings

name = "Johnny"
age = 55

print("Hi " + name + ". You are "+ str(age) + " years old." )

print(f"Hi {name}. You are {age} years old.") # Way to go

print("Hi {}. You are {} years old.".format(name, age))

print("Hi {0}. You are {1} years old.".format(name, age))

print("Hi {new_name}. You are {age} years old.".format(new_name = "Sally", age = 44))

#EXERCISE String formatting

# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string?
name = "Cindy"
amount = 50
print(f"Hello {name}, your balance is {amount}.")


# String indexes

word ="01234567"
print(word[6])

# String slicing

#[start:stop]
print(word[0:8]) #01234567

#[start:stop:stepover]
print(word[0:8:2]) #0246

print(word[1:]) # 1234567

print(word[:5]) # 01234

print(word[::1]) #default behavior 01234567

print(word[-1]) #7
print(word[-4]) #4

print(word[::-1]) #76543210
print(word[::-2]) #7531

# Immutability
#You can't reassign part of a string - once created it exists like that
# only way to chnage it is to create sth new

word ="01234567"
name = "saurabh"
# word[0] = "g" 
# the above statement gives error.
word = word + "100"

print(word)


#EXERCISE String indexes

python = 'I am PYHTON'

print(python[1:4])  
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])