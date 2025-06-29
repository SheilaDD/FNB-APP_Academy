#Loops control statements

#fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

#for fruit in fruits:
    #if fruit == 'banana':
        #continue # Skip the rest of the loop for 'banana'
    #print(fruit)

#for fruit in fruits:
    #if fruit == 'kiwi':
        #break # Exit the loop when 'kiwi' is encountered
    #print(fruit)

# Using the pass statement to do nothing in the loop
#for fruit in fruits:
    #if fruit == 'cherry':
        #pass # Do nothing for 'cherry'
    #print(fruit)  

# Using the range function to generate a sequence of numbers
#for i in range(5):  
    #print(i)  # Output: 0, 1, 2, 3, 4 
# Using the range function with a start and end value
#for i in range(2, 10):  
    #print(i)  # Output: 2, 3, 4, 5, 6, 7, 8, 9
# Using the range function with a start, end, and step value
#for i in range(1, 10, 2):  
    #print(i)  # Output: 1, 3, 5, 7, 9   
# Using the range function to iterate through a list of numbers

count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break  # Exit the loop when count is 5
    