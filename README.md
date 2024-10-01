## About
A simple Django app to store data to postgres.
`myproject` is the entrypoint and invokes the database model defined in `myapp`

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
The manifests have an ingress resource but it will not do anything without a load balancer
For local deployment to minikube, I would port forward the app and interact with the application.

## TODO
The app falls over if postgres isn't running, could be a problem with local machine.
Workaround: Run the web service from docker-compose and app runs just fine.