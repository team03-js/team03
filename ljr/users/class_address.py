from ljr.users.class_geo import Geo

class Address:
    def __init__(self, userId, street, suite, city, zipcode, geo):
        self.userId = userId
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = Geo(**geo)
