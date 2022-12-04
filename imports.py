from ctypes import sizeof
import itertools
from math import floor
import random
import os
import re
from team import Team


def round_robin(team_list, num_of_days, total_matches, schedule_to_be_saved):
    for i in range(1, num_of_days+1):
        schedule_to_be_saved = '-----Day',i,'line up-----\n'
        print('-----Day',i,'line up-----')
        for j in range(int(total_matches/num_of_days)):
            # Choose a random tuple from list of matches
            match = random.choice(team_list)
            # Display first team in tuple
            schedule_to_be_saved = '' + str(match) + '\n'
            print(match)  
            # Update list  
            team_list.remove(match)