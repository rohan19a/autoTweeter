import twint

c = twint.Config()
c.Limit = 20
c.Username = "arya_amsha"
c.Pandas = True

twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df