from ctypes import sizeof
import itertools
from math import floor
import random
import os
from team import Team


def round_robin(team_list, num_of_days, total_matches):
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