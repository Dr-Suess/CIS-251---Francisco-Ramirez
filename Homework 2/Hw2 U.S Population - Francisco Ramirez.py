# Programmer Name: Francisco Ramirez
# Date: January 26th, 2020
# Python II
# HW2: U.S. Population

#Global Variable
file = "USPopulation.txt"
year = 1950

def main():
    #runs methods
    title()
    print()
    yearly_pop = file_io()
    pops_val(yearly_pop)
    print()
    #matrix(yearly_pop)
    
def title():
    print("Francisco Ramirez")
    print("January 26th, 2020\nPython II",
          "Hw: U.S. Population")

def file_io():
    #Reads file 
    file_object = open(file,'r')
    yearly_pop = file_object.readlines()

    #Converts list strings into ints
    for i in range(len(yearly_pop)):
        yearly_pop[i] = int(yearly_pop[i])

    #Closes file
    file_object.close()
    
    #Returns completed list
    return(yearly_pop)
    
def pops_val(yearly_pop):
    avg_pop = sum(yearly_pop)/len(yearly_pop)
    max_pop = max(yearly_pop)
    min_pop = min(yearly_pop)

    print("The average annual change in population during the time period:", format(avg_pop, '.2f'),
          "\nThe year with the greatest increase in population is:", yearly_pop.index(max_pop) + year,
          "\nThe year with the greatest increase in population is:", yearly_pop.index(min_pop) + year)
    
def matrix(yearly_pop):
    print("Population values:")
    for i in range(len(yearly_pop)):
            print(yearly_pop[i],'\t', end='')
            if (i % 5 == 0):
                print()
                
main()

'''
The average annual change in population during the time period.
The year with the greatest increase in population during the time period.
The year with the smallest increase in population during the time period.
'''
