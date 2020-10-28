from __future__ import unicode_literals
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests
import dropbox

app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

import praw
import requests
import youtube_dl
import random
import time
import os

dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))

reddit = praw.Reddit(
 client_id=os.environ.get('REDDIT_CLIENT_ID'),
 client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
 user_agent=os.environ.get('REDDIT_USER_AGENT'),
 username=os.environ.get('REDDIT_USERNAME'),
 password=os.environ.get('REDDIT_PASSWORD')
)
print(reddit.read_only)

from twython import Twython
twitter = Twython(os.environ.get('TWITTER_APP_KEY'), os.environ.get('TWITTER_APP_SECRET'),
                  os.environ.get('TWITTER_OAUTH_TOKEN'), os.environ.get('TWITTER_OAUTH_TOKEN_SECRET'))

@app.route("/") 
def home_view(): 
        return render_template('frontpage.html')

@app.route("/postreddit") 
def post_reddit():
    
    os.remove('./ids')
    dbx.files_download_to_file("./ids", '/Reddit-Twitter/ids')
    
    print("VAR:", os.environ.get('VAR'))
    if request.args.get('frensandfamilycode') == os.environ.get('SUPER_SECRET_TOKEN'):
        print("Access granted")
        subreddits_list = ["aww","earthporn","cattaps","tippytaps","masterreturns","dogpictures","RarePuppers","DogsWithJobs"]
        random_subbreddit = random.choice(subreddits_list)
        subreddit = reddit.subreddit(random_subbreddit)

        time_filters_counts = ["year:100", "month:20", "week:5"]
        time_filter_count = random.choice(time_filters_counts)
 
        alreadyPosted = False
        reddit_post = {"url": "", "id": "", "title": "", "postlink": ""}

        for submission in subreddit.top(time_filter=time_filter_count.split(":")[0],limit=int(time_filter_count.split(":")[1])):
                try:
                        readfile = open("ids", "r")
                        isUnique = submission.id not in readfile.read()
                        readfile.close()
                except:
                        isUnique = True
                        open("ids",'w').close()

                if isUnique and not alreadyPosted: #check if id does not exists in file:
                        alreadyPosted = True
                        try:
                                appendfile = open("ids", "a")
                                appendfile.write("\n" + submission.id)
                                appendfile.close()

                                reddit_post["postlink"] = "http://reddit.com" + submission.permalink
                                reddit_post["url"] = submission.url
                                reddit_post["id"] = submission.id
                                reddit_post["title"] = submission.title
                                reddit_post["author"] = submission.author

                        #     print("reddit_link: " + reddit_link)

                        except:
                                alreadyPosted = False
                                print("Checking the next post")


        r = requests.get(reddit_post["url"], allow_redirects=True)
        print(r.headers.get('content-type'))
        print("running code now for: " + reddit_post["id"])
        ydl_opts = {'outtmpl': reddit_post["id"] + '.%(ext)s'}

        print(r.headers.get('content-type'))
        if r.headers.get('content-type') == "image/jpeg" or r.headers.get('content-type') == "text/html":
                open(reddit_post["id"] + '.jpg', 'wb').write(r.content)
                photo = open(reddit_post["id"] + '.jpg', 'rb')
                tweet = reddit_post["title"] + ' \nr/' + str(random_subbreddit) + '\nu/' + str(reddit_post["author"]) + '\n\n[' + reddit_post["postlink"] + ']'
                response = twitter.upload_media(media=photo)
                twitter.update_status(status=tweet, media_ids=[response['media_id']])
                os.remove(reddit_post["id"] + '.jpg')

        if r.headers.get('content-type') == "text/html; charset=utf-8" or r.headers.get('content-type') == "text/html;charset=UTF-8":
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([reddit_post["url"]])
                        tweet = reddit_post["title"] + '\nr/' + str(random_subbreddit) + '\nu/' + str(reddit_post["author"]) + '\n\n[' + reddit_post["postlink"] + ']'
                        print(os.listdir("./"))
                        video = open(reddit_post["id"] + '.mp4', 'rb')
                        response = twitter.upload_video(media=video, media_category='tweet_video', media_type='video/mp4', check_progress=True)
                        twitter.update_status(status=tweet, media_ids=[response['media_id']])
                        os.remove(reddit_post["id"] + '.mp4')
        dbx.files_delete_v2('/Reddit-Twitter/ids', parent_rev=None)
        with open("./ids", "rb") as f:
                dbx.files_upload(f.read(), '/Reddit-Twitter/ids', mute = True)
        return {"message": "Posted successfully"}
