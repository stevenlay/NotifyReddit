import praw
import pdb
import re
import os

#reddit instance
reddit= praw.Reddit("notifier")

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
messageToSend += subreddits.display_name + "\n"
print(messageToSend)
for submission in subreddits.hot(limit=10):
    titleAndLink = (submission.title + "Link: %s \n" % (submission.shortlink))
    print(titleAndLink)
    messageToSend += titleAndLink


#---------------------------------------------------------------------#
#2: Look at all the subscribed subreddit with:
#subscribed = list(reddit.user.subreddits(limit=None))

#iterate through all the subscribed subreddits
#for subreddit  in subscribed:
 #   print(subreddit.title)
  #  messageToSend += subreddit.title
    
    #get the top 50 submissions in the subreddit
   # for submission in subreddit.hot(limit=1):
        #if submission isn't already sent to the user, add it
    #    if submission.id not in upvoted_posts:
     #       submission_ref= (submission.title + " Link: %s" %(submission.shortlink))  
      #      dashes = ("----------------------------------------- \n")
       #     print(submission_ref)
        #    print(dashes)
         #   upvoted_posts.append(submission_ref)
          #  upvoted_posts.append(dashes)

with open("upvoted_posts.txt", "w") as file:
    file.write(messageToSend)

#send the links to reddit user
reddit.redditor('ENTER USERNAME HERE').message("Highlights", messageToSend)
            
        
