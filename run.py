from config_generators import * 
import os
# don't use subprocess because heroku doesn't like it
# from subprocess import call

if __name__ == '__main__':
  os.system("mkdir -p /tmp/.sync")
  os.system("mkdir -p /tmp/data")

  secret = str(os.environ.get('SYNC_SECRET'))

  config = SyncConfig(secret = secret)
  f = open('config', 'w')
  f.write(config.generate_file())
  f.close()

  os.system("./btsync --nodaemon --config config")
