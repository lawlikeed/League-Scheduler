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

# Creat opponent list
team1_op_list = list_of_teams[0]
print('\n'+list_of_teams[0].name+'\n')
team1_op_list.create_ops(list_of_teams)

print(type(team1_op_list))
print(type(team1_op_list.opponents))
print(type(team1_op_list.opponents[0]))
for i in list_of_teams:
    print(i.name)

for i in team1_op_list.opponents:
    print('Team1 Opponent List: '+i)

for i in range(team1_op_list.opponents):
    print(i.name)









# Output the list of opponents for each team 
# for i in list_of_teams: 
#     print(i.name+"'s opponents: ")
#     for j in list_of_teams: 
        
#         pass