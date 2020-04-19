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
        # todo we could easily use the grafana api to hook prom up and import the dashboard
        ;;
    *)
        echo "bye"
        ;;
esac
