# Programmer Name: Francisco Ramirez
# Date: January 26th, 2020
# Python II
# HW2: Bonus (World Champions)

#Global variable
file = "WorldSeriesWinners.txt"

def main():
    #Variable Declarations
    teams = file_read()
    team_list(teams)
    print()
    team_select(teams)

def title():
    print("Francisco Ramirez")
    print("January 26th, 2020\nPython II",
          "Hw: World Series Champions")

def team_list(teams):
    
    #Creates a list with each teams name only once
    updated_teams =[]
    for name in teams:
        if name not in updated_teams:
            updated_teams.append(name)

    #Sorts the team names alphabetically
    #Prints the updated list
    updated_teams.sort(key = str.lower)
    for name in updated_teams:
        print(updated_teams.index(name), ' - ', name, sep='')
    
def team_select(teams):
    count = 0

    #Compares user input to string list.
    user_input = input("Enter the name of a baseball team to learn how many times they won\nWorld Series: ")
    for name in teams:
        if name.upper() == user_input.upper():
            count += 1
    print()
    print("The",user_input,"has won the World Series",count,"times")

def file_read():
    #Reads file 
    file_object = open(file,'r')
    team = file_object.readlines()

    #Converts list strings into ints
    for i in range(len(team)):
        team[i] = (team[i].rstrip('\n'))

    #Closes file
    file_object.close()
    
    #Returns completed list
    return(team)

#Calls main
main()
