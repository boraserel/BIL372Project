import pandas as pd
from sqlalchemy.exc import IntegrityError

from model import db

from model import   Cart,Course,Customer,Enrolls,Instructor,Needed,Order,Product,Purchased
import pandas as pd

data = db.get_engine()  # db is the one from the question
file_csv = 'Cart.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Cart",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Course.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Course",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Customer.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Customer",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Enrolls.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Enrolls",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Instructor.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Instructor",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Needed.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Needed",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Order.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Order",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Product.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Product",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action

file_csv = 'Purchased.csv'

# Read CSV with Pandas
with open(file_csv, 'r', encoding='utf-8-sig') as file:
    dcsv = pd.read_csv(file)

# Insert to DB
for i in range(len(dcsv)):
    try:
        dcsv.iloc[i:i+1].to_sql(name="Purchased",if_exists='append',con = data,index=False)
    except IntegrityError:
        pass #or any other action
