# reddit-account-migration
Migrate old Reddit account's subreddits and saved posts to fresh Reddit account.

## Requirements

Using a virtual environment in an Anaconda Prompt is a good way to simplify Python package management and deployment. [Here is a link](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) that can help you set up Anaconda and Python. If you have a preferred package management tool, feel free to use that instead.

Creating and entering a virtual environment in Anaconda:

```
conda create --name reddit-migration python=3.7
conda activate reddit-migration
```

Praw has good documentation on using the Reddit API. Here is their [Quick Start guide](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html). We will be using an OAuth authentication method called [Password Flow](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow). 

Collect the necessary information - Client ID, Client Secret, User Agent, and the username and password of a Reddit account. Avoid displaying your Reddit account and API credentials in a public repository!

### Finding the Password Flow information
1. Go to https://www.reddit.com/prefs/apps/
2. Click on the 'are you a developer? create an app...' button
!['are you a developer? create an app...' button](https://github.com/erin-bristow/reddit-account-migration/blob/main/img/dev_button.PNG)
3. Fill in the info.
![name, script, description, and redirect uri (can just be https://reddit.com)](https://github.com/erin-bristow/reddit-account-migration/blob/main/img/create_app.PNG)
4. Use the provided info. The client ID is at least a 14-character string listed just under “personal use script” for the desired developed application. The client secret is at least a 27-character string listed next to "secret" for the application.
