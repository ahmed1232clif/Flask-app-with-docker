# Flask-app-with-docker
Deploying a sample flask app with docker in ec2 instance 

- go to aws ec2 and create an instance ubuntu or linux

- give the security group port number 8000 and 80

- connect the instance and run this command
- sudo apt update
- sudo apt install docker-compose

- installing docker-compose will install everything from docker even the docker.io

- now you can check if docker is working by running a command
- docker
- docker-compose

- now clone this repo git clone ..

- and go in the folder and edit the docker-compose file by running a command
- sudo vi docker-compose.yml
- and replace the SERVER_NAME=0.0.0.0 with your instance ip address and also you can change the network_mode: host to bridge if its not working
- and if you dont want the nginx server you can clear the nginx part in the yml file

- thats it thanks and learn more 
