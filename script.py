import sys

def run():
  f = open('/private/etc/hosts').read().split('\n')
  out = []
  for i, line in enumerate(f):

    if i < 11:
      out.append(line)
    else:
      try:
        if line[0] == '#': 
          out.append(line[1:])
        else:
          out.append('#' + line)
      except:
        continue

  outF = open('/private/etc/hosts', "w")

  for line in out:
    # write line to output file
    outF.write(line)
    outF.write("\n")

  outF.close()

import time
while(1):
  run()
  time.sleep(5)
  run()
  if len(sys.argv) > 1:
    exit()
  time.sleep(200)
