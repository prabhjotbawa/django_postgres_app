## About
A simple Django app to store data to postgres.
`myproject` is the entrypoint and invokes the database model defined in `myapp`.

The project comes with a [docker-compose](docker-compose.yml) file to facilitate running the 
project locally on docker.
Run `docker-compose up --build` to build and run the app. The app runs on `http://localhost:5001`
`docker-compose` creates a volume to store the data and mounts on to the container. The volume persists the data
and acts like a persistent volume. However, the volume is a docker volume and can be inspected running the 
`docker volume inspect <volume-name>` command or using docker desktop.

### Local development
The project can be built with running the below command
`docker build -t mywebapp:latest .`
To run on linux:
`docker buildx build -t mywebapp:latest . --platform=linux/amd64`

Remember to run the migrations, if any changes are made to the models.
`python manage.py makemigrations myapp`

Postgres can be connected from the commandline running the command:
`psql --host=127.0.0.1 --dbname=mydatabase --username=myuser`
Enter the password when promoted to.

### Running on kubernetes
The project also has kubernetes [manifests](resources/deployment.yml).
When running on AWS or a cloud, create a load balancer and point to the ingress controller.
The manifests have an ingress resource, but it will not do anything without a load balancer.
The manifest has a configmap `postgres-init-script`. 
Postgres on initialization creates the database and the users 
automatically; however, I have left the configmap as an example to show how to pass custom scripts to postgres. 
Please note the configmap must be mounted as a volume for the script to `/docker-entrypoint-initdb.d` in such cases.
An example:
```yaml
spec:
containers:
- name: postgres
volumeMounts:
- name: init-script
  mountPath: /docker-entrypoint-initdb.d
volumes:
- name: postgres-storage
  emptyDir: {}
- name: init-script
  configMap:
    name: postgres-init-script
```

For local deployment to `minikube`, I would port forward the app and interact with the application.
Suggested steps:

```
kubectl expose deployment django-app --port=8765 --target-port=5001 --name=django-service --type=NodePort
```

Then use `minikube service` to get a URL:
```
minikube service django-service --url
```

This [diagram](architecture.png) shows the overall data flow when the app is deployed on EKS and launched via the 
browser entering `https://testapp.prabhjotbawa.com`.
The solid lines are requests and dotted lines are responses.

I used **Terraform** to provision a single node cluster.

## Installing via helm (Recommended)
Please refer https://prabhjotbawa.github.io/helm-charts/ for detailed instructions. I have also added the ability to
capture `data-inserted` [custom metrics](custom-metrics.png) and get scraped by Prometheus. The app registers the metrics with
Prometheus when `custom-metrics` endpoint is invoked.


## TODO
Add unit tests to test the code.
Simulate scenarios to test app launch when database is created v/s database already exists.

**Please note**: 
* For production, `persistent volume claims` must be used to store the data. Since, I have not used PVC's, the data is 
not persisted and gets deleted if the pod gets removed.
* Fetch secrets from a secure location like vault or AWS secret manager.
