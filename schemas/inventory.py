import uuid
import csv
from schemas.products import get_products
from schemas.suppliers import get_suppliers


FILE_PATH = "/home/dev/workspace/projects/inventory-management-system/db/inventory.csv"
FIELDS = ["id", "name", "location", "inventory_type", "product_ids", "supplier_ids"]


class Inventory:
    def __init__(self,name, location, inventory_type, product_ids = [], supplier_ids = []):
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
        

    def add_product_id(self):
        for item in get_products():
            self.product_ids.append(item["id"]) 


    def add_supplier_id(self):
        for item in get_suppliers():
            self.supplier_ids.append(item["id"])    


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

