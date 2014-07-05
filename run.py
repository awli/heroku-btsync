import os
from subprocess import call
call(["mkdir /app/.sync"])
call(["mkdir -p /tmp/data"])

secret = str(os.environ.get('SYNC_SECRET'))

CONFIG_SKELETON = """
{
  "device_name": "mirror",
  "listening_port" : 0,                       // 0 - randomize port
  "storage_path" : ".sync",
  "check_for_updates" : false, 
  "use_upnp" : false, 
  "download_limit" : 0,
  "upload_limit" : 0,
  "webui" : // this is disabled
    {
      //"listen" : "0.0.0.0:8888",
      //"login" : "admin",
      //"password" : "password"
    }
  ,
  "shared_folders" :
  [
    {
      "secret" : "%s",
      "dir" : "tmp/data", 
      "use_relay_server" : true,
      "use_tracker" : true,
      "use_dht" : true,
      "search_lan" : false,
      "use_sync_trash" : true,
      "overwrite_changes" : true,
      "known_hosts" :
      [
        //"192.168.1.2:44444"
      ]
    }
  ]
}
""" % secret

f = open('config', 'w')
f.write(CONFIG_SKELETON)

call(["./btsync", "--config", "./config"])
