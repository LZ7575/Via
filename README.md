# Installation

Run the hosts script to configure `/etc/hosts`

``` sh
cd scripts
bash hosts.sh
```

## Routes

bitcoin.local/redis
bitcoin.local/api

## Testing API

API should be exposed at `bitcoin.local/api`
Go to `bitcoin.local/api/docs` to see all commands and trigger api

## Testing Horizontal Autoscaler

``` sh
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://hpa-demo-deployment; done"
```

## Debugging

If the nginx port is not configured for localhost run this

``` sh
cd app
kubectl patch deployment ingress-nginx-controller --patch "$(cat ingress-nginx-controller-patch.yaml)" -n kube-system
```
