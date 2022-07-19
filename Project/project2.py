import csv
from cs50 import SQL
open ('mydata.db','w').close()
database = SQL("sqlite:///mydata.db")
brancheset = set()
employee_name = set()
database.execute(""" CREATE TABLE IF NOT EXISTS branches(
    branch_number INTEGER PRIMARY KEY,
    branch_name TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS branches_visited(
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_value INTEGER,
    worker_id INTEGER
    branch_value REFERENCES branches(branch_number) ON DELETE CASCADE
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_sex TEXT,
    customer_password TEXT,
    employee_assistant INTEGER,
    customer_phone INTEGER,
    customer_email TEXT,
    sex TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    employee_sex TEXT,
    branch_id INTEGER,
    client_id INTEGER,
    FOREIGN KEY(branch_id) REFERENCES branches_visited(branch_id)
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS customer_rooms(
    room_number INTEGER,
    room_star INTEGER,
    arrival_date TEXT,
    customer_id INTEGER,
    departure_date TEXT,
    bags INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(room_star) REFERENCES branch_star_type(star_id)
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS branch_star_type(
    star_id INTEGER PRIMARY KEY AUTOINCREMENT,
    star_types INTEGER,
    star_value TEXT,
    packages INTEGER,
    branch_id INTEGER,
    total_amount INTEGER,
    paid_amount INTEGER,
    balance INTEGER,
    FOREIGN KEY(branch_id) REFERENCES branches_visited(branch_id)
    );""")
with open ('customers.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        brancheset.add(row["Branch"])
        employee_name.add(row["Employees"])
    number = [115,114,113,112,116]
    for branch,i in zip(brancheset,number):
        branch_ids = database.execute("INSERT INTO branches(branch_number,branch_name) VALUES(?,?);",i,branch)
with open ('customers.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        room_number = row['Room_number']
        employee_sex = row['Employee_sex']
        star = row['Star_type']
        package = row['Packages']
        room_type = row['Room_type']
        total_amount = row['Total_amount']
        cash_payed = row['Cash_payed']
        balance = row['Balance']
        branch_id = row['Branch_id']
        customer_id = row['Customer_id']
        customer_name = row['Customer_name']
        customer_password = row['Password']
        employee_assistant = row['Employees']
        customer_phone = row['Phone_number']
        customer_email = row['Email']
        arrival_date= row['Arrival_date']
        departure_date = row['Departure_date']
        bags = row['Bags']
        sex = row['Customer_Sex']
        branches=row['Branch']
        workers = row['Employee_id']
        star_value = row['Hotel_value']
        man = database.execute("INSERT INTO branches_visited(branch_value) VALUES(?)",branch_id)
        database.execute("INSERT INTO customers(customer_id,customer_name,customer_sex,customer_password,employee_assistant,customer_phone,customer_email,sex) VALUES(?,?,?,?,?,?,?,?);",customer_id,customer_name,sex,customer_password,employee_assistant,customer_phone,customer_email,sex)
        database.execute("INSERT INTO employees(employee_name,employee_sex,branch_id,client_id) VALUES(?,?,(SELECT branch_id FROM branches_visited WHERE branch_id = ?),?);",employee_assistant,employee_sex,man,customer_id)
        men = database.execute("INSERT INTO branch_star_type(star_types,star_value,packages,branch_id,total_amount,paid_amount,balance)VALUES (?,?,?,(SELECT branch_id FROM branches_visited WHERE branch_id = ?),?,?,?)",star,star_value,package,man,total_amount,cash_payed,balance)
        database.execute("INSERT INTO customer_rooms(room_number,room_star,arrival_date,customer_id,departure_date,bags)VALUES (?,(SELECT star_id FROM branch_star_type WHERE star_id = ?),?,?,?,?)",room_number,men,arrival_date,customer_id,departure_date,bags)