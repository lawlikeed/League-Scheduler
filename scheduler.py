from team import Team

num_of_teams = int(input ('How many teams?: '))
num_of_days = int(input ('How many days?: '))
num_of_fields = int(input ('How many fields?: '))
list_of_teams =[]

# print(type(num_of_teams), '-> ', num_of_teams)
# print(type(num_of_days), '-> ', num_of_days)
# print(type(num_of_days), '-> ', num_of_fields)


# Create generic team names based off of # of teams 
for i in range(num_of_teams):
    team_num = i+1
    team_num = str(team_num)
    list_of_teams.append(Team('Team'+team_num))

print('All Registered Teams')
for team in list_of_teams: 
    print('*'+team.name)


#Build all teams opponents list and output list
for team in list_of_teams:
    team.create_ops(list_of_teams)
    print(team.name+"'s","Oppenent List:", team.opponents)
