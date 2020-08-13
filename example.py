#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:30:46 2020

@author: matan
"""
import instabot_main as instabot
import users
import sleep



bot = instabot.InstagramBot('<username>', '<password>')
bot.login()

#Example for running of list of hashtags:

hashtags = ['seoul','busan','gwangju','daegu']

for tag in hashtags:
        
    bot.run(tag, 
            location = False, 
            follow_enable = True,
            num_pics = 100, 
            like_enable = True, 
            break_after = 50,
            break_len = 30, 
            max_follow = 20,
            comment_enable = True
           )
    
    sleep.sleep_in_min(10)
      


# Running by location:
bot.run('12345678', 
	    location = True,   # SET TO TRUE!
	    follow_enable = True,
	    num_pics = 100, 
	    like_enable = True, 
	    break_after = 50,
	    break_len = 30, 
	    max_follow = 20,
	    comment_enable = True
	   )

# Example of getting a list of not following back users
'''bot.not_follows_back('follows_users_20200728_1905.csv',
                     'followed_by_users_20200728_1905.csv',
                     export_csv = True)'''


# not following back using instaloader
#bot.not_follows_back(instaloader = True)


# Example for removing from a file
#bot.remove_follow('08-01_03:12:26.csv',by_one = False)


# Example of follow the follower list of certain user
#bot.follow_from_user('<wanted_user>',20)


# Example of removing following who followed after certain user (not uinclude)
#bot.remove_prev_follow('<wanted_user>',20)
	
	
# to close the browser
bot.closeBrowser()
