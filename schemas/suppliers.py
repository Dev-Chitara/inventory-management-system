import uuid
import csv

FILE_PATH = "./db/suppliers.csv"
FIELDS = ["id", "name", "contact_number"]

class Supplier:

    def __init__(self, name, contact_number):
        self.id = uuid.uuid4()
        self.name = name
        self.contact_number = contact_number


    def _validation(self,data):
        valid_type = {
            "name": str,
            "contact_number": int
        }

        for item in data:
            if type(data.get(item)) != valid_type.get(item):
                return f"Cannot set invalid value :{item}"
            
            elif data.get(item):
                return f"Cannot set an empty value : {item}"
            

    def set_supplier(self, **kwargs):
        invalid = self._validation(kwargs)

        if invalid:
            return invalid
        
        self.name = kwargs.get("name", self.name)
        self.contact_number = kwargs.get("contact_number", self.contact_number)


    def get_supplier_details(self):
        return self.__dict__
    

def get_suppliers():
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        for item in reader:
            records.append(item)
        return records


def create_suppliers(name, contact_number):
    supplier = Supplier(name, contact_number)
    supplier_dict = supplier.get_supplier_details()

    with open(FILE_PATH, "a") as file:
        writer = csv.DictWriter(file, FIELDS)
        writer.writerow(supplier_dict)


def get_supplier(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file, FIELDS)

        for item in reader:
            if item["id"] == id:
                return item


def update_supplier(id, name, contact_number):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file,FIELDS)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] == id:
                item["name"] = name
                item["contact_number"] = contact_number
                is_exists = True
            records.append(item)

        if is_exists:
            with open(FILE_PATH, "w") as file:
                writer = csv.DictWriter(file, FIELDS)
                writer.writeheader()
                writer.writerows(records)
        else:
            return (is_exists, "supplier does not exists")
        
        return (is_exists,"Sucessfully updated")


def delete_supplier(id):
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file,FIELDS)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] != id:
                is_exists = True
                records.append(item)

        if is_exists:
            with open(FILE_PATH, "w") as file:
                writer = csv.DictWriter(file, FIELDS)
                writer.writerows(records)
        else:
            return (is_exists, "supplier does not exists")
        
        return (is_exists,"Sucessfully deleted")


        

        






    













# . get_products  - list of products
# 2. create_products - initialize and save products
# 3. get_product -  return single details of a product
# 4. update_product - update and return single details of a product
# 5. delete_product - delete a product