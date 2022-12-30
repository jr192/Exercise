# Exercise
Using 2 datasets, one contains orders from customers and another contains barcodes (with an order_id if they are sold).
To print the tickets vouchers we need a csv file with all the barcodes and orders_ids per customer.
I writed a program that reads these two files, orders.csv and barcodes.csv, and generates an output file that contains the following data:
customer_id, order_id1, [barcode1, barcode2, ...] 
customer_id, order_id2, [barcode1, barcode2, ...]

Features added:
 ● The top 5 customers that bought the most amount of tickets.
 ● Print the amount of unused barcodes (barcodes left)

orders.csv
order_id, customer_id
This contains a list of orders. order_id is unique.

barcodes.csv
barcode, order_id
The barcodes. If a barcode has been sold, it’s assigned to an order using order_id, otherwise order_id is empty.

Validation:
● No duplicate barcodes
● No orders without barcodes
Items which failed the validation are logged (e.g. stderr) and ignored for the output.

The requests collections used are on [Tiqets.postman_collection.json] file.

## Installation

Let's use Docker to simplify the requirements dependency and virtualize the run environment. This will ensure that
everything goes by smoothly.


### Setup with Docker
Setup to run api:
 - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - In Repository root run: 
 1)  run `cp dev.env .env` && `docker compose build` 
 2) `docker compose up —wait db` 
 3) `docker compose up` 
 4) open a new terminal window and run `docker-compose exec web python manage.py makemigrations --noinput` and `docker-compose exec web python manage.py migrate --noinput` 
 5) close all the windows and run `docker compose down` and `docker compose up` 
 - After this setup you just need to run the api a simple command: `docker compose up`and to stop `docker compose down`
 

### HOW TO UPDATE FILES?
I created two endpoints to handle the file (see postman collections above, please) and another get endpoint to retrieve all the answers.  
