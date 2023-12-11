Data Stream Processing
Lab 3 - Docker

Careful Note :
I am working on MacOs so the commands could change, please adapt.

1 - basic_page

From the root of the repo, do the following:
```command
cd basic_page
```

This directory contains the code to answer the questions 1, 2, 3 and 4

Question 1

In this directory, you will see 3 main files:
```
app.py
Dockerfile
docker-compose.yml
```

Combined with the content of the directories `static` and `templates`, these files are the answer to question 1.
The app is a simple web page that displays an image with a title and a short text.

Question 2

```command
docker-compose up --build
```

This will create a Docker Image and run a container.

Question 3

Then, in your brower, go to http://localhost:5001

Question 4

The Docker volume is implemented in the `docker-compose.yml`. You can make a modification in the `index.html`, **save the file** and refresh the page http://localhost:5001 to see the changes are being reflected

2 - jovian-careers-website

Navigate back to the root and do
```command
cd jovian-careers-website
```

This directory contains the answers to questions 5 and 6.

The base for the code is from this repo, that codes a basic website that displays job offers that are stored in a dictionnary variable in the main script. The work I did was to build a MySQL server that would contain this data.

If not already done, stop the previous command because I am using the same port with this script.

Now do:
```command
docker-compose up --build
```

In the `docker-compose.yml`, you can see what I am doing, let's break it down.

Question 5

```docker-compose.yml
  mysql:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3306:3306"
```
These instructions setup 


