import pandas as pd
from sqlalchemy.exc import IntegrityError

from model import db

from model import customer
import pandas as pd

data = db.get_engine()  # db is the one from the question
file_csv = 'Customer.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="customer",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Product.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="product",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Instructor.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="instructor",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Course.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="course",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Order.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="order",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Cart.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="cart",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Needed.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="needed",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Enrolls.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="enrolls",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Purchased.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="purchased",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Adminlogin.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="adminlogin",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Customerlogin.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="customerlogin",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Instructorlogin.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="instructorlogin",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action


