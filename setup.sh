echo "enter your wifi password (we know you use the same one for everything)"
read -s password
echo $password  | tr -d '\n' > .wifipassword

echo "want to install requirements?"
read install
case "$response" in
    [yY][eE][sS]|[yY]) 
        pip3 install -r requirements.txt
        brew tap teamookla/speedtest
        brew update
        brew install speedtest --force
        brew cask install docker
        open -a Docker
        docker run --name prometheus -d -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
        docker run --name pushgateway -d -p 9091:9091 prom/pushgateway
        docker run --name grafana -i -d -p 3000:3000 grafana/grafana
        ;;
    *)
        echo "bye"
        ;;
esac
