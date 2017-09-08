# Sublime package NVM node path configuration
# Save this file in:
# ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/node_env.py
import os
import getpass
import subprocess

def runProcess(exe):
  p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  while(True):
    retcode = p.poll() #returns None while subprocess is running
    line = p.stdout.readline()
    yield line
    if(retcode is not None):
      break

user = getpass.getuser()

version = None

for line in runProcess('/Users/%(user)s/bin/node_ver' % {'user': user}):
  if not version:
    version = line.rstrip().decode("utf-8")
    break

path = "/Users/%(user)s/.nvm/versions/node/%(version)s/bin:/Users/%(user)s/.nvm/versions/node/%(version)s/lib:/Users/%(user)s/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" % {'version':version, 'user':user}
os.environ["PATH"] = path