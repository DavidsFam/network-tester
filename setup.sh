echo "enter your wifi password (we know you use the same one for everything)"
read -s password
echo $password  | tr -d '\n' > .wifipassword

echo "want to install requirements?"
read install
case "$install" in
    [yY][eE][sS]|[yY]) 
        pip3 install -r requirements.txt
        brew tap teamookla/speedtest
        brew update
        brew install speedtest --force
        brew cask install docker
        open -a Docker
        docker network create -d bridge localnet
        docker run --name prometheus --network localnet -d -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
        docker run --name pushgateway --network localnet -d -p 9091:9091 prom/pushgateway
        docker run --name grafana --network localnet -i -d -p 3000:3000 grafana/grafana
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
       # todo set network test to default home dash https://grafana.com/docs/grafana/latest/http_api/preferences/#update-current-user-prefs
        ;;
    *)
        echo "bye"
        ;;
esac
