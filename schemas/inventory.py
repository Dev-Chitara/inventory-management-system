import uuid
import csv
from schemas.products import get_products
from schemas.suppliers import get_suppliers


FILE_PATH = "./inventory_management_system/db/inventory.csv"
FIELDS = ["id", "name", "location", "inventory_type", "product_stock"]


class Inventory:
    def __init__(self,name, location, inventory_type, product_stock = []):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.inventory_type = inventory_type
        self.product_stock = product_stock


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


    def add_product_stock(self):
        self.product_stock = []

        self.product_stock.append(get_products())
        self.product_stock.append(get_suppliers())



def get_inventory_list():
    with open(FILE_PATH,"r") as file:
        reader = csv.DictReader(file)

        inventory_list = []
        for item in reader:
            inventory_list.append(item)
        return inventory_list


def create_inventory(name, location, inventory_type, product_stock):
    inventory = Inventory(name, location, inventory_type, product_stock)
    inventory_dict = inventory.get_inventory_details()

    with open(FILE_PATH, "a") as file:
        writer = csv.DictWriter(file, fieldnames = FIELDS)
        writer.writerow(inventory_dict)


def get_inventory(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"] == id:
                return item
            

def update_inventory(id, name, location, inventory_type):
    with open(FILE_PATH, "r") as file:
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
        with open(FILE_PATH, "w") as file:
            writer = csv.DictWriter(file, fieldnames = FIELDS)
            writer.writeheader()
            writer.writerows(records)
    else:
        return (is_exists, "Inventory does not exists") 
    
    return (is_exists,"Successfully updated")


def delete_inventory(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] != id:
                is_exists = True
                records.append(item)

    if is_exists:
        with open(FILE_PATH, "w") as file:
            writer = csv.DictWriter(file, fieldnames = FIELDS)
            writer.writeheader()
            writer.writerows(records)
    else:
        return (is_exists, "Inventory does not exists") 
    
    return (is_exists,"Successfully deleted")

# products - > product_stock - product_id , quantity, supplier_id (list of dictionary) 

# id,name,location,inventory_type,product_stock
# 6b345ab5-f635-4631-aa2c-2133b968e7eb,Fruits,Junagadh,Fruit
# bc9552b6-487c-46db-97e0-3ddef05696d0,Dryfruits,Jamnagar,Dry
# 7f76f3df-f504-431d-8ec3-5aed4f202334,Electronics,Rajkot,Electronics

# create_inventory("Fruits", "Junagadh", "Fruit", "33160059-9103-41bb-8828-22a96662d2fb", "97ab0f05-89c1-435c-9ec5-71fc05b6353c", 20)
# create_inventory("Fruits", "Junagadh", "Fruit", "444a497d-1b4b-4adb-ac3d-ee269d238678", "2e768f3b-dfa9-43dd-94ee-52b10ee1e7fd", 15)
# create_inventory("Fruits", "Junagadh", "Fruit", "5681e482-51e7-4f37-84bb-7e6de1888d0a", "86472266-80e2-4dca-afe6-8acb1bbb3060", 30)
# create_inventory("Fruits", "Junagadh", "Fruit", "b1524357-13c7-47cb-981f-74c62ddb5878", "04026ba0-e93f-43a7-8611-a5e83b818b21", 25)
# create_inventory("Fruits", "Junagadh", "Fruit", "33160059-9103-41bb-8828-22a96662d2fb", "b7f9227b-cd09-488d-bc13-d805aa0c2d35", 20)