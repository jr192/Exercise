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
This is how I would design my database [link](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=uml.png#R7Vldc9o4FP01PLJjWQbCY0wCbTebTZtus9OXHWELo0ZYVBYB8uv3ypY%2FBcSkSdNOMsMM6Opb5%2Bici93Bo8VmIsly%2FpcIKe%2B4Trjp4LOO6yLP7cOXjmyzyGDoZYFIstA0KgPX7J6aoGOiKxbSpNZQCcEVW9aDgYhjGqhajEgp1vVmM8Hrsy5JRK3AdUC4Hb1hoZpn0RN3UMbfURbN85lRf5jVLEje2OwkmZNQrCshfN7BIymEyn4tNiPK9eHl53LzfnvDL277kw8fk%2B%2FkH%2F%2FPz5dfutlg42O6FFuQNFaPHvr%2BdjZ%2B98X79u%2Fyavxx7UxOpx%2B6potzR%2FjKnNffMqTSbFht81NM1mzBSQwlfyZidW1qMJQJZ1EMvwNYHPTE%2Fh2VigEAp6ZCiSVEgznj4QXZipXeQqJIcJuX%2FLmQ7B6GJRyqEASgWirDJSBgtcW17glhB6KSJtDmKj8XVIQuSKJMm0BwTpYJm6YL1k0WREYs9oVSYpEPJFZxSENTKoBOC0qK24I6un9LNAxq%2BjTopsJFg86EigVVcgtNTG1BNHPTUF5el7xFfRObVzh7YmLEXJWoGLqY7RNcLRJHcAbldLgxnddyulwR8ukIB9xjoqivTzGpkhB%2BVHZahlJqHkHTnkXTYJUAfDuYCoet2rMyWZKAxdEFnenNeWXkk9mvDgnoO%2BMpI%2BYsDGmcMkYRRTJSaZosBYtVeiA9Hz5wbCPnj16nB0saQRmVZfjo5lKNRAzkIixlEQXGrqlm7Q5%2BHby6D%2FNrW8ftWHyrdKoBeyyKCFsw%2BkQGYDlt9Qa96c3z6Q3GLQVg8Ci9wV5jupMd0w1%2BDb1BnsXU6R6mvhq9KW7vbyQ4fQtGCz8ah6c6zYTSlAt91X0IGS1ATlYcMz1xm8tav9k0hFzUzEX5VKzPy4CfBqAiZ8rRVz0RKxnQFpCBukW0hZfo5R4EdheSknKi2F093T4gDVeauRUVQg1ZGOD6ENkuTa9qftsYCDcGcgeNtWSnYA30ZJoxsMg22pekvNnb89tb7%2Bem073e75NOu7a9QfvX62yD1tz6VZzNPc7ZxDI96uO8q7A99PJO5rQ0shzKB53MwKyZVL21HnoSUyty21wMhu7jTK3nPTDQHlOzBuo2s%2B%2FGOGI2S%2Biz%2BKJr%2B6JF1dRmKhqQaw5P1cRSnKkxG5%2BTKeU%2BOFiUcnckuACFOotFaa0mkXPby0F%2Bt8wTSbOsTvF3qb0FdX%2BQTTkpfxpUQwsqDstO9ORqnz%2FM1SIXiSaMdSnXat3GTxbgDKmsHEb3qCTjB6lgQb6PHe2FZvgkQtPFJ%2FVhnWfgytlXD%2Fmz%2F8ZfI%2Bf79JJ%2FjtFkU%2BRjJVUuWzCkPfgPc4mslEgMpgXoTQkAB2uE9iLazqz2IoydhsI6dgKId%2BQI%2BEC62TZH2ImQayGE3hCq%2FUNEL4yQ%2FTz0td%2BhQV0lEe69LEL2i4dXfoe8YSMh3fHQ%2BIkQgmL5cjWzrfIVNT7%2FHw%3D%3D).

About indexes, I would add on the columns where I use more the WHERE(FILTER) or JOIN(SELECTED_RELATED) operations to improve the query performance;
