from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from flask_migrate import Migrate
import datetime
import dbconfig

app = Flask(__name__);

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/hobiburada'


db = SQLAlchemy(app)

class customer(db.Model):
    __tablename__ = 'customer'
    cust_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    cust_fname = db.Column(db.String(80))
    cust_lname = db.Column(db.String(80))
    cust_phone=db.Column(db.String)
    cust_address = db.Column(db.String)
    cust_bday = db.Column(db.Date)

    def __init__(self, cust_fname, cust_lname, cust_bday, cust_phone, cust_address):
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.cust_bday = cust_bday
        self.cust_phone = cust_phone
        self.cust_address = cust_address

class course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    course_name = db.Column(db.String(80))
    course_category = db.Column(db.String(80))
    course_level=db.Column(db.Integer)
    course_price = db.Column(db.Integer)
    course_duration = db.Column(db.Integer)
    course_inst_id = db.Column(db.Integer,db.ForeignKey('inst.inst_id'))

    def __init__(self, course_name, course_category, course_level, course_price, course_duration, course_inst_id):
        self.course_name = course_name
        self.course_category = course_category
        self.course_level = course_level
        self.course_price = course_price
        self.course_duration = course_duration
        self.course_inst_id = course_inst_id

class product(db.Model):
    __tablename__ = 'product'
    prod_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    prod_name = db.Column(db.String(80))
    prod_brand = db.Column(db.String(80))
    prod_weight = db.Column(db.Float)
    prod_price = db.Column(db.Integer)
    prod_instock = db.Column(db.Integer)
    
    def __init__(self, prod_name, prod_brand, prod_weight, prod_price, prod_instock):
        self.prod_name = prod_name
        self.prod_brand = prod_brand
        self.prod_weight = prod_weight
        self.prod_price = prod_price
        self.prod_instock = prod_instock
        
class instructor(db.Model):
    __tablename__ = 'instructor'
    inst_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    inst_fname = db.Column(db.String(80))
    inst_lname = db.Column(db.String(80))
    inst_contact = db.Column(db.String)
    inst_phone = db.Column(db.String)
    inst_avgrate = db.Column(db.Float)
    
    def __init__(self, inst_fname, inst_lname, inst_contact, inst_phone, inst_avgrate):
        self.inst_fname = inst_fname
        self.inst_lname = inst_lname
        self.inst_contact = inst_contact
        self.inst_avgrate = inst_avgrate
        self.inst_phone = inst_phone

class order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    order_totalprice = db.Column(db.Integer)
    order_quantity = db.Column(db.Integer)
    order_date = db.Column(db.Date)
    order_totalweight = db.Column(db.Float)
    order_shippingfee = db.Column(db.Float)
    order_state = db.Column(db.String)
    
    def __init__(self, order_totalprice, order_quantity, order_date, order_totalweight, order_shippingfee, order_state):
        self.order_totalprice = order_totalprice
        self.order_quantity = order_quantity
        self.order_date = order_date
        self.order_totalweight = order_totalweight
        self.order_shippingfee = order_shippingfee
        self.order_state = order_state

class cart(db.Model):
    __tablename__ = 'cart'
    cart_cust_id = db.Column(db.Integer,db.ForeignKey('cust.cust_id'),primary_key=True)
    cart_prod_id = db.Column(db.Integer,db.ForeignKey('prod.prod_id'),primary_key=True)
    cart_prodcount = db.Column(db.Integer)
    
    def __init__(self, cart_cust_id, cart_prod_id, cart_prodcount):
        self.cart_cust_id = cart_cust_id
        self.cart_prod_id = cart_prod_id
        self.cart_prodcount = cart_prodcount

class needed(db.Model):
    __tablename__ = 'needed'
    needed_prod_id = db.Column(db.Integer,db.ForeignKey('prod.prod_id'),primary_key=True)
    needed_course_id = db.Column(db.Integer,db.ForeignKey('course.course_id'),primary_key=True)
    
    def __init__(self, needed_prod_id, needed_course_id):
        self.needed_course_id = needed_course_id
        self.needed_prod_id = needed_prod_id

class enrolls(db.Model):
    __tablename__ = 'enrolls'
    enrolls_prod_id = db.Column(db.Integer,db.ForeignKey('cust.cust_id'),primary_key=True)
    enrolls_course_id = db.Column(db.Integer,db.ForeignKey('course.course_id'),primary_key=True)
    
    def __init__(self, enrolls_prod_id, enrolls_course_id):
        self.enrolls_course_id = enrolls_course_id
        self.enrolls_prod_id = enrolls_prod_id

class purchased(db.Model):
    __tablename__ = 'purchased'
    purchased_prod_id = db.Column(db.Integer,db.ForeignKey('prod.prod_id'),primary_key=True)
    purchased_cust_id = db.Column(db.Integer,db.ForeignKey('cust.cust_id'),primary_key=True)
    purchased_order_id = db.Column(db.Integer,db.ForeignKey('order.order_id'),primary_key=True)
    def __init__(self, enrolls_prod_id, enrolls_course_id):
        self.enrolls_course_id = enrolls_course_id
        self.enrolls_prod_id = enrolls_prod_id

                

db.create_all()