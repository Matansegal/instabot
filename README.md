<p align="center">
  <img src="https://avatars2.githubusercontent.com/u/26087671?s=200&v=4" width="154">
  <h1 align="center">Instabot</h1>
  <p align="center">Tool to automate your social media.<p>

## Table of contents
- [Requirements](#requirements)
- [instabot_main](#InstagramBot)
  * [InstagramBot](#InstagramBot)
  * [Run](#run)
  * [Remove follows](#remove-follows)
  * [List following and follows](#List-following-and-follows)
  * [Not follows back](#Not-follows-back)
  * [Followers from a user](#Followers-from-a-user)
  * [Remove prev follow](#remove-prev-follow)
- [comments_list](#comments_list)
- [sleep](#sleep)
- [Example](#example)
- [Warning](#warning)


## **Requirements**
> - python3
> - Firefox web browser
> - **Selenium** library. to install:
>```elm
> pip install selenium
>```
#### Optional but not required
> - **Instaloader** library. to install:
>```elm
> pip3 install instaloader
>```

## **InstagramBot**
```elm
bot = InstagramBot('<username>',
                   '<password>',
                   browser = 'firefox'
                   )
bot.login()
```

>*bot* is the variable name of the new object, which we send our username and password of our account.
>when we call the *login()* function, it will open Firefox web browser, go to instagram.com, and login to your account.
> - <ins>**username:**</ins> string. Your account username.
> - <ins>**password:**</ins> string. Your account password.
> - <ins>**browser:**</ins> string, default to Firefox (also more recommended). The other option is 'chrome', which works worse.


#### **Run**
```elm
bot.run(hashtag,
        location = False,
        num_pics = 20,
        follow_enable=False,
        like_enable = True,
        comment_enable=False,
        break_after = 60,
        break_len = 45, 
        max_follow = 30
        )
 ```
 > - <ins>**hashtag:**</ins> string. Feffers to the hasgtag you want to load the pictures from e.g. 'dogs'.
 > - <ins>**location:**</ins> default to False. if set to True, it search by location and not hashtag, and the hashtag now should be the **location id** e.g. '6889842'. The location id you can find in the url of the location:
 > <img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/575d3a4cc6979111618ef748/images/5978abee042863033a1b65c4/file-KSrDNXuzvK.png">
 > - <ins>**num_pics:**</ins> int, default to 20. Refferas to the number of pictures you want to like (or comment and follow as well). **If set to more than 60, after 60 photoes, it will sleep for 50 minutes. You can change it, 
 <span style=“color:red;”> but it is not recommended!! </span>** 
 > - <ins>**follow_enable:**</ins> default to False. If set to True, it will also follow all the users you liek their pictures. **Do not follow too many people**. Also, it will creat a ```.csv file``` with all the usernames you followed.
 > - <ins>**like_enable:**</ins> default to True, if set to False, it won't like the pictures.
 > - <ins>**comment_enable:**</ins> default to False. If True, it will commant random comments and additions to the comments from [comments_list](#comments_list)
 > - <ins>**break_after:**</ins> int, default to 60. The run will stop every this number of pictures (if the num_pics is larger). **This should be limited to prevent over liking and temporary ban**.
 > - <ins>**break_len:**</ins> int, default to 45. The length of the break in minutes. **Should be long enough to prevent a temporary ban**.
 > - <ins>**max_follow:**</ins> int, default to 30. Will stop follow users after this number of pictures. **This should br limited to prevent over following and temporary ban**.
 
 
 #### **Remove follows**
 ```elm
 bot.remove_follow(file_name,by_one = True)
```
> Remove following from a given ```.csv file``` 
> - <ins>**by_one:**</ins> default to True. it will ask you each user if you want to remove the follow from. If set to False, it will remove from all the given usernames without asking.


 #### **List following and follows**
 ```elm
 bot.list_following_follows(opt, 
                            user = "", 
                            extract_csv = False, 
                            instaloader = False
                            )
```
> - <ins>**opt:**</ins> string. Has to be 'following' - for following list or 'follows' - for followers list.
> - <ins>**user:**</ins> string. default to given the object username. The wanted username to export its following/followers list.
> - <ins>**extract_csv:**</ins> default to False. If True, will creat a ```.csv file```.
> - <ins>**instaloader:**</ins> default to False. If True, will use instaloader **(need to be installed)**. May take more than 10 minutes.


  #### **Not follows back**
 ```elm
 bot.not_follows_back(following_csv = "", 
                      followers_csv = "",
                      idx = 1,
                      export_csv = False,
                      instaloader = False
                      )
```
> list all the following and followers and check which user appears in following list and not in the followrs list.
> - <ins>**following/followers_csv:**</ins> string. Both default to empty string. If defalt - will call the ```list_following_follows()``` function automatically.
> - <ins>**idx:**</ins> int, default to 1. index of the username in the csv file
> - <ins>**export_csv:**</ins> default to False. If True, export to ```.csv file```.
> - <ins>**instaloader:**</ins> default to False. If True **and both following/followers_csv set to default**, it will call ```list_following_follows()``` function with the instaloader option and create the not follows back list.


  #### **Followers from a user**
   ```elm
 bot.follow_from_user(user,number = 20)
```
> Follow number of people from the list of the follows of certain user.
> - <ins>**user:**</ins> string. The wanted user to follow its follows list.
> - <ins>**number:**</ins> int. default to 20. The number of follows you want to do.


#### **Remove prev follow**
```elm
 bot.remove_prev_follow(from_user, num = 20)
```
> Use a given username as a anchor, which you choose number of users to removed follow from after this person. The following list is chronology, means the lower you scroll down, the earlier you followed this person. By using this function you can remove follow from unwanted users.
> - <ins>**from_user:**</ins> string. The wanted user you use as anchor and remove the number of following after him (not include).
> - <ins>**num:**</ins> int. default to 20. The number of users you want to remove follow from.


## **comments_list**
```elm
import comments_list as cl

cl.get_comments_list()
```

This file contain all the random comments the bot can have. You can change it as much as you want.
It returns a list of two list - the first index(0) is a word and the seconf index is an addition to the word - ! or emojy. When running, the program will choose random word and connect it to random addition to prevent repititve comment **which can lead to temporary ban**.

## **Sleep**
```elm
import sleep

sleep.sleep_in_min(num_min = 50)
```
This file contain the sleep command. I have just one function there ```sleep.sleep_in_min()```, which accept the number of min (default to 50 minutes) it will sleep in the required places. **It is important to set a sleep time so your account will not be banned due to over activity**.



## **Example**

Examples which all are shown in the ```example.py``` file.

First we need to log in to our account. We are using the default browser - Firefox.
```elm
bot = InstagramBot('<username>','<password>')
bot.login()
```

- The first examlple is running the program on a list of 4 hashtags, which all are cities in South Korea.
While running, it will stop every 50 minutes on the same hashtag for 30 minutes and at the end of each iteration for another 10 minutes.
**It is important to set the break often and long enough!!**

```elm
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
```


- The second exmaple is running the program on a given location. The location you can find by the URL as mention [here](#run).
Be aware of setting the tag to a location id as a string and the location enable to **True**.

```elm
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
```



- The third example is getting a list of not following back user to a ```.csv file```. 
We can do it with already exist files we have:

```elm
bot.not_follows_back('follows_users_20200728_1905.csv',
                     'followed_by_users_20200728_1905.csv',
                     export_csv = True)
```

> Which the first file is the user who follows us, and the second is the file of users we are following.
> The second option is using ```instaloader```. We first need to make sure we installed it, as described [here.](#requirements)

```elm
bot.not_follows_back(instaloader = True)
```

> In both cases we will get ```.csv file``` with all the users we are following and they are not following us back.
> **Both of the function will take quite a long time.** The instaloader option might be better.



- The Fourth example is follow number of user from a follows list of a given user:

```elm
bot.follow_from_user('<wanted_user>',20)
```

> This example will follow the first 20 follows of the given wanted user.



- The last example is removing follow of users we followed after given user name. In the example below, we use <wanted_user> as the anchor and the function will remove the first 20 users we followed after <wanted_user>:

```elm
bot.remove_prev_follow('<wanted_user>',20)
```


Lastly, we will close the browser:
```elm
bot.closeBrowser()
```



<h1 align="center"><ins>Warning</ins></h1>
<h3 align="center">Please Note that this is a research project. 
I am by no means responsible for any usage of this tool. 
Use on your own behalf. 
I'm also not responsible if your accounts get banned due to extensive use of this tool.</h3>

<p align="center">© Matan Segal</p>



