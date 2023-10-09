import uuid

class Product:
    def __init__(self,name,description,price,quantity):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price 
        self.quantity = quantity

    def update_quantity(self,new_quantity):
        if type(new_quantity)==int:
            self.quantity = new_quantity
        else:
            print("Invalid Quantity")

    def get_product_details(self):
        return f"""Product Name is : {self.name}
Product Price is : {self.price}
and Quantity is : {self.quantity}"""
    
      
def initializing_obj(name,description,price,quantity):
    return Product(name,description,price,quantity)

