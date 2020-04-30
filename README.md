# network-tester

![](.github/example.png)

monitors our subpar network connection(s) up in the middle of the woods

![](.github/notsureif.gif)

## running locally
### [on mac](#on-mac):
get set up
```
./setup.sh
```

grafana can be accessed in a browser at [localhost:3000](http://localhost:3000). default login is `admin`/`admin`; change at your leisure. the network speed dashboard has been automatically generated.

run network tester
```
python3 main.py
```

### on non-mac:
1. buy a mac
2. see [on mac](#on-mac)

### dependencies
this repo depends on
- the python packages in [requirements.txt](requirements.txt)
- the [speedtest CLI](https://www.speedtest.net/apps/cli)
- the OSX command-line networking utility [networksetup](https://www.unix.com/man-page/OSX/8/networksetup/)
- [grafana](https://grafana.com/)
- [prometheus](https://prometheus.io/)
