echo "enter your wifi password (we know you use the same one for everything)"
read -s password
echo $password  | tr -d '\n' > .wifipassword

echo "want to install speedtest?"
read install
case "$response" in
    [yY][eE][sS]|[yY]) 
        brew tap teamookla/speedtest
        brew update
        brew install speedtest --force
        ;;
    *)
        echo "bye"
        ;;
esac
