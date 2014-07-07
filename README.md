heroku-btsync
=============

Deploy a BitTorrent Sync node to Heroku. 

The node is not persistent across dyno restarts, and should only be used to assist other nodes that you may run. 

It is highly recommended that you provide a read-only (and when available, encrypted) secret. Your node won't be able to accidentally mess up your files in this way. 

**Warning: You need to provide your BitTorrent Sync secrect, so Heroku or Amazon can in theory read your data.**

# Quickstart

- Clone this repo `git clone https://github.com/awli/heroku-btsync.git`
- `cd heroku-btsync`

The next steps assume you have the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed. 

- Create a new Heroku application `heroku create`
- Set the config variable `heroku config:set SYNC_SECRET=your_secret_here`
- Add the `heroku` remote to this git repo `heroku git:remote`
- Deploy the application (may take some time) `git push heroku master`

Initially, there will be no Heroku dynos running. To run one dyno (free tier):

- `heroku scale sync=1`

Your dyno should now be querying the tracker server and broadcasting on the DHT network. If you do not like this default behavior, you can modify it in the options in `config_generators.py`. 

# How it works
heroku-btsync works by reading a `SYNC_SECRET` environment variable, and generating some configuration files. It then calls the Linux x64 binary. 
