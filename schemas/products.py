import uuid
import csv

FIELDS = ["id", "name", "description", "price"]
FILE_PATH = "./inventory_management_system/db/products.csv"


class Product:

    def __init__(self, name, description, price):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        
        
    def _validation(self, data): 
        valid_type = { 
            "name": str,
            "description": str,
            "price": float,
        }   
            
        for item in data:
            if type(data.get(item)) != valid_type.get(item):
                return f"Cannot set invalid value :{item}"
            
            elif data.get(item):
                return f"Cannot set an empty value :{item}"
            

    def set_product(self, **kwargs):
            
        invalid = self._validation(kwargs)

        if invalid:
            return invalid 
        
        self.name = kwargs.get("name", self.name)
        self.description = kwargs.get("description", self.description)
        self.price = kwargs.get("price", self.price)


    def get_product_details(self):
        return self.__dict__


def get_products():
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        for item in reader:
            records.append(item)
        return records


def create_products(name, description, price):
    product = Product(name, description, price)
    product_dict = product.get_product_details()

    with open(FILE_PATH, "a") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(product_dict)
    

def get_product(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"] == id:
                return item
    

def update_product(id, name, description, price):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for row in reader:
            if row["id"]==id:
                row["name"]=name
                row["description"]=description
                row["price"]=price

                is_exists = True
            records.append(row)

    if is_exists:
        with open(FILE_PATH, "w") as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(records)        
    else:
        return (is_exists, "Product does not exists")
    
    return (is_exists, "Sucessfully updated")


def delete_product(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for row in reader:
            if row["id"] != id:
                is_exists = True
                records.append(row)
    
    if is_exists:
        with open(FILE_PATH, "w") as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(records)         
    else:
        return (is_exists, "Product does not exists")
    
    return (is_exists, "Succesfully deleted")

