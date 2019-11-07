# Spotify_AdBlock

## Block Ads on Spotify

This script blocks off all audio ads on a Mac/Unix base client although poster ads still remain. Best suited to running 
long mixes, playlists or podcasts which are the best part of Spotify too!

For running the script. Follow these steps:-

1. Make the host file writable without sudo, this is so that the connection to adservers of spotify can be blocked.

```
sudo chmod a+rwx  /private/etc/hosts  # for mac
sudo chmod a+rwx  /etc/hosts # for Linux
```

2. Run the script to block ads

```
python Spotify_AdBlock/main.py
```

In case you observe stoppage in music wait for some time or just re-run the script. In case it doesn't work even after doing 
these steps. Close the script and wait for the music to start, when it does, start running the script back. The latter may 
result in one burst of Ads but they should not appear afterwards. 

If the stops in music happen more frequently, try reducing `timeNoAd` and on the opposite end if audio ads still come in 
try reducing `timeAd`. These depend a bit on internet speeds, high speed means better to have smaller `timeAd` and slower speeds mean smaller `timeNoAd` or larger `timeAd`.  
