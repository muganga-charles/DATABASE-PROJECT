--Sql Statements
CREATE TABLE branches
(
    branch_number integer PRIMARY KEY,
    branch_name text
);
CREATE TABLE branches_visited
(
    branch_id integer PRIMARY KEY,
    branch_value integer

CREATE TABLE employees
(
    employee_id integer PRIMARY KEY,
    employee_name text,
    employee_sex text,
    branch_id integer,
    client_id integer
);

CREATE TABLE branch_star_type
(
     star_id integer PRIMARY KEY,
    star_types integer,
    star_value text,
    package integer,
    branch_id integer,
    total_amount integer,
    paid_amount integer,
    balance integer
);
CREATE TABLE customers
(
    customer_id integer PRIMARY KEY,
    customer_name text,
    customer_sex text,
    customer_password text,
    employee_assistant integer,
    customer_phone integer,
    customer_email text,
    sex text
);

CREATE TABLE customer_rooms
(
    room_number integer,
    room_star integer,
    arrival_date text,
    customer_id integer,
    departure_date text,
    bags integer

);
ALTER TABLE branch_star_type ADD FOREIGN KEY (branch_id) REFERENCES branch_visited(branch_id);
ALTER TABLE branch_star_type ADD FOREIGN KEY (star_id) REFERENCES customer_rooms(room_star);
ALTER TABLE customer_rooms ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
ALTER TABLE branches_visited ADD FOREIGN KEY (branch_value) REFERENCES branches(branch_number);
ALTER TABLE employees ADD FOREIGN KEY (branch_id) REFERENCES branches_visited(branch_id);
ALTER TABLE employees ADD FOREIGN KEY (client_id) REFERENCES customers (customer_id);

