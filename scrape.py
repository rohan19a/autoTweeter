import twint
import difflib





def is_updated(previous, c):
    twint.run.Search(c)

    ll = twint.storage.panda.Tweets_df

    with open('new.txt', 'w') as s:
        for xx in ll:
            s.write(xx)
            s.write('\n')

    clearScreen()
    
    diff = differences(previous, ll)
    print(diff)
    

def differences(x, y):

    cases= [x, y]

    for a,b in cases:     
        print('{} => {}'.format(a,b))  
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Delete "{}" from position {}'.format(s[-1],i))
            elif s[0]=='+':
                print(u'Add "{}" to position {}'.format(s[-1],i))    
        print()



def clearScreen():
    for x in range(10):
        print(" ")



def main():
    c = twint.Config()
    c.Limit = 10
    c.Username = "arya_amsha"
    c.Pandas = True

    twint.run.Search(c)

    Tweets_df = twint.storage.panda.Tweets_df
    clearScreen()
    Tweets_df.sample(5)
    Tweets_df.to_csv('tweets.csv', index=False)

    print(Tweets_df.id)

    l = Tweets_df['tweet']

    with open('info.txt', 'w') as f:
        for x in l:
            f.write(x)
            f.write('\n')
    print(l)

    

if __name__ == "__main__":
    main()