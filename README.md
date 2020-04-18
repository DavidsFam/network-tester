# network-tester

monitors our subpar network connection(s) up in the middle of the woods

![](.github/notsureif.gif)

## deployment
todo

## running locally
### dependencies
this repo depends on
- the python packages in [requirements.txt](requirements.txt)
- the [speedtest CLI](https://www.speedtest.net/apps/cli)
- the OSX command-line networking utility [networksetup](https://www.unix.com/man-page/OSX/8/networksetup/)
- [grafana](https://grafana.com/)
- [prometheus](https://prometheus.io/)

### [on mac](#on-mac):
get set up
```
./setup.sh
```

run network tester
```
python3 main.py
```

### on non-mac:
1. buy a mac
2. see [on mac](#on-mac)
