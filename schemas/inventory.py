import uuid
import csv
from products import get_products
from suppliers import get_suppliers

FILE_PATH = "./db/inventory.csv"

FIELDS = ["id", "name", "location", "inventory_type", "product_ids", "supplier_ids"]


def product_id_list():
    ids = []

    for item in get_products():
        ids.append(item["id"])
    return ids


def supplier_id_list():
    ids = []

    for item in get_suppliers():
        ids.append(item["id"])
    return ids


class Inventory:
    def __init__(self,name, location, inventory_type, product_ids = product_id_list(), supplier_ids = supplier_id_list()):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.inventory_type = inventory_type
        self.product_ids = product_ids
        self.supplier_ids = supplier_ids

    
    def _validation(self, data):
        valid_type = {
            "name": str,
            "location": str,
            "inventory_type": str
        }

        for item in data:
            if type(data.get(item)) != valid_type.get(item):
                return f"Cannot set invalid value :{item}"
            
            elif data.get(item):
                return f"Cannot set an empty value :{item}"
            

    def set_inventory(self, **kwargs):
        invalid = self._validation(kwargs)

        if invalid:
            return invalid
            
        self.name = kwargs.get("name", self.name)
        self.location = kwargs.get("location", self.location)
        self.inventory_type = kwargs.get("inventory_type", self.inventory_type)


    def get_inventory_details(self):
        return self.__dict__
        

def get_inventory_list():
    with open(FILE_PATH,"r") as file:
        reader = csv.DictReader(file)

        inventory_list = []
        for item in reader:
            inventory_list.append(item)
        return inventory_list


def create_inventory(name, location, inventory_type):
    inventory = Inventory(name, location, inventory_type)
    inventory_dict = inventory.get_inventory_details()

    with open(FILE_PATH,"a") as file:
        writer = csv.DictWriter(file, fieldnames = FIELDS)
        writer.writerow(inventory_dict)


def get_inventory(id):
    with open(FILE_PATH,"r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"] == id:
                return item
            

def update_inventory(id, name, location, inventory_type):
    with open(FILE_PATH,"r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] == id:
                item["name"] = name
                item["location"] = location
                item["inventory_type"] = inventory_type
                is_exists = True
            records.append(item)

    if is_exists:
        with open(FILE_PATH,"w") as file:
            writer = csv.DictWriter(file, fieldnames = FIELDS)
            writer.writeheader()
            writer.writerows(records)
    else:
        return (is_exists, "Inventory does not exists") 
    
    return (is_exists,"Successfully updated")
    
def delete_inventory(id):
    with open(FILE_PATH,"r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] != id:
                is_exists = True
                records.append(item)

    if is_exists:
        with open(FILE_PATH,"w") as file:
            writer = csv.DictWriter(file, fieldnames = FIELDS)
            writer.writeheader()
            writer.writerows(records)
    else:
        return (is_exists, "Inventory does not exists") 
    
    return (is_exists,"Successfully deleted")

# create_inventory("Fruits","Ahmedabad","Fruit")
# create_inventory("Dryfruits","Jamnagar","Dry")
# create_inventory("Colddrinks","Surat","Drinks")
# create_inventory("Vegitables","Ahmedabad","Veg")

# print(get_inventory_list())

# print(get_inventory("d4e62f03-b3b9-4a56-8ee2-f8069a92ee2c"))

# print(update_inventory("6b345ab5-f635-4631-aa2c-2133b968e7eb","Fruits","Junagadh","Fruit"))

# print(delete_inventory("4c8080c3-1fbf-4364-919e-bffdce3824e2"))

#1 id,inventory_name,location,type,products(id),suppliers(id)

#1 show_inventory - suppliers + products

# . get_inventory  - list of inventory
# 2. create_inventory - initialize and save inventory
# 3. get_inventory -  return single details of a inventory
# 4. update_inventory - update and return single details of a inventory
# 5. delete_inventory - delete a inventory
