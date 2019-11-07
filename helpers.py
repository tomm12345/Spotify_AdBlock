import os
import sys

# path = 'kick'

timeNoAd = 200
timeAd = 10

hosts = ['0.0.0.0 b.scorecardresearch.com',
'0.0.0.0 bounceexchange.com',
'0.0.0.0 media-match.com',
'0.0.0.0 omaze.com',
'0.0.0.0 redirector.gvt1.com',
'0.0.0.0 s0.2mdn.net',
'0.0.0.0 spclient.wg.spotify.com',
'0.0.0.0 v.jwpcdn.com',
'0.0.0.0 weblb-wg.gslb.spotify.com',
'0.0.0.0 www.omaze.com',
'127.0.0.1 media-match.com',
'127.0.0.1 adclick.g.doublecklick.net',
'127.0.0.1 googleads.g.doubleclick.net',
'127.0.0.1 http://www.googleadservices.com',
'127.0.0.1 pagead2.googlesyndication.com',
'127.0.0.1 desktop.spotify.com',
'127.0.0.1 pubads.g.doubleclick.net',
'127.0.0.1 audio2.spotify.com',
'127.0.0.1 crashdump.spotify.com',
'127.0.0.1 adeventtracker.spotify.com',
'127.0.0.1 log.spotify.com',
'127.0.0.1 analytics.spotify.com',
'127.0.0.1 ads-fa.spotify.com',
'127.0.0.1 audio-ec.spotify.com',
'127.0.0.1 heads-ec.spotify.com',
'127.0.0.1 prod.spotify.map.fastlylb.net',
'127.0.0.1 sto3.spotify.com',
'127.0.0.1 spclient.wg.spotify.com',
'127.0.0.1 upgrade.spotify.com'
]


 
def addHosts(path):
  f = open(path)
  dataInit = f.read()
  f.close()
  f = open(path, 'a+')
  # dataInit = f.read()
  f.write('\n' + "="*100 + '\n')
  for host in hosts:
    f.write(host + '\n')

  return dataInit

def run(path):
  f = open(path).read().split('\n')
  out = []
  flag = 1
  for i, line in enumerate(f):

    if flag:
      if line == '='*100:
        outAc = [it for it in out]
        flag = 0
        out.append(line)
        continue
      out.append(line)
    else:
      try:
        if line[0] == '#': 
          out.append(line[1:])
        else:
          out.append('#' + line)
      except:
        continue

  outF = open(path, "w")

  for line in out:
    # write line to output file
    outF.write(line)
    outF.write("\n")

  outF.close()
  return outAc

import time

def skipAds(path):
  outAc = run(path)

  time.sleep(timeAd)
  outAc = run(path)
  if len(sys.argv) > 1:
    exit()
  time.sleep(timeNoAd)

  return outAc




