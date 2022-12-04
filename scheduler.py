from imports import *

num_of_teams = 4#int(input ('How many teams?: '))
num_of_days = 2#int(input ('How many days?: '))
num_of_fields = 1#int(input ('How many fields?: '))
total_matches = int(((num_of_teams/2) * (num_of_teams-1)))
list_of_teams =[]
schedule_to_be_saved = str()

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
    schedule_to_be_saved = ''
    round_robin(original_list.copy(), num_of_days, total_matches, schedule_to_be_saved)
    cont = input('Would you like to generate a new schedule? (Y/N): ')
    if cont.upper() == 'N':
        break
    os.system('cls')

file_name = input('Give the schedule a name: ')

if re.search('.txt$', file_name) == None:
    file_name = file_name + '.txt'

oFile = open(file_name, 'w')

oFile.close()






