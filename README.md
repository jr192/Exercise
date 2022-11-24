# Exercise

The requests collections used are on [Tiqets.postman_collection.json] file.

## Installation

Let's use Docker to simplify the requirements dependency and virtualize the run environment. This will ensure that
everything goes by smoothly.


### Setup with Docker
Setup to run api:
 - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - In Repository root run: 
 1) remove data diretory and run `docker compose build` 
 2) `docker compose up —wait db` 
 3) `docker compose up` 
 4) open a new terminal window and run `docker-compose exec web python manage.py makemigrations --noinput` and `docker-compose exec web python manage.py migrate --noinput` 
 5) close all the windows and run `docker compose down` and `docker compose up` 
 - After this setup you just need to run the api a simple command: `docker compose up`and to stop `docker compose down`

### SQL UML DATABASE
This is how I would design my database.
![](../../../Desktop/uml.png)

About indexes, I would add on the columns where I use more the WHERE(FILTER) or JOIN(SELECTED_RELATED) operations to improve the query performance;
