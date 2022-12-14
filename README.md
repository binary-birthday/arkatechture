# Code challenge for Arkatechture

## Instructions

### Phase 1

To run this you'll need docker and docker compose installed on your local machine.

Intructions for how to install each can be found at https://docs.docker.com/engine/install/ (Docker) & https://docs.docker.com/compose/install/ (Docker Compose)

- First, clone this repo to your machine.

- Change directories to the one containing the cloned repository.

- In the root folder create a .env file

  `touch .env`

- Add the required environment variables to the .env file

  - DB="postgres"
  - DB_HOST="db"
  - DB_USER="postgres"
  - DB_PASSWORD="postgres"
  - DB_PORT="5432"

- In your terminal run:

  `docker compose up -d`

  This will build the containers and initilize the postgres database with the create_tables.sql file and populate the database with the data from the csv files.

### Phase 2

Question 1: Who was the highest performing salesman in the month of November?

In your terminal run:

    docker compose exec db psql -U postgres -c "select salespeople.salesperson_name from sales inner join salespeople on sales.salesperson_id = salespeople.salesperson_id inner join products on sales.product_id = products.product_id where extract(month from sale_date) = 11 group by salespeople.salesperson_name order by sum(sales.quantity_sold * products.unit_price) desc limit 1";

See /arkatechture/sql/query_1.sql

Answer 1: Celka Nys

Question 2: What is the lowest selling product?

In your terminal run:

    docker compose exec db psql -U postgres -c "select products.product_name from sales inner join products on sales.product_id = products.product_id group by products.product_name order by sum(sales.quantity_sold) asc limit 1";

See /arkatechture/sql/query_2.sql

Answer 2: Onion Powder

Question 3: What is the day with the highest sales?

In your terminal run:

    docker compose exec db psql -U postgres -c "select sales.sale_date from sales inner join products on sales.product_id = products.product_id group by sales.sale_date order by sum(sales.quantity_sold * products.unit_price) desc limit 1";

See /arkatechture/sql/query_3.sql

Answer 3: 2020-11-12
