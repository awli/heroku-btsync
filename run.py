import os
from subprocess import call

# call(["mkdir /app/.sync"])
# call(["mkdir -p /tmp/data"])
# apparently heroku doens't like call...
os.system("mkdir -p /tmp/.sync")
os.system("mkdir -p /tmp/data")

secret = str(os.environ.get('SYNC_SECRET'))

CONFIG_SKELETON = """
{
  "device_name": "filemirror",
  "listening_port" : 0,                       // 0 - randomize port
  "storage_path" : "/tmp/.sync",
  "check_for_updates" : false,
  "use_upnp" : false,
  "download_limit" : 0,
  "upload_limit" : 0,
  "shared_folders" :
  [
    {
      "secret" : "%s",
      "dir" : "/tmp/data",
      "use_relay_server" : true,
      "use_tracker" : true,
      "use_dht" : true,
      "search_lan" : false,
      "use_sync_trash" : true,
      "overwrite_changes" : false
    }
  ]
}
""" % secret

f = open('config', 'w')
f.write(CONFIG_SKELETON)
f.close()

os.system('cat config')

os.system("./btsync --nodaemon --config config")
# call(["./btsync", "--config", "./config"])
