from imports import *

def round_robin(team_list):
    for i in range(1, num_of_days+1):  
        prev = ('-1', '-1')  
        print('-----Day',i,'line up-----')
        for j in range(int(total_matches/num_of_days)):
            # Choose a random tuple from list of matches
            match = random.choice(team_list)
            # Display first team in tuple
            print(match)  
            # Update list  
            team_list.remove(match)      
            prev = match



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
print('')

# Build all teams opponents list and output list
for team in list_of_teams:
    team.create_ops(list_of_teams)
    print(team.name+"'s","Oppenent List:", team.opponents)
print('')

# Create list of team numbers
team_numbers_list = list(range(1, num_of_teams+1))

# Get all combos of team match ups 
original_list = list(itertools.combinations(team_numbers_list, 2))
print(original_list , '\n')

# Display matche line ups
while True:
    round_robin(original_list.copy())
    cont = input('Would you like to generate a new schedule? (Y/N): ')
    if cont.upper() == 'N':
        break
    os.system('cls')







