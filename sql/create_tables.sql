CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS products (
  product_id uuid,
	product_name VARCHAR ( 50 ) NOT NULL,
	unit_price NUMERIC(5, 2) NOT NULL,
  PRIMARY KEY(product_id)
);

CREATE TABLE IF NOT EXISTS salespeople (
  salesperson_id uuid,
  salesperson_name VARCHAR ( 50 ) NOT NULL,
  PRIMARY KEY(salesperson_id)
);

CREATE TABLE IF NOT EXISTS sales (
  sale_id uuid DEFAULT uuid_generate_v4 (),
  customer_name VARCHAR ( 50 ) NOT NULL,
  salesperson_id uuid NOT NULL,
  product_id uuid NOT NULL,
  quantity_sold integer NOT NULL,
  sale_date DATE NOT NULL,
  PRIMARY KEY(sale_id),
  CONSTRAINT fk_salesperson
      FOREIGN KEY(salesperson_id) 
	    REFERENCES salespeople(salesperson_id), 
  CONSTRAINT fk_product
      FOREIGN KEY(product_id) 
	    REFERENCES products(product_id)
);