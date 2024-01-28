from class_geo import Geo

class Address:
    def __init__(self, street, suite, city, zipcode, geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = Geo(**geo)