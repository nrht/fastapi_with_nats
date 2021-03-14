# TODO
* --user auth--
* --user create--
* --role create--
* push docker hub
* setup k8s
    * setup service itself
    * setup ingress service

* setup skaffold(development only)
* setup jwt secret(see tips below)
* ```slaffold dev```

# tips
* creating and accessing secrets
    * development only

```
kubectl create secret generic jwt-secret --from-literal=JWT_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```