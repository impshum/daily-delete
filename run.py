import praw
import schedule
from time import sleep
from random import choice
import configparser
import datetime
import os


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


def get_date():
    return f"{datetime.datetime.now():%d/%m/%Y}"


def runner(reddit, target_subreddit, posts_folder, test_mode):
    with open('last.txt', 'r') as f:
        last_id = f.read().strip()
    if last_id != 'start':
        reddit.submission(last_id).delete()

    random_file = choice(os.listdir(posts_folder))

    with open(f'{posts_folder}/{random_file}') as f:
        line = choice(f.read().splitlines()).split('|')
        title = line[0].strip()
        selftext = line[1].strip()

    if not test_mode:
        new_id = reddit.subreddit(target_subreddit).submit(
            title, selftext=selftext)

        with open('last.txt', 'w') as f:
            f.write(new_id.id)

    print(f'{C.G}{get_date()} {C.Y}{title} {C.C}{selftext} {C.P}{random_file}{C.W}')


def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    reddit_user = config['REDDIT']['reddit_user']
    reddit_pass = config['REDDIT']['reddit_pass']
    client_id = config['REDDIT']['client_id']
    client_secret = config['REDDIT']['client_secret']
    target_subreddit = config['REDDIT']['target_subreddit']
    post_time = config['SETTINGS']['post_time']
    test_mode = int(config['SETTINGS']['test_mode'])
    posts_folder = config['SETTINGS']['posts_folder']

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent='Daily delete (by u/impshum)',
                         username=reddit_user,
                         password=reddit_pass)

    if test_mode:
        t = f'{C.R}TEST MODE{C.Y}'
    else:
        t = ''

    print(f"""{C.Y}
╔╦╗╔═╗╦╦ ╦ ╦  ╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗
 ║║╠═╣║║ ╚╦╝   ║║║╣ ║  ║╣  ║ ║╣  {t}
═╩╝╩ ╩╩╩═╝╩   ═╩╝╚═╝╩═╝╚═╝ ╩ ╚═╝ {C.C}v1.1{C.W}

Posting every day at {post_time}
Bot started on {get_date()}
    """)

    if test_mode:
        runner(reddit, target_subreddit, posts_folder, test_mode)
    else:
        schedule.every().day.at(post_time).do(
            runner, reddit, target_subreddit, posts_folder, test_mode)
        while True:
            schedule.run_pending()
            sleep(1)


if __name__ == '__main__':
    main()
