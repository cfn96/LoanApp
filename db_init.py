import sqlite3
from dict import *
import os

# auto-create and connect to the main db
con = sqlite3.connect(path_maindb)

cur = con.cursor()

res = cur.execute("SELECT COUNT(*) from sqlite_master")

table_count = res.fetchone()

# auto-create table structure
if table_count[0] == 0:
    # create customers table
    cur.execute(
        "CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT, amount REAL)")
    # create payment history table
    cur.execute(
        "CREATE TABLE payment_hist(id INTEGER, amount REAL,payment_date DATETIME NOT NULL DEFAULT(DATETIME('now')))")

# FUNCTIONS


def loadrecord(pTable):
    maindb_tables = {
        "customer": "SELECT * FROM customers",
        "paymenthist": "SELECT * FROM paymenthist"
    }
    res = cur.execute(maindb_tables.get(pTable))
    return res.fetchall()


customer_record = loadrecord("customer")

for customer in customer_record:
    print(customer)