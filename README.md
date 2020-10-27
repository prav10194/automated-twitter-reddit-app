# automated-twitter-reddit-app

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

## Fixing ffmpeg for heroku

You need to follow this for fixing in-case you are having issues while downloading videos from reddit using youtube-dl - https://elements.heroku.com/buildpacks/jonathanong/heroku-buildpack-ffmpeg-latest

## Postman screenshot on how the API looks like

![Postman screenshot](https://github.com/prav10194/automated-twitter-reddit-app/blob/master/assets/s1.png)
