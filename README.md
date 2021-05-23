# Framework stack
- flask
- slack event api
- sqlite

# Cloning
since the submodules are in git, need to add ssh keys first, alternatively can manually clone submodules in plugin page.
```
git clone --recurse-submodules -j8 https://github.com/stancsz/slack-bot-with-events-api.git
```


# Setup
ngrok & events subscription
```
sudo snap install ngrok
ngrok http 5000
http://localhost:5000
```
```
ngrok by @inconshreveable                                                                                                               (Ctrl+C to quit)
                                                                                                                                                        
Session Status                online                                                                                                                    
Session Expires               1 hour, 7 minutes                                                                                                         
Update                        update available (version 2.3.40, Ctrl-U to update)                                                                       
Version                       2.3.35                                                                                                                    
Region                        United States (us)                                                                                                        
Web Interface                 http://127.0.0.1:4040                                                                                                     
Forwarding                    http://3154debedac2.ngrok.io -> http://localhost:5000                                                                     
Forwarding                    https://3154debedac2.ngrok.io -> http://localhost:5000   
```
## Event Subscriptions
go to `https://api.slack.com/apps/<app-id>/event-subscriptions?`
and then add `http://3154debedac2.ngrok.io/slack/events` to `Request URL` 


## Environment variables
- SLACK_CHANNEL: copy url of channel to get the channel str
- SLACK_BOT_TOKEN: under `OAuth & Permissions`
- SIGNING_SECRET: under `Basic Information`
https://api.slack.com/apps/ 


# Docker
```bash
docker build --tag slackbot-wea .
docker run -e SLACK_BOT_TOKEN=""\
-e SLACK_CHANNEL=C022NRBTRN1=""\
-e SIGNING_SECRET=""\
slackbot-wea
```
