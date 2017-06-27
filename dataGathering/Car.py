class Car:

    lux = {"A1":10, "A-Klasse":12, "A3":20, "B-Klasse":22, "1 Series":25,
           "A4":50, "C-Klasse":53, "3 Series":55, "X1":71, "Q3":70, "GLK-Klasse":73,
           "A5":99, "6 Series":100, "A7":102, "X3":145, "Q5":143, "GLC":140,
           "5 Series":165, "A6":163, "E-Klasse":160,
           "X4":190, "GLE-Klasse":203, "X6":205, "Q7":200, "X5":210,
           "G-Klasse":235, "GL-Klasse":230,
           "A8":250, "7 Series":255, "S-Klasse":253}

    type = {"A1":1, "A-Klasse":1, "A3":2, "B-Klasse":2, "1 Series":2,
            "A4":5, "C-Klasse":5, "3 Series":5,
            "A5":15, "6 Series":15, "A7":15,
            "5 Series":10, "A6":10, "E-Klasse":10,
            "A8":12, "7 Series":12, "S-Klasse":12,
            "X1":28, "Q3":28, "GLK-Klasse":28,
            "X3":30, "Q5":30, "GLC-Klasse":30,
            "X5":33, "Q7":33,
            "X4":40, "X6":40, "GLE-Klasse":40}

    def __init__(self):
        self.make = ""
        self.model = ""
        self.mileage = 0
        self.year = 0
        self.ccm = 0
        self.power = 0
        self.price = 0

    def lux_value(self):
        return self.lux[self.model]

    def type_value(self):
        return self.type[self.model]

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




