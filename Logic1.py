from Database1 import Product, Supply, Sale


# ---------- Работа с товарами ----------

def add_product(name, description, price):
    return Product.create(
        name=name,
        description=description,
        price=float(price),
        stock=0
    )


def edit_product(product_id, name, description, price):
    p = Product.get_by_id(product_id)
    p.name = name
    p.description = description
    p.price = float(price)
    p.save()
    return p


def delete_product(product_id):
    p = Product.get_by_id(product_id)
    p.delete_instance()


def get_all_products():
    return list(Product.select())


# ---------- Поставки ----------

def supply_product(product_id, qty):
    p = Product.get_by_id(product_id)
    qty = int(qty)

    Supply.create(product=p, quantity=qty)
    p.stock += qty
    p.save()


# ---------- Продажи ----------

def sell_product(product_id, qty):
    p = Product.get_by_id(product_id)
    qty = int(qty)
    
    if qty > p.stock:
        raise ValueError("Недостаточно товара на складе!")

    Sale.create(product=p, quantity=qty)
    p.stock -= qty
    p.save()


# ---------- История операций ----------

def get_supply_history():
    return list(Supply.select().order_by(Supply.date.desc()))


def get_sales_history():
    return list(Sale.select().order_by(Sale.date.desc()))
