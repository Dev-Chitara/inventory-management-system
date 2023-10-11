import uuid
import csv


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


p1 = Product("Apple", "Apple is very delicious", 20, 4)
p2 = Product("Mango", "Mango is very delicious", 25, 2)
p3 = Product("Banana", "Banana is very delicious", 30, 4)
p4 = Product("Grapes", "Grapes is very delicious", 40, 20)
p5 = Product("Watermelon", "Watermelon is very delicious", 35, 1)
p6 = Product("Strawberry", "Strawberry is very delicious", 30, 10)


def get_products():
    list1 = []
    file = open("./db/products.csv", "r")
    reader = csv.DictReader(file)

    for item in reader:
        list1.append(item["name"])

    file.close()
    return list1

# print(get_products())


instance = [p1, p2, p3, p4]

# This fuction for store product dictionary in list


def list_of_products(persons):
    lst = []
    for i in persons:
        lst.append(i.get_product_details())
    return lst


l = list_of_products(instance)


def create_products():
    file = open("./db/products.csv", "w")

    fields = ["id", "name", "description", "price", "quantity"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(l)
    file.close()

# create_products()


def get_product(id):

    file = open("./db/products.csv", "r")
    reader = csv.DictReader(file)

    for item in reader:
        if item["id"] == id:
            print(item)
    file.close()

# get_product("5c0e3e7d-c44d-4e07-8e41-152777468cb2")


def update_product(id, name, description, price, quantity):
    pass


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
