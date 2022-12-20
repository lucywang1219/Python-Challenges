"""
Our aim is to write a collection of subroutines that will be used to extract and display relevant information from this text file. We will then display a menu of options for the user to select what goals analysis to perform. Here will be the options from our menu:

A: Total number of goals scored by a given country
B: Total number of goals scored by a given player
C: List the name of all the players who scored for a given country
D: Total number of goals by all countries
E: Total number of goals scored during the first half (45 minutes)
F: Total number of goals scored during the second half (45 minutes to 90 minutes)
G: Total number of goals scored during extra time (after 90 minutes of play)
X: Exit?
"""
import time


def scrap_data():
    file = open("goals.txt", "r")
    goal_list = list() 
    for line in file:
        data = line.split(';')
        name = data[0]
        country = data[1]
        minutes = int(data[2])
        goal_list.append((name, country, minutes))
    return goal_list


# 2018 Football World Cup Challenge -  www.101computing.net/2018-world-cup-goals-analysis/


def menu():
    print("*********************************************")
    print("*                                           *")
    print("*      2018 World Cup: Goals Analysis       *")
    print("*                                           *")
    print("*********************************************")
    print("")
    print("> Select an option:")
    print("       > A: Total number of goals scored by a given country")
    print("       > B: Total number of goals scored by a given player")
    print("       > C: List the name of all the players who scored for a given country")
    print("       > D: Total number of goals by all countries")
    print("       > E: Total number of goals scored during the first half (45 minutes)")
    print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
    print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
    print("       > X: Exit")
    print("")

# A Procedure to count the number of goals scored by a given country during the 2018 world cup


def goalsPerCountry():
    userInput = input("> Enter country:").title()

    file = open("goals.txt", "r")
    goals = 0
    for line in file:
        data = line.split(";")
        player = data[0]
        country = data[1]
        minutes = int(data[2])
    if country == userInput:
        goals = goals + 1
    file.close()
    print("\n> " + userInput + " scored " +
          str(goals) + " goal(s) in the 2018 world cup.")


# B Total number of goals scored by a given player
def count_goals_player(goal_list):
    userinput = input('> Enter a player: ').title()
    goals = 0 
    for goal in goal_list: 
        if goal[0] == userinput: 
            goals += 1  
    print(f"\n> {userinput} scored {goals} goal(s) in the 2018 World Cup.")

# C List the name of all the players who scored for a given country
def find_players_by_country(goal_list): 
    userinput = input('> Enter a country: ').title() 
    players = []
    for goal in goal_list: 
        if goal[1] == userinput: 
            if goal[0] not in players: 
                players.append(goal[0])
            else: 
                pass
    print(f"\n> {players} scored for {userinput} in the 2018 World Cup.")

# D Total number of goals by all countries
def count_total_goals(goal_list): 
    num_goals = len(goal_list)
    print(f"\n> There were total of {num_goals} scored in the 2018 World Cup.")

# E Total number of goals scored during the first half (45 minutes)
def count_first_half(goal_list): 
    number_goals = 0
    for goal in goal_list: 
        if goal[2] <= 45: 
            number_goals += 1 
    print(f"\n> {number_goals} were scored during the first half of the games in the 2018 Wrold Cup.")

# F Total number of goals scored during the second half (45 minutes to 90 minutes)
def count_second_half(goal_list): 
    number_goals = 0
    for goal in goal_list: 
        if 45 < goal[2] <= 90: 
            number_goals += 1 
    print(f"\n> {number_goals} were scored during the second half of the games in the 2018 Wrold Cup.")

# G Total number of goals scored during extra time (after 90 minutes of play)
def count_goals_extra_time(goal_list): 
    number_goals = 0
    for goal in goal_list: 
        if goal[2] > 90: 
            number_goals += 1 
    print(f"\n> {number_goals} were scored during the extra time of the games in the 2018 Wrold Cup.")


##################### Main Program Starts Here ##############################
def main():
    goal_list =scrap_data()
    userChoice = ""
    while userChoice != "X":
        menu()
        userChoice = input(
            "> Select an option from the menu (A to G) or X to exit:").upper()
        if userChoice == "A":
            goalsPerCountry()
        elif userChoice == "B":
            count_goals_player(goal_list)
        elif userChoice == "C":
            find_players_by_country(goal_list)
        elif userChoice == "D": 
            count_total_goals(goal_list)
        elif userChoice == "E": 
            count_first_half(goal_list)
        elif userChoice == "F": 
            count_second_half(goal_list)
        elif userChoice == "G": 
            count_goals_extra_time(goal_list)
        else: 
            pass 
        time.sleep(3)
        print("\n\n\n")
    print("Good bye!")

if __name__ == '__main__':
    main()
