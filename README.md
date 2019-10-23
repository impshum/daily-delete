## Daily Delete

Posts a submission to a chosen subreddit every day and deletes it after 24hrs

![](https://github.com/impshum/daily-delete/blob/master/screenshot.jpg?raw=true)

### Instructions

- Install requirements ```pip install -r requirements.txt```
- Create Reddit (script) app at https://www.reddit.com/prefs/apps/ and get your id, tokens etc
- Edit conf.ini with your details
- Edit posts.txt with your post titles and texts
- Run it ```python run.py```

#### Info

- Separate titles and text in posts.txt with a pipe ```|```
- Posts are picked at random from posts.txt
- Posts are not deleted from posts.txt
- Windows users see this post to enable colours in your terminal/prompt: https://recycledrobot.co.uk/words/?print-python-colours
