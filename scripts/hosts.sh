kubectl get ingress --watch
read -p "Enter address: " address
if [ -z "$var" ]
then
    sudo echo "$address	bitcoin.local" >> /etc/hosts
fi