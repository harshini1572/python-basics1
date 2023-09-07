#!/usr/bin/env python
# coding: utf-8

# PYTHON BASED VARIABLE

# 1. Declare two variables, x and y, and assign them integer values. Swap the values of these variables without using any temporary variable.

# In[1]:


#taking user input
x=int(input())
y=int(input())
#function to swap
def swap_variables(x,y):
    print(f"Before swap x: {x} and y: {y}")
    x,y = y, x
    print(f"After swap x: {x} and y: {y}")

swap_variables(x,y)


# 2. Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.
# 
# 

# In[2]:


#Taking the length and width of rectangle from the user
length=float(input("Enter width of rectangle: "))
width=float(input("Enter width of rectangle: "))

#calculating the area of rectangle
area=length*width

#print the area
print("area of rectangle is:",area)


# 3. Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.

# In[6]:


#Taking  temperature in celsius as user input 
celsius=float(input("Enter temperature in celsius "))
#Converting celsius into farenheit
farenheit_temperature = (celsius * 9/5) + 32
#print the result 
print(f"{celsius}is equal to {farenheit_temperature} Farenheit")


# STRING BASED QUESTIONS
# 

# 1. Write a Python program that takes a string as input and prints the length of the string

# In[9]:


#Taking input string from user
String=str(input("Enter a string"))
#calculating the length of string
length=len(String)
#Print the length of string
print("Length of string is: ",length)


# 2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
# 

# In[12]:


#Taking the input sentence from user
Sentence=str(input("Enter a sentence"))
#Writing a function to count thje vowels
def vowel_count(Sentence):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in Sentence:
        if alphabet in vowel:
            count=count+1
    #print the number the vowels
    print("No.of vowels :",count)
#return function
vowel_count(Sentence)


# 3. Given a string, reverse the order of characters using string slicing and print the reversed string.

# In[13]:


#Taking input from user
input_string=input("Enter a string:")
#REversing the string
reversed_string=input_string[::-1]
#Print the reversed string
print("The reversed string is:",reversed_string)


# 4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).
# 

# In[18]:


#Taking input string from user
input_string = input("Enter a string: ")

#Remove spaces and convert the input string to lowercase
cleaned_string = input_string.replace(" ", "").lower()

#Reverse the cleaned string using slicing
reversed_string = cleaned_string[::-1]

#Compare the cleaned string with its reverse to check for palindrome
if cleaned_string == reversed_string:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")


# 5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.

# In[23]:


#Take input string
Input_string=" wa t er "
#Remove spaces
modified_string=Input_string.replace(" ","")
#Print the modified string 
print(modified_string)


# In[ ]:




