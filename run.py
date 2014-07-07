from config_generators import * 
import os
# don't use subprocess because heroku doesn't like it
# from subprocess import call

if __name__ == '__main__':
  secret = str(os.environ.get('SYNC_SECRET'))
  config = SyncConfig(secret = secret)
  f = open('config', 'w')
  f.write(config.generate_file())
  f.close()

  for folder in config.used_folders():
    os.system("mkdir -p %s" % folder) 

  os.system("./btsync --nodaemon --config config")
