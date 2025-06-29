#list

fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits[1] = "kiwi"

print(fruits)  # Accessing the first element

fruits.append("orange")  # Adding an element to the end of the list
print(fruits)

fruits.insert(1, "mango")  # Inserting an element at a specific position
print(fruits)

fruits.remove("cherry")  # Removing a specific element
print(fruits)

fruits.pop()  # Removing the last element
print(fruits)

fruits.sort() # Sorting the list
print(fruits)

fruits.reverse()  # Reversing the list
print(fruits)

# Tuple
fruits_tuple = ('apple', 'banana', 'cherry')
print(fruits_tuple)
# Accessing elements in a tuple
print(fruits_tuple[0]) 
print(fruits_tuple[2]) # Accessing the first element
# Tuples are immutable, so we cannot change their elements
# fruits_tuple[1] = "kiwi"  # This will raise an error
# Converting a tuple to a list
fruits_list = list(fruits_tuple)
print(fruits_list)


# set
fruits_set = {'apple', 'banana', 'cherry'}
print(fruits_set) 

fruits_set.add('orange')  # Adding an element to the set
print(fruits_set)



