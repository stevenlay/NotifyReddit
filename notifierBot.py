import praw
import pdb
import re
import os

#reddit instance
reddit= praw.Reddit("notifier")
limit = 10
counter = 0
#if no file exists, initialize it
if not os.path.isfile("upvoted_posts.txt"):
    upvoted_posts = []
#if it does exist, then read it and split it by id
else:
    with open("upvoted_posts.txt", "r") as file:
        upvoted_posts = file.read()
        upvoted_posts = upvoted_posts.split("\n")
        upvoted_posts = list(filter(None, upvoted_posts))

messageToSend = ""
#1: Pick the subreddits to look at with: ("subreddit1 + subreddit2... + subredditn")
subreddits = reddit.subreddit("learnprogramming+aww")
messageToSend += subreddits.display_name + "\n \n"
print(messageToSend)
for submission in subreddits.hot(limit=None):
    if counter >= limit:
        break
    if submission.id not in upvoted_posts:
        titleAndLink = (submission.title + "\t%s \n \n" % (submission.shortlink))
        print(titleAndLink)
        messageToSend += titleAndLink
        upvoted_posts.append(submission.id)
        counter += 1
            

#---------------------------------------------------------------------#
#2: Look at all the subscribed subreddit with:
#subscribed = list(reddit.user.subreddits(limit=None))

#iterate through all the subscribed subreddits
#for subreddit  in subscribed:
 #   print(subreddit.title)
  #  messageToSend += subreddit.name + "\n \n"
    
    #get the top submission in the subreddit
    #for submission in subreddit.hot(limit=1):
        #if counter >= limit:
            #break
        #if submission.id not in upvoted_posts:
            #titleAndLink= (submission.title + "\t%s \n \n" %(submission.shortlink))  
            #print(titleAndLink)
            #messageToSend += titleAndLink
            #upvoted_posts.append(submission.id)
            #counter += 1

#add new ids to the txt document for future filtering
with open("upvoted_posts.txt", "w") as file:
    for id in upvoted_posts:
        file.write(id + "\n")

#send the links to reddit user
reddit.redditor('ENTER USERNAME HERE').message("Highlights", messageToSend)
            
        
