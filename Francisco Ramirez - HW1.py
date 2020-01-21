#Programmer: Francisco Ramirez
#Date: January 18, 2020
#Python II: Homework 1 (Rainfall Statistics)

#Global Variables
MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
         'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def main():
    #Variable Declarations
    count = 0
    month_rain = [0.0]*12
    
    #Calls Display (Title Method)
    title()
    
    #User Input
    print("Input the amount of rainfall for each month.")
    for months in MONTH:
        print(months,end=": ")
        month_rain[count] = float(input())
        count+=1
    print()
    
    #Calls Rainfall MethodS
    details_rainfall(month_rain)
    print()
    summary_rainfall(month_rain)
    print()

#-------------------------------------------------------------------
#-------------------------METHODS-----------------------------------
#-------------------------------------------------------------------

def title():
    print("Francisco Ramirez")
    print("January 18, 2020")
    print("Homework 1: Rainfall Statistics\n")

def details_rainfall(rain):
    print("\t\tDetails of Rainfall")
    print("--------------------------------------------")
    
    for count in range(len(MONTH)):
        print(MONTH[count],':', sep='', end=' ')
        print(rain[count], "inches")


def summary_rainfall(rain):
    print("\t\tSummary of Rainfall")
    print("--------------------------------------------")
    print("Total rainfall:", "%.2f"%(sum(rain)))
    print("Average rainfall:", "%.2f"%(sum(rain)/len(rain)))
    print("Highest rainfall:", "%.2f"%(max(rain)))
    print("The month of highest rainfall:", MONTH[rain.index(max(rain))])

#Calls Main Method
main()
