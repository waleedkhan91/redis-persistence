*****************************
Author: Waleed Khan
email: waleedkhan91@gmail.com
*****************************

This redis deployment provision a single instance redis on kubernetes with persistence which means if the pod is crashed and rebounced the cache data is not lost.

This deployment assumes that you have a running NFS and it is ready to mount any volume in kubernetes cluster. It is required to modify IP address in redis-persistent-volume.yaml.

Deploy the files with following command.

> kubectl apply -f redis-persistent-volume.yaml

Check if persistent volume is successfully bound with the claim by following command:

> kubectl get pv

Once successful, deploy the redis. This deployment is configured to start background process of saving redis instance in rdb file after 300 seconds.

> kubectl apply -f redis.yaml

After successful deployment. Run in to the pod and set some keys. Then delete the pod and you will have the keys still present in the cache.
