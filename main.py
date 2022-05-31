# Adapted from leemi's migratereddit.py on GitHub Gist (https://gist.github.com/leemi/e36e8c056aff7990baad28de6e7458d1)
# Old version was in Pythohn 2 and was using an out-dated version of praw

import praw
from prawcore.exceptions import Forbidden
import settings 	# Reddit account info in settings.py
from tqdm import tqdm

# Load account info
old_account, new_account = settings.reddit_init()

# Remove default subreddits
for sub in tqdm(new_account.user.subreddits(limit=None)):
	sub.unsubscribe()

num_subs_old_account = 0

# Copy Subreddits
for sub in tqdm(old_account.user.subreddits(limit=None)):
	num_subs_old_account = num_subs_old_account + 1
	try:
		new_account.subreddit(sub.display_name).subscribe()
	except Forbidden: 
		# Usually occurs for user accounts that the account is following (u_username)
		print("\nManually subscribe - automatic subscription failed: " + sub.display_name)

# Sanity check
num_subs_new_account = 0
for sub in new_account.user.subreddits(limit=None):
	num_subs_new_account = num_subs_new_account + 1
print("Number of subscribed subreddits for old account: " + str(num_subs_old_account))
print("Number of subscribed subreddits for new account: " + str(num_subs_new_account))