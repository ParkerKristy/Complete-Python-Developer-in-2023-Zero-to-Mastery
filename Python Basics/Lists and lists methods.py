# List

li = [1, 2, 3, 4 ,5]
li2 = ["a", "b", "c"]
li3 = [1, 2.5, "a", True]

# Data Structure 
# organize data into structures, folders

amazon_cart = ["notebooks", "sunglasses"]
print(amazon_cart[0])
print(amazon_cart[1])
# print(amazon_cart[2]) IndexError: list index out of range

#String slicing - just reminder what we have already done
# string = 'helllloooo'
# print(string[0:2:1]) [start:end:step] he
 
#List slicing - we create entirely new list
amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
print(amazon_cart) #entire list
print(amazon_cart[0:2]) # ['notebooks', 'sunglasses']
print(amazon_cart[0::2]) # ['notebooks', 'toys']

#List are mutable - we can replace items in the list
amazon_cart[0] = "laptop"
print(amazon_cart) # ['laptop', 'sunglasses', 'toys', 'grapes']
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# EXERCISE Lists
#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!

new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)


# Matrix - way to descibe 2D (multidimensional) lists

matrix = [
    [1,2,3],
    [2,4,6], 
    [7,8,9]
    ] #subarrays
# used a lot in machine learning, images processing

print(matrix[0][1]) #accessing the first array and the item on position 1

# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

print(basket[1][1][0])

# Lists Methods https://www.w3schools.com/python/python_ref_list.asp

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

basket = [1,2,3,4,5]

#adding - it modifies the list inplace, it doesn't create a new copy of it
basket.append(100)
new_list = basket
print(new_list) # [1, 2, 3, 4, 5, 100]

new_list.insert(1, 55) #(position, object)
print(new_list) # [1, 55, 2, 3, 4, 5, 100]

new_list = basket.extend([100, 101])
print(basket)  # [1, 55, 2, 3, 4, 5, 100, 100, 101]


#removing
basket.pop ()  #removes the last item in the list
print(basket) # [1, 55, 2, 3, 4, 5, 100, 100]

basket.pop(0)
print(basket)  # [55, 2, 3, 4, 5, 100, 100]

new_list = basket.pop(4)  
print(new_list)     #return the element you have removed

basket.remove(4)   
print(basket) # [55, 2, 3, 5, 100, 100]

basket.clear()
print(basket)

#EXERCISE List methods

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove("Banana")
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
# 4. Add "Apples" at the beginning of the list
basket.insert(0,"Apples")
# 5. Count how many apples in the basket
print(basket.count("Apples"))
# 6. empty the basket
basket.clear()
print(basket)



basket = ['a','b','c','d','e', 'd']
print(basket.index('b')) #1
print(basket.index('d', 0, 4)) #indexional looking


#python keyword  https://www.w3schools.com/python/python_ref_keywords.asp

print('x' in basket)  #True/False
print('i' in 'hi my name is Ian')

print(basket.count('d'))

basket = ['a','x','b','c','d','e','d']
basket.sort()
print(basket) # ['a', 'b', 'c', 'd', 'd', 'e', 'x']

#built in function sorted
new_basket = basket.copy()
print(sorted(new_basket))  #sorted creates a new copy of a list does not modify it

basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(basket)


# COMMON LISTS PATTERNS

basket = ['a','x','b','c','d','e','d']
basket.sort()

#lenght of the list
print(len(basket)) 
#list reverse
basket.reverse() #1st reverse -  inplace
print(basket[::-1]) #2nd reverse - list slicing - creates copy
print(basket) #1st reverse

#range
basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(list(range(1,101))) #1-100


#.join str method

# sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
# print(new_sentence)


new_sentence = " ".join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)

# EXERCISE  Common Lists Patterns

#fix this code so that it prints a sorted list of all of our friends (alphabetical).
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
# new_friend = ['Stanley']
# print(friends.sort() + new_friend)


#Option1
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.append('Stanley')
friends.sort()
print(friends)

#Option2
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']
friends.extend(new_friend)
print(sorted(friends))


#LIST UNPACKING

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

# NONE
None
#special data type - absence of value

weapons = None
print(weapons)