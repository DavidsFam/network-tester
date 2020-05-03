echo "enter your wifi password (we know you use the same one for everything)"
read -s password
echo $password  | tr -d '\n' > .wifipassword

echo "want to install requirements?"
read install
case "$install" in
    [yY][eE][sS]|[yY])
        # this extremely fragile hack puts the airport command (needed for network discovery) on the PATH
        ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport

        # python deps
        pip3 install -r requirements.txt

        # speedtest cli
        brew tap teamookla/speedtest
        brew update
        brew install speedtest --force

        # dockerized prom, pushgateway, and grafana
        brew cask install docker
        open -a Docker
        docker network create -d bridge localnet
        docker run --name prometheus --network localnet -d -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
        docker run --name pushgateway --network localnet -d -p 9091:9091 prom/pushgateway
        docker run --name grafana --network localnet -i -d -p 3000:3000 grafana/grafana

        # creates default datasource, dashboard, home dash setup
        curl --location --request POST 'admin:admin@localhost:3000/api/datasources' \
            -H 'Content-Type: application/json' \
            -d '{
                "name": "Prometheus",
                "type": "prometheus",
                "access": "proxy",
                "url": "http://prometheus:9090",
                "basicAuth": false,
                "isDefault": true
            }'
        curl --location --request POST 'admin:admin@localhost:3000/api/dashboards/db' \
            -H 'Content-Type: application/json' \
            -d "$(cat Dashboard.json)"
        curl --location --request PUT 'admin:admin@localhost:3000/api/user/preferences' \
            -H 'Content-Type: application/json' \
            -d "{\"homeDashboardId\": 1}"
        ;;
    *)
        echo "bye"
        ;;
esac
