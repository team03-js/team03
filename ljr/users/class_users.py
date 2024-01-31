from ljr.users.class_address import Address
from ljr.users.class_company import Company

class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.address = kwargs('address')
        self.phone = kwargs('phone')
        self.website = kwargs.get('website')
        self.company = kwargs.get('company')
