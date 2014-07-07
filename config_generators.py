CONFIG_PROTOTYPE = """
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
"""

def generate_config(secret):
  return CONFIG_PROTOTYPE % secret
