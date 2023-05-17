from ctypes import sizeof
import itertools
from math import floor
import random
import os
import re
from team import Team


def round_robin(team_list, num_of_days, total_matches, schedule_to_be_saved):
    for i in range(1, num_of_days+1):
        header = '-----Day',i,'line up-----'
        schedule_to_be_saved.append(header)
        schedule_to_be_saved.append('\n')
        print('-----Day',i,'line up-----')
        for j in range(int(total_matches/num_of_days)):
            # Choose a random tuple from list of matches
            match = random.choice(team_list)
            # Display first team in tuple
            cur_match = '' + str(match) + '\n'
            schedule_to_be_saved.append(cur_match)
            print(match)  
            # Update list  
            team_list.remove(match)

        for i in range(len(schedule_to_be_saved)):
            print(i)
        #print('This is a test #1: ' + schedule_to_be_saved)
        return schedule_to_be_saved