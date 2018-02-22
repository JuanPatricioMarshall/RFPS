

    # Reddit random top post message scrapper

import praw
import random


def getRandomComment():
    RANDOM_LOWER = 0
    RANDOM_UPPER = 60
    APPROX = 24

    TWEET_LENGTH = 140

    RANDOM_HIT = 30

    reddit = praw.Reddit(client_id='hn6YR788bXUOXg',
                         client_secret='KeH_-kol_a0xpreboMq2Toqfz2o',
                         user_agent='my user agent')

    subreddit = reddit.subreddit("leagueoflegends")
    subreddit = reddit.subreddit("all")



    #for comment in reddit.subreddit('leagueoflegends').stream.comments():
    #    print(comment)
    #    submission = reddit.submission(id=comment)
    #    print()

    for submission in subreddit.top(limit=200):
#        print("Title: ", submission.title)
#        print("Text: ", submission.selftext)
#        print("Score: ", submission.score)
#        print("submission: ", submission)
#        print("---------------------------------\n")
        random_number = random.randint(RANDOM_LOWER + APPROX, RANDOM_UPPER - APPROX)
        if random_number != RANDOM_HIT :
            continue
        from praw.models import MoreComments
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
#            print(top_level_comment)
#            print(top_level_comment.body)
            random_number = random.randint(RANDOM_LOWER, RANDOM_UPPER)
            if random_number == RANDOM_HIT and len(top_level_comment.body) < TWEET_LENGTH:
                return top_level_comment.body
#        for top_level_comment in submission.comments:
#            if isinstance(top_level_comment, MoreComments):
#                continue
#            print(top_level_comment)
#            print(top_level_comment.body)
#            return top_level_comment.body


comment = getRandomComment()

#print("............\n")
#print("............\n")
#print("............\n")

#print(comment)