from peewee import *
import datetime

db = SqliteDatabase("inventory.db")


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = CharField(unique=True)
    description = TextField(null=True)
    price = FloatField(default=0)
    stock = IntegerField(default=0)  


class Supply(BaseModel):
    product = ForeignKeyField(Product, backref="supplies")
    quantity = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)


class Sale(BaseModel):
    product = ForeignKeyField(Product, backref="sales")
    quantity = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)


def init_db():
    db.connect()
    db.create_tables([Product, Supply, Sale])
