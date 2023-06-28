-- SQL-команды для создания таблиц

CREATE TABLE customer_data
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
)

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date date,
	notes text
)

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customer_data(customer_id) NOT NULL,
	employee_id int REFERENCES employees_data(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(50)
)

SELECT * FROM customer_data
SELECT * FROM employees_data
SELECT * FROM orders_data