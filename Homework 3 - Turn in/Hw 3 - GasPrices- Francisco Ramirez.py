# Programmer Name: Francisco Ramirez
# Date: February 17th, 2020
# Python II
# HW3: The Gas Prices

'''
Write a program that reads the file's contents and formats as shown:
    DD-MM-YYYY:Price
    Ex: 11-01-1998:9.191
'''

#Global variable
file = "GasPrices.txt"

def main():
    #Format
    title()

    #Reads file
    prices = file_read()
    #print(prices)
    print()
    array(prices)


    
def array(prices):
    list1 = prices.split('\n')
    for x in range(len(list1)-1):
        week = list1[x]
        avg_week = week.split('-')
        print(avg_week[1],avg_week[0],avg_week[2],sep='-')

def file_read():
    #Reads file 
    file_object = open(file,'r')
    prices = file_object.read()

    #Closes file
    file_object.close()
    
    #Returns completed list
    return(prices)

def title():
    print("Francisco Ramirez")
    print("February 17th, 2020\nPython II",
          "Hw3: The Gas Prices")

#Calls main
main()
