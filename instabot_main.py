#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:54:29 2020

@author: matan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from datetime import datetime
import csv
import following_followers as ff
import sys
import sleep
import random
import comments_list as cl



class InstagramBot:

    def __init__(self, username, password, browser = 'firefox'):
        self.username = username
        self.password = password
        if(browser == 'firefox'):
            self.driver = webdriver.Firefox()
        elif( browser == 'chrome'):
            self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        else:
            print('Please enter valid browser: "firefox" or "chrome"')
        
        
        

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(3)


    def run(self, hashtag, location = False, follow_enable = False,
            num_pics = 20, like_enable = True, break_after = 60,
            break_len = 45, max_follow = 30 ,comment_enable = False):
        
        '''
            automation of likes, comment and following
            Gives an option to set hashtag or a location and do the above
            actions with setting minimum number of pictures.
            if follow set to true, it will create a csv file with all the urls of the photos
            the program followed their users and name it date_time.
        '''
        
        driver = self.driver
        # if locaiton set to true, need to give a location id number
        if location:
            driver.get("https://www.instagram.com/explore/locations/" + hashtag + "/")
        else:
            driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        
        if(comment_enable):
            comments = cl.get_comments_list()
        
        #continue while a required photoes number is more than found
        while(len(pic_hrefs) < num_pics + 9):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # for debugging
                # print(pic_hrefs)
            except Exception:
                continue
            

        unique_photos = len(pic_hrefs)
        
        #open a file to keep track of followings
        if(follow_enable):
            name = datetime.now().strftime("%m-%d_%H:%M:%S")
            print('open a new csv file = ',name)
            self.file = open(name + '.csv', "w")
        
        #skip the first 9 pics of the most popular
        counter = 9
        
        driver.get('https://www.instagram.com/matansegall/')
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button').click()
        except Exception:
            print('finish loading, start running')
        
        while(counter < num_pics + 9):
            
            #flush update
            sys.stderr.write(
                '\r%s: %d/%d                           ' % (hashtag, counter - 9, num_pics))
            sys.stderr.flush()
            
            try:
                self.driver.get(pic_hrefs[counter])
            except:
                print("could not find such a url, continue")
                continue
            
            if(follow_enable):
                name = self.follow()
                #update the flush
                if(name != ""):
                    sys.stderr.write(
                        '\r%s: %d/%d  Followed -- %s' % (hashtag, counter - 9, num_pics,name))
                    sys.stderr.flush()
            
            #scroll down
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            if(like_enable):
                #time.sleep(1)
                if(self.like()):
                    sys.stderr.write(
                        '\r%s: %d/%d -- LIKE!                          ' % (hashtag, counter - 9, num_pics))
                    sys.stderr.flush()

            
            if(comment_enable):
                #generate radom comment
                self.comment(random.choice(comments[0])+random.choice(comments[1]))  
                
            unique_photos -= 1
            counter += 1
            
            #Limit of likes and follows
            if(counter - 9 == max_follow):
                follow_enable = False
            if((counter - 9) % break_after == 0):
                sleep.sleep_in_min(break_len)
            
        
        if(follow_enable):
            self.file.close()
            
            
    def like(self):

        try:
            #self.driver.find_element_by_xpath("//section/span/button/div[*[local-name()='svg']/@aria-label='Like']").click()
            # both like and unlike - if the first one does not work
            self.driver.find_element_by_class_name('fr66n').click()
            time.sleep(1)
            return True
            
        except NoSuchElementException:
            print("\nalready liked or could not find")
            return False
        
        except ElementClickInterceptedException:
            #if error message
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[2]').click()
            time.sleep(1)
            try:
                self.driver.find_element_by_class_name('fr66n').click()
                time.sleep(1)
                return True
                
            except NoSuchElementException:
                print("\nalready liked or could not find")
                return False
                
            
    def comment(self,label):
        # try a comment
        try:
            commentArea = self.driver.find_element_by_class_name('Ypffh')
            commentArea.click()
            commentArea = self.driver.find_element_by_class_name('Ypffh')
            commentArea.send_keys(label)
            commentArea.send_keys(Keys.RETURN)
            time.sleep(1)
        except NoSuchElementException:
            print("\ncould not find comment box")
        except ElementClickInterceptedException:
            #if error message
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[2]').click()
            try:
                commentArea = self.driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea = self.driver.find_element_by_class_name('Ypffh')
                commentArea.send_keys(label)
                commentArea.send_keys(Keys.RETURN)
                time.sleep(1)
            except NoSuchElementException:
                print("\ncould not find comment box")
            
            
            
    def follow(self):
        
        name = ""    
        try:
            self.driver.find_element_by_xpath("//button[text()='Follow']").click()
            time.sleep(1)
            #get the user name
            name = self.driver.find_element_by_xpath("//div[@class='e1e1d']").text
            self.file.write(name + '\n')
            
        except NoSuchElementException:
            print("\nalready followed")
        
        except ElementClickInterceptedException:
            #if error message
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[2]').click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//button[text()='Follow']").click()
                time.sleep(1)
                #get the user name
                name = self.driver.find_element_by_xpath("//div[@class='e1e1d']").text
                self.file.write(name + '\n')
                
            except:
                print("\nalready followed")
        
        time.sleep(1)
        return name
            
       
    def remove_follow_csv(self, file_name, by_one = True):
        
        '''
            removes followings from a given csv file.
            remove by username
            Has an option to remove one by one as default
        ''' 

        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)

        # data is a list of lists (list of rows)
        
        
        for name in data:
                
            self.driver.get('https://www.instagram.com/' + name[0] + '/')
            time.sleep(1)
            
            if(by_one):
                toremove = input('To remove press Enter,\nto skip any other key\n')
                if(toremove != ""):
                    continue
            
            try:
                #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button').click()
                time.sleep(1)
                # click on confirm unfollow
                self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                time.sleep(1)
                print("follow removed from",name[0])
                
            except NoSuchElementException:
                # try smaller button:
                try:
                    print('got into second chance')
                    #check first to see if has message button
                    self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button')
                    #follow button
                    self.driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()
                        
                    time.sleep(1)
                    # click on confirm unfollow
                    self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                    time.sleep(1)
                    print("follow removed from",name[0])
                    
                except NoSuchElementException:
                    print("already unfollowed")
            
            
            
    def list_following_follows(self, opt, user = "", 
                               extract_csv = False, instaloader = False):
        
        '''
            opt is to choose followings or followers : "following" / "follows"
            make a list of all the following/ers of a given user
            user default to the username of the object.
            has an option to extract to csv file.
            Can use instaloader, might be faster
        '''
        
        #check for right input
        if(opt not in ['following','follows']):
            print('please enter one of the follwoing options for opt:')
            print('following\nfollows')
            return
        
        # if want to use instaloader
        if(instaloader):
            return ff.get_list(user = self.username,
                               password = self.password,
                               opt = opt, 
                               wanted_user = user)
        
        if(user == ""):
            user = self.username
            
        if(extract_csv):
            name = opt + '_' + user + '_' + datetime.now().strftime("%m-%d_%H:%M") 
            print('open a new csv file = ',name)
            file = open(name + '.csv', "w")
        
        follow_list = []
        
        self.driver.get('https://www.instagram.com/' + user + '/')
        time.sleep(1)
        
        #gets number of followings
        if( opt == 'following'):
            num_followings = int(self.driver.find_element_by_xpath("//a[contains(@href,'following')]/span").text)    
        elif(opt == 'follows'):
            num_followings = int(self.driver.find_element_by_xpath("//ul/li[2]/a/span").text)    
        
        print('num of ' + opt ,num_followings)
        
        #click on following/ers
        # for following we need li[3] and for followers li[2]
        x = '3' if opt == 'following' else '2'
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li['+x+']/a').click()
        time.sleep(2)        
    
        # save scroll box to scroll in it
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
                                                        
        for i in range(1,num_followings+1):
            try:
                text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                
            except NoSuchElementException:
                #scroll down if did not find and try again
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(1)), scroll_box)
                print('scrolled down')
                time.sleep(1)
                
                try:
                    text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                
                #second chance
                except NoSuchElementException:
                    time.sleep(3)
                    try:
                        text = self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                    
                    except NoSuchElementException:
                        time.sleep(10)
                        try:
                            text = self.driver.find_element_by_xpath(
                                '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                        except NoSuchElementException:
                            break
            # add to list
            new_name = text.text.partition('\n')[0]
            follow_list.append(new_name)
            if(extract_csv):
                file.write(new_name + '\n')
        

        print('followings len:',len(follow_list))
        
        if(extract_csv):
            file.close()
            
        #click to close box
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(2)
        
        return follow_list
    
    
    def not_follows_back(self, following_csv = "", 
                         followers_csv = "", idx = 1,
                         export_csv = False, instaloader = False):
        
        '''
            list all the following and followers and check which user 
            appears in following list and not in the followrs list.
            Have an opption for loading from a csv (can get csv files with 
                                                    helper tools for instagram)
            idx : int. index of the username in the csv file
            Option to export to csv file
            option for using instaloafer in the list_following function
        '''
        
        following = []
        follows = []
        difference = []
        

        if(following_csv == "" and followers_csv == ""):
            following = self.list_following_follows(opt = 'following',
                                                    instaloader = instaloader)
            follows = self.list_following_follows(opt = 'follows',
                                                    instaloader = instaloader)
            difference = [item for item in following if item not in follows]
            
        #load from a csv    
        else:
            with open(following_csv, newline='') as f:
                reader = csv.reader(f)
                following = list(reader)
                
            with open(followers_csv, newline='') as f:
                reader = csv.reader(f)
                follows = list(reader)
            
            difference = [item[idx] for item in following if item not in follows]
        
        if(export_csv):
            name = 'not_follows_' + datetime.now().strftime("%m-%d_%H:%M:%S")
            print('open a new csv file = ',name)
            file = open(name + '.csv', "w")
            
            for user in difference:
                file.write(user + '\n')
                
            file.close()
        
        
        #---------------------
        print('\n\ndiffernce count:', len(difference))
        print(difference)
        
        
    def follow_from_user(self,user,number = 20):
        '''
        Follow number of people from the list of the follows of certain user.
        Good to follow user with negative follows - following ratio
        
        TODO: remove follows the same way
        
        Parameters
        ----------
        user : string
            username which you want to look at its followers list.
        number : int, optional
            number of following you want to do. The default is 20.

        Returns
        -------
        None.

        '''
        
        self.driver.get('https://www.instagram.com/' + user + '/')
        time.sleep(1)
        
        name = user + '_' + datetime.now().strftime("%m-%d_%H:%M") 
        print('open a new csv file = ',name)
        file = open(name + '.csv', "w")
        
        #get to follows list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        
        # save scroll box to scroll in it
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        
        for i in range(1,number+1):
            
            sys.stderr.write('                                                  ')
            sys.stderr.write('\r%d/%d' % (i, number))
            sys.stderr.flush()
            
            try:
                time.sleep(1)
                text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                
            except NoSuchElementException:
                #scroll down if did not find and try again
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(1)), scroll_box)
                time.sleep(1)
                
                try:
                    text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                
                #second chance
                except NoSuchElementException:
                    time.sleep(3)
                    try:
                        text = self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                    
                    except NoSuchElementException:
                        time.sleep(10)
                        try:
                            text = self.driver.find_element_by_xpath(
                                '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']')
                        except NoSuchElementException:
                            break
            
            element = text.text.partition('\n')
            #follow/following
            last_elm = element[-1].partition('\n')[-1]
            
            if(last_elm == 'Follow'):
                try:
                    self.driver.find_element_by_css_selector(
                        'li.wo9IH:nth-child('+str(i)+') > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
                    #self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button').click()
                except NoSuchElementException:
                    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(5)),scroll_box)
                    time.sleep(1)
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button').click()
                
                time.sleep(1)
                
                #name of the user
                new_name = text.text.partition('\n')[0]
                
                #update flush
                sys.stderr.write('\r%d/%d -- Followed: %s   ' % (i, number,new_name))
                sys.stderr.flush()
                file.write(new_name + '\n')
                
        file.close()
        
    
    
    def remove_prev_follow(self, from_user, num = 20):
        '''
        Parameters
        ----------
        from_user : string. the user which you want to remove following after
        num : int, number of following to remove

        Returns
        -------
        None.

        '''
        
        self.driver.get('https://www.instagram.com/' + self.username + '/')
        time.sleep(1)
        
        
        #get to following list
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        
        # save scroll box to scroll in it
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        
        cur_name =""
        location = 0
        print('Search for:', from_user)
        
        #scroll down
        for i in range(10):
            #scroll down if did not find and try again
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(1)), scroll_box)
        
        
        # loop to find location of required user
        while(cur_name != from_user):
            
            location += 1 
            try:
                #time.sleep(1)
                text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(location)+']')
                
            except NoSuchElementException:
                #scroll down if did not find and try again
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(1)), scroll_box)
                time.sleep(1)
                
                try:
                    text = self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(location)+']')
                
                #second chance
                except NoSuchElementException:
                    time.sleep(3)
                    try:
                        text = self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(location)+']')
                    
                    except NoSuchElementException:
                        time.sleep(10)
                        try:
                            text = self.driver.find_element_by_xpath(
                                '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(location)+']')
                        except NoSuchElementException:
                            print('could not find or stack')
                            return
            
            
            cur_name = text.text.partition('\n')[0]
        
        print('find ' + from_user + ' at: ' + str(location))
        
        for i in range(location-1,location-1-num,-1):
            try:
                self.driver.find_element_by_css_selector(
                    'li.wo9IH:nth-child('+str(i)+') > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
                # click on confirm unfollow
                self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                time.sleep(1)
            except NoSuchElementException:
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button').click()
                # click on confirm unfollow
                self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                time.sleep(1)
            except ElementClickInterceptedException:
                #if error message
                time.sleep(1)
                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]').click()
                except ElementClickInterceptedException:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]').click()
                try:
                    self.driver.find_element_by_css_selector(
                        'li.wo9IH:nth-child('+str(i)+') > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
                    # click on confirm unfollow
                    self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                    time.sleep(1)
                except:
                    continue
                    
            sys.stderr.write('\r%d/%d removed' % (location - i, num))
            sys.stderr.flush()
                    
            time.sleep(1)
            
        #click to close box
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(2)

    
        
