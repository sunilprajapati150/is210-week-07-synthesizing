#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a good docstring"""

import authentication
import getpass



def login(username,maxattempts = 3):

    count = False
    attempts = 1
    
    start = 'Please Enter the password: '
    wrongpassword = 'Password Incorrect. {0} attempts remaining. '

    while attempts <= maxattempts:
        
        passauth = getpass.getpass(start)
        
        output = authentication.authenticate(username,passauth)
        
        if output:
            
            count = True
            break
        
        else:
        
            print wrongpassword.format(maxattempts - attempts)
            attempts += 1
            
    return count
