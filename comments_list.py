#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:35:37 2020

@author: matan
"""

'''comments = []

with open('addition_comments.txt') as file:
    line = file.readline()
    while line:
        comments.append(line)
        line = file.readline()



counter = 0
for c in comments:
    comments[counter] = comments[counter][:-1]
    counter +=1
    
print(comments)'''

def get_comments_list():

    comments = ['clean', 'enthusiastic', 'heartening', 'talented', 
             'accommodating', 'clever', 'helpful', 'meritorious', 
             'refined', 'temperate', 'accomplished', 'commendable', 
             'excellent', 'high-class', 'moral', 'reliable', 'terrific',
             'adept', 'compassionate', 'exceptional', 'neat', 'lit💥', 
             'remarkable', 'tidy', 'admirable', 'composed', 'exemplary',
             'honorable', 'noble', 'resilient', 'top quality', 'exquisite',
             'obliging\t', 'tremendous', 'amazing', 'extraordinary', 'humble', 
             'observant', 'respect\t', 'appealing', 'fabulous', 'important', 
             'resplendent\t', 'correct', 'faithful', 'impressive', 'organized',
             'attractive', 'courageous', 'fantastic', 'incisive', 'outstanding',
             'robust', 'unbeatable', 'awesome', 'courteous', 'fascinating', 
             'incredible', 'peaceful', 'beautiful', 'dazzling', 'fine', 'super', 
             'superb', 'insane!', 'perceptive', 'sensational\t', 'benevolent', 
             'decent', 'first-class', 'insightful', 'perfect', 'unparalleled', 
             'delightful', 'fortitudinous', 'inspiring', 'pleasant', 'serene', 
             'upbeat', 'breathtaking', 'dependable', 'gallant', 'intelligent',
             'pleasing', 'sharp', 'valiant', 'bright', 'devoted', 'generous', 
             'shining', 'valuable', 'brilliant', 'gentle', 'Wow','judicious', 
             'stay positive', 'shrewd', 'vigilant', 'bubbly', 'discerning', 
             'gifted', 'praiseworthy', 'smart', 'vigorous', 'buoyant', 
             'disciplined', 'kindly', 'precious', 'sparkling', 'virtuous',
             'calm', 'wonderful', 'elegant', 'gleaming', 'laudable', 'priceless', 
             'spectacular', 'well mannered', 'well done', 'unbelievable', 'awesome']


    additions = ['!!', '😻', '😱', '😮', '😎', '🤗', '😝', '😋', '🤩', '😊',
             '!!!', '😁', '😄', '😃', '😏', '🤯', '🥳', '😺', '💛', '💥', 
             '💯', '👌', '✌', '🤙', '☝', '👍', '👏', '💪']
    
    return [comments,additions]

if __name__ == "__main__":
    print(get_comments_list())