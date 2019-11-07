import signal
import time
from helpers import *
from sys import platform

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        self.kill_now = True
        self.closer()

    def closer(self):
        try:
            with open(self.path, 'w') as f:
                f.write(self.dataInit)
        except:
            print("closed too soon!")
        
        exit()
if __name__ == '__main__':
    killer = GracefulKiller()
    killer.path = ''

    if len(killer.path):
        print("using pre-default path")
    elif platform == "linux" or platform == "linux2":
        killer.path = '/etc/hosts'
    elif platform == "darwin":
        killer.path = '/private/etc/hosts'
    else:
        print("Error: host file not found. Manually, define the path vairable in this script")
        exit()
    killer.dataInit = addHosts(killer.path)
    start = 1
    while not killer.kill_now:
        time.sleep(1)
        if start:
            outAc = skipAds(killer.path)
            start = 0
        else:
            skipAds(killer.path)

    print("End of the program. All back to normal")
