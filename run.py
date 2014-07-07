from config_generators import * 
import os
# don't use subprocess because heroku doesn't like it
# from subprocess import call

if __name__ == '__main__':
  os.system("mkdir -p /tmp/.sync")
  os.system("mkdir -p /tmp/data")

  secret = str(os.environ.get('SYNC_SECRET'))

  f = open('config', 'w')
  f.write(generate_config(secret))
  f.close()

  os.system("./btsync --nodaemon --config config")
