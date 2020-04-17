# network-tester

monitors our subpar network connection(s) up in the middle of the woods

# deployment
todo

# running locally
## on mac:
install the speedtest CLI using `homebrew`:
```
brew tap teamookla/speedtest
brew update
brew install speedtest --force
```

get airport hooked up via [black magic](https://osxdaily.com/2007/01/18/airport-the-little-known-command-line-wireless-utility/):
```
sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport
```

run
```
python3 main.py
```


