import json

class SyncConfig(object):

  def __init__(self, name = 'heroku-btsync', secret = None):
    self.name = name
    self.options = {
      "listening_port" : 0,
      "storage_path" : "/tmp/.sync",
      "check_for_updates" : False,
      "use_upnp" : False,
      "download_limit" : 0,
      "upload_limit" : 0,
    }
    self.secrets = []
    if secret:
      self.add_secret(secret)

  def add_secret(self, secret):
    self.secrets.append(secret)

  def used_folders(self):
    ans = ["/tmp/.sync"]
    for i in xrange(len(self.secrets)):
      ans.append("/tmp/data/%d" % i)
    return ans

  def generate_shared_folders(self):
    ans = []
    for index, secret in enumerate(self.secrets):
      ans.append({
        'secret' : secret, 
        "dir" : "/tmp/data/%d" % index,
        "use_relay_server" : True,
        "use_tracker" : True,
        "use_dht" : True,
        "search_lan" : False,
        "use_sync_trash" : True,
        "overwrite_changes" : False
        })
    return ans

  def generate_file(self):
    config = self.options.copy()
    config['device_name'] = self.name
    config['shared_folders'] = self.generate_shared_folders()
    return json.dumps(config)
