import uuid
import csv
from functools import wraps


class Product:

    def __init__(self, name, description, price, quantity):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def set_product(self, new_name, new_description, new_price, new_quantity):
        if type(self.name) == str:
            self.name = new_name
        else:
            print("Invalid Name")

        if type(self.description) == str:
            self.description = new_description
        else:
            print("Invalid Description")

        if type(self.price) == int:
            self.price = new_price
        else:
            print("Invalid Amount")

        if type(self.quantity) == int:
            self.quantity = new_quantity
        else:
            print("Invalid Quantity")

    def get_product_details(self):
        return self.__dict__


# p1 = Product("Apple", "Apple is very delicious", 20, 4)
# p2 = Product("Mango", "Mango is very delicious", 25, 2)
# p3 = Product("Banana", "Banana is very delicious", 30, 4)
# p4 = Product("Grapes", "Grapes is very delicious", 40, 20)
# p5 = Product("Watermelon", "Watermelon is very delicious", 35, 1)
# p6 = Product("Strawberry", "Strawberry is very delicious", 30, 10)


def get_products():
    list1 = []
    file = open("./db/products.csv", "r")
    reader = csv.DictReader(file)

    for item in reader:
        list1.append(item["name"])

    file.close()
    return list1



def create_products(product,name, description, price, quantity):
    p=product(name, description, price, quantity)
    d=p.get_product_details()
    file = open("./db/products.csv", "a")

    fields = ["id", "name", "description", "price", "quantity"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writerow(d)
    file.close()

# create_products(Product,"Apple", "Apple is very delicious", 20, 4)
# create_products(Product,"Mango", "Mango is very delicious", 25, 2)
# create_products(Product,"Banana", "Banana is very delicious", 30, 4)
# create_products(Product,"Grapes", "Grapes is very delicious", 40, 20)
# create_products(Product,"Watermelon", "Watermelon is very delicious", 35, 1)
# create_products(Product,"Strawberry", "Strawberry is very delicious", 30, 10)

def get_product(id):

    file = open("./db/products.csv", "r")
    reader = csv.DictReader(file)

    for item in reader:
        if item["id"]==id:
            print(item)
    file.close()
    

# get_product("6478da5e-82b7-44e4-825b-deac414639e3")


def update_product(id, name, description, price, quantity):
    file = open("./db/products.csv", "r+")
    reader = csv.DictReader(file)

    L=[]
    found=False

    for row in reader:
        if row["id"]==id:
            found=True
            row["name"]=name
            row["description"]=description
            row["price"]=price
            row["quantity"]=quantity
        L.append(row)
    file.close()
    if found==False:
        print("Fruit not Found")
    else:
        file=open("./db/products.csv","w+",newline="")
        fields = ["id", "name", "description", "price", "quantity"]
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writerows(L)
        file.seek(0)
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        file.close()
update_product("95e0f7e8-4715-4dbf-be57-50c41eb94a70","pappya", "Apple is very delicious", 20, 4)



def delete_product(id):
    pass


# initialization of a product
# set values of a product  - update object values
# get values of a product - return dictionary


# . get_products  - list of products
# 2. create_products - initialize and save products
# 3. get_product -  return single details of a product
# 4. update_product - update and return single details of a product
# 5. delete_product - delete a product
