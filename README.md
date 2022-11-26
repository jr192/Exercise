# Exercise

The requests collections used are on [Tiqets.postman_collection.json] file.

## Installation

Let's use Docker to simplify the requirements dependency and virtualize the run environment. This will ensure that
everything goes by smoothly.


### Setup with Docker
Setup to run api:
 - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - In Repository root run: 
 1) remove data diretory and run `cp dev.env .env` && `docker compose build` 
 2) `docker compose up —wait db` 
 3) `docker compose up` 
 4) open a new terminal window and run `docker-compose exec web python manage.py makemigrations --noinput` and `docker-compose exec web python manage.py migrate --noinput` 
 5) close all the windows and run `docker compose down` and `docker compose up` 
 - After this setup you just need to run the api a simple command: `docker compose up`and to stop `docker compose down`
 

### HOW TO UPDATE FILES?
I created two endpoints to handle the file (see postman collections above) and another get endpoint to retrieve all the answers.  

### SQL UML DATABASE
This is how I would design my database [link](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7VldU9s4FP01eWTHsuwEHnEg6XZZlpZu2enLjmIrthbZcmWFJPz6XtnydwCHbUo7MJMZoqsvS%2Bfccy7OCE%2FjzVySNPpTBJSPbCvYjPDZyLaRY4%2Fhj45si8jkxCkCoWSBGVQHrtk9NUHLRFcsoFlroBKCK5a2g75IEuqrVoxIKdbtYUvB27umJKS9wLVPeD96wwIVFdFje1LH31EWRuXOaHxS9MSkHGxOkkUkEOtGCJ%2BP8FQKoYpv8WZKub688l5uft%2Fe8Ivb8fz9h%2Bwr%2Bdv749Pl56Nisdk%2BU6ojSJqoZy99f7ucvfvs%2FPdPejX7sLbmp4v3R2aKdUf4ytzXXzKg0hxYbctbzNYs5iSBlrcUibo2PRjahLMwge8%2BPBzMxN4dlYoBAKemQ4kUon7EeHBBtmKlj5Ap4t%2BWLS8Skt3DsoRDF4IAdEtluAQEbI641jMhbEFU0gzGXJX3gqrQBcmUGeMLzkmasUX%2BwHpITGTIEk8oJeJyIbFKAhqYVgV03lBS3FbU0fMHomFQ07dBNw0uGnTmVMRUyS0MMb0V0UymobK9rnmLxiYWNTh7bGLEpEpYLV3t9hFSiyQh3EG9He5s5wzcrlSEcjvCAfeEKOrpW8yaJIQvjZPWoZyae9DU7dHUX2UA3w6mwmWr4azMUuKzJLygS304p458NOfVIQFzlzxnRMSCgCY5YxRRpCCVpkkqWKLyC3E9%2BMC1Ta3f3JELjzSFNqrb8NHDpZqKBMhFWM4iCoxdU83aHfx6NHWf5te2jdu%2B%2BDbp1AJ2XxQR7sHoEemD5QzVG%2FSmN4fTG4wHCsDkWXqDnc52xzu2m%2FwceoOcHlMXDzD11ehNlb2%2FkOCMezD28KNJcKrLTGgtuNCp7kHIaAGyiuaM6Y2HJGs7s2kAtajZi%2FKFWJ%2FXAS8PQEfJlL1TPRMr6dMBkIG6hXSAl%2BjHfRTYXUhKyolid%2B1y%2BxFpuNLMbagQ6sjCBLeXKE5pZjXr285CuLOQPek8S3ELvYW%2Bm2ZMemSbPlSkvNnb4e3N%2FbHltOv%2BOuW03bc3GP96nW0ymFs%2Fi7PZ%2BzmbSPOr3s%2B7KttDL%2B9k1kAjK6F80skMzJpJzax10Hcxtaq2LcXgxH6eqbnOEws9YGq9hY661XdnHbFcZvQgvmj3fbFH1dxmGhpQag7P1aSnOAtjNh4nC8o9cLAw5%2B5UcAEKdZaI2lpNIWcPl4Myt8wbSfNYo%2BrfpeEWdPQ%2F2VSS8gBQnX1xkLf8d%2FYltL4uLvmnBM03lcfWSF0%2B5AqRiktpeNIgYpD6XCe6MLelXqs5WSmRGcgqjerCCqrUCR2qhsBWJ2usvqnjHbqPHykhhur%2BToTsHkLoDaFW1Y9eGKH%2BO67XnkOTtsUi7L4sQv2Xya88h5wT60chBM36B7PCtuqfHfH5Nw%3D%3D).

About indexes, I would add on the columns where I use more the WHERE(FILTER) or JOIN(SELECTED_RELATED) operations to improve the query performance;
