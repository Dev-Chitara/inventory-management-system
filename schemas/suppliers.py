import uuid


class Supplier:

    def __init__(self,name,contact_info):
        self.id = uuid.uuid4()
        self.name = name
        self.contact_info = contact_info


    



