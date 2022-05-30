import praw

def reddit_init():

    # replace these with your Reddit API info and Reddit account credentials
    old_account = praw.Reddit(
        client_id = "",
        client_secret = "",
        user_agent = "",
        username = "",
        password = "",
    )
    
    new_account = praw.Reddit(
        client_id = "",
        client_secret = "",
        user_agent = "",
        username = "",
        password = "",
    )


    return old_account, new_account