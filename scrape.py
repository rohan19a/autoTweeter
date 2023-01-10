import twint
import difflib
import pandas as pd

def archive_all(user, c):
    #adds all of a users tweet to a pandas dataframe
    c.Username = user
    c.Pandas = True
    twint.run.Search(c)

    Tweets_df = twint.storage.panda.Tweets_df

    print(Tweets_df['tweet'])

def is_updated(previousTweets_df, c):
    twint.run.Search(c)

    Tweets_df = twint.storage.panda.Tweets_df

    #add a line called "hello" to Tweets_df['tweets']

    Tweets_df.insert()

    if previousTweets_df.equals(Tweets_df):
        return False
    else:
        return previousTweets_df['tweet'] - Tweets_df['tweet']

def clearScreen():
    for x in range(10):
        print(" ")

def main():
    c = twint.Config()
    c.Limit = 10
    c.Username = "arya_amsha"
    c.Pandas = True

    twint.run.Search(c)

    archive_all("arya_amsha", c)
    
    Tweets_df = twint.storage.panda.Tweets_df
    clearScreen()
    Tweets_df.to_csv('tweets.csv', index=False)

    dif = is_updated(Tweets_df, c)
    clearScreen()

    if dif == False:
        return False
    else:
        print(dif)



if __name__ == "__main__":
    main()
