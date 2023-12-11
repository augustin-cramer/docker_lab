# Data Stream Processing
## Lab 3 - Docker

Careful Note :
I am working on MacOs so the commands could change, please adapt.

### basic_page: questions 1 to 4

From the root of the repo, do the following:
```command
cd basic_page
```

#### Question 1

In this directory, you will see 3 main files:
```
app.py
Dockerfile
docker-compose.yml
```

Combined with the content of the directories `static` and `templates`, these files are the answer to question 1.
The app is a simple web page that displays an image with a title and a short text.

#### Question 2

```command
docker-compose up --build
```

This will create a Docker Image and run a container.

#### Question 3

In your brower, go to http://localhost:5001

#### Question 4

The Docker volume is implemented in the `docker-compose.yml`. You can make a modification in the `index.html`, **save the file** and refresh the page http://localhost:5001 to see the changes are being reflected

### jovian-careers-website: questions 5 and 6

Navigate back to the root and do
```command
cd jovian-careers-website
```

The base for the code is from [this repo](https://github.com/aakashns/jovian-careers-website/tree/main), that codes a basic website that displays job offers that are stored in a dictionnary variable in the main script. The work I did was to build a MySQL server that would contain this data.

If not already done, stop the previous command because I am using the same port with this script.

Now do:
```command
docker-compose up --build
```

#### Question 5

```docker-compose.yml
# docker-compose.yml
services:
  mysql:
    image: mysql:latest
    ...
    environment:
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
```
These instructions setup a Mysql Database Container.

#### Question 6

```docker-compose.yml
networks:
  web_network1:
    driver: bridge
  web_network2:
    driver: bridge

services:
  web1:
    networks:
      - web_network1
    environment:
      MYSQL_DB: jovian_careers_1
      DATA_FILE_NAME: jobs_1.json

  web2:
    networks:
      - web_network2
    environment:
      MYSQL_DB: jovian_careers_2
      DATA_FILE_NAME: jobs_2.json

  mysql:
    image: mysql:latest
    networks:
      - web_network1
      - web_network2
```

We are creating two containers containing copies of the same webapp but they are provided different configurations using the environnment variables.
They also belong to different networks so these containers cannot communicate between each other but can communicate with the Mysql Database Container.
Each instance of the website has its own data, you can verify is using the api endpoint /api/jobs (for instance: http://localhost:5001/api/jobs).
