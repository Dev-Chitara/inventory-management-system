import uuid
import csv

FIELDS = ["id", "name", "description", "price", "quantity"]
FILE_PATH = "./db/products.csv"


class Product:

    def __init__(self, name, description, price, quantity):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        
        

    def _validation(self, data): 
        valid_type = { 
            "name": str,
            "description": str,
            "price": float,
            "quantity": int
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
        self.quantity = kwargs.get("quantity", self.quantity)


    def get_product_details(self):
        return self.__dict__


def get_products():
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        for item in reader:
            records.append(item)
        return records


def create_products(name, description, price, quantity):
    p = Product(name, description, price, quantity)
    d = p.get_product_details()

    file = open(FILE_PATH, "a")
    writer = csv.DictWriter(file, fieldnames=FIELDS)
    writer.writerow(d)
    file.close()


def get_product(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"]==id:
                return item
    

def update_product(id, name, description, price, quantity):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for row in reader:
            if row["id"]==id:
                row["name"]=name
                row["description"]=description
                row["price"]=price
                row["quantity"]=quantity

                is_exists = True
            records.append(row)

    if is_exists:
        with open(FILE_PATH, "w") as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(records)
            reader = csv.DictReader(file)         
    else:
        return (is_exists, "Product does not exists")
    
    return (is_exists, "Succesfully updated")


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
            reader = csv.DictReader(file)         
    else:
        return (is_exists, "Product does not exists")
    
    return (is_exists, "Succesfully deleted")



# initialization of a product
# set values of a product  - update object values
# get values of a product - return dictionary


# . get_products  - list of products
# 2. create_products - initialize and save products
# 3. get_product -  return single details of a product
# 4. update_product - update and return single details of a product
# 5. delete_product - delete a product
