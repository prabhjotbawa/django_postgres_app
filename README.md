## About
A simple Django app to store data to postgres.
`myproject` is the entrypoint and invokes the database model defined in `myapp`.

The project comes with a [docker-compose](docker-compose.yml) file to facilitate running the 
project locally on docker.
Run `docker-compose up --build` to build and run the app. The app runs on `http://localhost:5001`

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
The manifests have an ingress resource, but it will not do anything without a load balancer
For local deployment to `minikube`, I would port forward the app and interact with the application.

This [diagram](architecture.png) shows the overall data flow when the app is deployed on EKS and launched via the 
browser entering `https://testapp.prabhjotbawa.com`.
The solid lines are requests and dotted lines are responses.

I used **Terraform** to provision a single node cluster.

## TODO
The app could fail to launch if postgres isn't running using `docker-compose`. 
It's probably not waiting long enough for the database to get ready, although it calls a script to wait.
Workaround: Re-run the web service from docker-compose and app runs just fine.

The same issue is not seen when running the app on kubernetes since it handles it gracefully.

**Please note**: 
* For production, `persistent volume claims` must be used to store the data. Since, I have not used PVC's, the data is 
not persisted and gets deleted if the pod gets removed.
* Fetch secrets from a secure location like vault or AWS secret manager.
