# automated-twitter-reddit-app

For my own learning, wanted to create a positive twitter feed filled with images taken from various subreddits. Not using it for any monetary gain or profits. (Also need help with the README or probably optimizing the code. Feel free to fork and send in PR.)

## Create Reddit App 

1. Go to https://www.reddit.com/prefs/apps

2. At the bottom of the page you will see a button - "Create another app"

![Twitter screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s5.png)

3. Fill out the following when creating the new app - (be sure to select script in the radio button)

![Twitter screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s6.png)

## Create Twitter App

1. Go to developer.twitter.com and apply for a new app - fill out the relevant information in the application. Mine took a few hours to approve. 

2. Create an app and get credentials - for TWITTER_APP_KEY and TWITTER_APP_SECRET

![Twitter screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s3.png)

![Twitter screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s2.png)

3. For TWITTER_OAUTH_TOKEN and TWITTER_OAUTH_TOKEN_SECRET

![Twitter screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s4.png)

## Add .env variables

**REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET** you can find it in the section of setup reddit app.

**REDDIT_USER_AGENT** can be anything unique for e.g. testapp:<reddit_username>

**REDDIT_USERNAME** your account username

**REDDIT_PASSWORD** your account password

**TWITTER_APP_KEY** Find API key in twitter app settings - refer to section of Twitter app section

**TWITTER_APP_SECRET** Find API key secret in twitter app settings - refer to section of Twitter app section

**TWITTER_OAUTH_TOKEN** refer to section of Twitter app section

**TWITTER_OAUTH_TOKEN_SECRET** refer to section of Twitter app section

**SUPER_SECRET_TOKEN** can be any keyword but you need to send in the same keyword while calling your get post reddit request. 

## Uploading the app on Heroku

Follow the steps to install heroku cli - https://devcenter.heroku.com/articles/heroku-cli

1. In the cmd/terminal after cloning the repo - (in case you have a git folder already in there do a **rm -r .git**)

```cmd
git init
git add .
git commit -m "added files"
heroku create
git push heroku master
heroku ps:scale web=1
```
Check logs using the following command - 

```cmd
heroku logs --tail
```

## Fixing ffmpeg for heroku

You need to follow this for fixing in-case you are having issues while downloading videos from reddit using youtube-dl - https://elements.heroku.com/buildpacks/jonathanong/heroku-buildpack-ffmpeg-latest

## Postman screenshot on how the API looks like

![Postman screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s1.png)

## Needs to add a external storage for persistent data
