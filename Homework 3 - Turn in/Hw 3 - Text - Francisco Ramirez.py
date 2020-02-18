# Programmer Name: Francisco Ramirez
# Date: February 17th, 2020
# Python II
# HW3: Character Analysis

'''
Write a program that reads the file's contents and determines the folowing:
    Number of uppercase letters in the file.
    Number of lowercase letter in the file.
    Number of digits in the file.
    Number of whitespace characters in the file.
'''


#Global variable
file = "Text.txt"

def main():
    #Format
    title()
    print()

    #Reading file
    mystring = file_read()

    #File contents
    #print(mystring)
    #print()
    
    #Char manipulation
    upper(mystring)
    lower(mystring)
    digit(mystring)
    space(mystring)

    



def space(mystring):
    count_spaces = 0
    for char in mystring:
        if char.isspace():
            count_spaces += 1
    print("Number of space(s) are:", count_spaces)

def digit(mystring):
    count_digit = 0
    for char in mystring:
        if char.isdigit():
            count_digit += 1
    print("Number of digit(s) are:", count_digit)

    
def upper(mystring):
    count_upper = 0
    for char in mystring:
        if char.isupper():
            count_upper += 1
    print("Number of uppercase char(s) are:", count_upper)
       
def lower(mystring):
    count_lower = 0
    for char in mystring:
        if char.islower():
            count_lower += 1
    print("Number of lowercase char(s) are:", count_lower)

def file_read():
    #Reads file 
    file_object = open(file,'r')
    words = file_object.read()

    #Closes file
    file_object.close()
    
    #Returns completed list
    return(words)

def title():
    print("Francisco Ramirez")
    print("February 17th, 2020\nPython II",
          "Hw3: Text")
main()
