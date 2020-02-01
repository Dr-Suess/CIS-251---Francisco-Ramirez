# Programmer Name: Francisco Ramirez
# Date: January 26th, 2020
# Python II
# HW2: U.S. Population

#Libraries
import matplotlib.pyplot as plt

#Global Variable
file = "1994_Weekly_Gas_Averages.txt"

def main():
    #runs methods
    title()
    print()
    weekly_gas = file_io()
    plot(weekly_gas)
    
def title():
    print("Francisco Ramirez")
    print("January 28th, 2020\nPython II",
          "Hw: Weekly Gas Averages")
    
def plot(weekly_gas):
    #create lists with the X and Y coordinates of each data point.
    x_coords = []
    for x in range (len(weekly_gas)):
        x_coords.append(x)
    y_coords = weekly_gas
    plt.plot(x_coords,y_coords)

    #Add a title and labels
    plt.title("Weekly Gas Prices")
    plt.xlabel("Weeks")
    plt.ylabel("Prices")

    #Display the line graph
    plt.grid(True)
    plt.show()
    
def file_io():
    #Reads file 
    file_object = open(file,'r')
    weekly_gas = file_object.readlines()

    #Converts list strings into floats
    for i in range(len(weekly_gas)):
        weekly_gas[i] = float(weekly_gas[i])

    #Closes file
    file_object.close()
    
    #Returns completed list
    return(weekly_gas)
 
main()

'''
Using matpltlib, write a Python program that reads the contents of the
file then plots the data as either a line graph or a bar chart. Be sure
to display meaninful labels along the X and Y axis, as well as tick marks.
'''
