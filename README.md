### Create network
```bash
docker network create jenkins
```
### In order to execute Docker commands inside Jenkins nodes, download and run the docker:dind Docker image
```bash
docker run --name jenkins-docker --rm --detach \
  --privileged --network jenkins --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind --storage-driver overlay2
```
### Build a new docker image from this Dockerfile
```bash
docker build -t myjenkins-blueocean:2.414.3-1 .
```
### Run Docker container
```bash
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.414.3-1
```
### Get initialAdminPassword
```bash
docker exec -it jenkins-blueocean bash
cat /var/jenkins_home/secrets/initialAdminPassword
```