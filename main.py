//tool that you sign up for and will automaatically send you updates on tweets via email
import stweet as st

def try_search():
    search_tweets_task = st.SearchTweetsTask(all_words='#covid19')
    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
    output_print = st.PrintRawOutput()
    st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                         tweet_raw_data_outputs=[output_print, output_jl_tweets],
                         user_raw_data_outputs=[output_print, output_jl_users]).run()


def try_user_scrap():
    user_task = st.GetUsersTask(['TrueIndology'])
    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()


def try_tweet_by_id_scrap():
    id_task = st.TweetsByIdTask('4472065032')
    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(tweets_by_id_task=id_task,
                        raw_data_outputs=[output_print, output_json]).run()

def return_tweets_from_user(username):
    search_tweets_task = st.SearchTweetsTask(
        from_username=username,
        tweets_limit=1
    )
    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
    output_print = st.PrintRawOutput()

    st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                         tweet_raw_data_outputs=[output_print, output_jl_tweets],
                         user_raw_data_outputs=[output_print, output_jl_users]).run()


_usernames = ['ProtasiewiczJ', 'donaldtuskEPP']


def test_get_user():
    task = st.GetUsersTask(_usernames)
    task_result = st.GetUsersRunner(task, [st.P()]).run()
    assert len(_usernames) == task_result.users_count


if __name__ == '__main__':
    #try_search()
    #try_user_scrap()
    #try_tweet_by_id_scrap()
    """
    l = ['TrueIndology']
    listALl = [[]]
    for x in l:
        return_tweets_from_user(x)
        with open('output_raw_search_tweets.jl', 'r') as f:
            listALl.append(f.readlines())
            for x in range(10):
                print(" ")
            print(len(listALl))"""
    
    test_get_user()



