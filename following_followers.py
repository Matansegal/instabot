#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 03:33:26 2020

@author: matan
"""

import instaloader as il
'''
    documentation from:
    https://instaloader.github.io/as-module.html#instagram-structures
'''

def get_list( user, password, opt = "", wanted_user = ""):
    '''

    Parameters
    ----------
    user, password : of the username
    opt : 'following' or 'follows'

    wanted_user : user to get the list from
                    default as given user
    Returns 
    -------
    list of usernames

    '''
    
    if(opt == ""):
        print('Please enter following or follows')
        return
    
    if(wanted_user == ""):
        wanted_user = user
    
    L = il.Instaloader()
    
    L.login(user, password) 
    
    profile = il.Profile.from_username(L.context, wanted_user)
    
    '''
        get_followers()
        get_followees() = following
    '''
    
    return_list = []
    
    if(opt == 'following'):
        for followee in profile.get_followees():
            return_list.append(followee.username)
        print('done following')
    
    elif(opt == 'follows'):
        for follower in profile.get_followers():
            return_list.append(follower.username)
        print('done followers')
        
    return return_list
    
    '''difference = [item for item in following if item not in followers]
        
    print('differnce count:', len(difference))
    print(difference)'''
