#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a good docstring"""

def get_matches(players):
    
'''this function makes list of players and created
unique matchup between players and store them as a list of tuples  '''

    output = []

    for int1, boy1 in enumerate(players):
        
        for int2, boy2 in enumerate(players):
            
            if boy1 is not boy2 and int1 < int2:
                
                output.append((boy1,boy2))
                
            else:
                
                continue
            
    return output
                
