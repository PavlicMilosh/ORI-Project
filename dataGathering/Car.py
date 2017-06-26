class Car:

    def __init__(self):
        self.make = ""
        self.model = ""
        self.mileage = 0
        self.year = 0
        self.ccm = 0
        self.power = 0
        self.price = 0

    def make_value(self):
        return 0

    def model_value(self):
        return 0

    def __str__(self):
        return "make= " + self.make + \
               "; model= " + self.model + \
               "; mileage= " + self.mileage + \
               "; year= " + self.year + \
               "; ccm= " + self.ccm + \
               "; power= " + self.power + \
               "; price= " + self.price

    def get_line(self):
        #make,model,mileage,year,ccm,power,price
        return self.make + "," + \
               self.model + "," + \
               self.mileage + "," + \
               self.year + "," + \
               self.ccm + "," + \
               self.power + "," + \
               self.price + ","




