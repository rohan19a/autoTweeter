from em import send_email_gmail
import pandas as pd
from scrape import is_updated, archive_all

def update(twtHandle, email):
    Tweets = archive_all(twtHandle)
    print(Tweets['tweet'])
    message = ""
    for x in Tweets['tweet']:
        message += x + "\n"
    send_email_gmail('New Tweet from ' + twtHandle, message, [email])

def main():
    update("arya_amsha", 'tweetupdaterbot@gmail.com')

if __name__ == "__main__":
    main()