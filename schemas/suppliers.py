import uuid
class Supplier:
    def __init__(self,name,contact_info):
        self.id = uuid.uuid4()
        self.name = name
        self.contact_info = contact_info

    def supplier_details(self):
        return f"""Supplier Name is : {self.name}
and Supplier Contact Number is : {self.contact_info }"""
    
def initializing_obj(name,contact_info):
        return Supplier(name,contact_info)

s1=initializing_obj("Rahul","123456789")
print(s1.supplier_details())