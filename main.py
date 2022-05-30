# Adapted from leemi's migratereddit.py on GitHub Gist (https://gist.github.com/leemi/e36e8c056aff7990baad28de6e7458d1)

import praw
import settings 	# Reddit account info in settings.py

# Load account info
old_account, new_account = settings.reddit_init()

old_account.login()
new_account.login()

# Remove default subreddits
for sub in new_account.get_my_subreddits(limit=None):
	sub.unsubscribe()

# Copy Subreddits
for sub in old_account.get_my_subreddits(limit=None):
	new_account.get_subreddit(sub.display_name).subscribe()

# Copy Saved
for article in old_account.user.get_saved(sort="new", time="all", limit=None):
	article.reddit_session = new_account
	article.save()