import itertools
from math import floor
import random
from team import Team

num_of_teams = 4#int(input ('How many teams?: '))
num_of_days = 2#int(input ('How many days?: '))
num_of_fields = 1#int(input ('How many fields?: '))
total_matches = int(((num_of_teams/2) * (num_of_teams-1)))
list_of_teams =[]

# Create generic team names based off of # of teams 
for i in range(num_of_teams):
    team_num = i+1
    team_num = str(team_num)
    list_of_teams.append(Team('Team'+team_num))

print('All Registered Teams')
for team in list_of_teams: 
    print('*'+team.name)


# Build all teams opponents list and output list
for team in list_of_teams:
    team.create_ops(list_of_teams)
    print(team.name+"'s","Oppenent List:", team.opponents)


# Create list of team numbers
team_numbers_list = list(range(1, num_of_teams+1))

# Get all combos of team match ups 
test_list = list(itertools.combinations(team_numbers_list, 2))
print(test_list)

# Display matche line ups
for i in range(1, num_of_days+1):  
    prev = '-1'  
    print('-----Day',i,'line up-----')
    for j in range(int(total_matches/num_of_days)):
        match = random.choice(test_list)
        print(match[0])
        print(prev)
        while match[0] == prev:
            print('entering while loop')
            match = random.choice(test_list)
        test_list.remove(match)        
        prev = match
        print(match)
        print(prev)










# print('-----Day 1 line up-----')
# for i in range(int(total_matches/num_of_days)):
#     match = random.choice(test_list)
#     test_list.remove(match)
#     print(match)
# print('-----Day 2 line up-----')
# for i in range(int(total_matches/num_of_days)):
#     match = random.choice(test_list)
#     test_list.remove(match)
#     print(match)
