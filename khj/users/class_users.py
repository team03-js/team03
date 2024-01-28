from class_address import Address
from class_company import Company

class Users:
    def __init__(self, id, name, username, email, address, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = Address(**address)
        self.phone = phone
        self.website = website
        self.company = Company(**company)