# fastapi_study
```
kubectl create secret generic jwt-secret --from-literal=JWT_KEY=asdf

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.44.0/deploy/static/provider/cloud/deploy.yaml
```

```
curl -X 'POST' \
  'http://localhost:8000/api/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=&username=string%40admin.com&password=string&scope=&client_id=&client_secret='
```

## TODO
* implement user authentication
* implement roll based access control
* implement common auth module









