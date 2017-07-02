class Car:

    lux = {"A1":10, "A-Klasse":12, "A3":20, "B-Klasse":22, "Series 1":25,
           "A4":50, "C-Klasse":53, "Series 3":55, "X1":71, "Q3":70, "GLK-Klasse":73,
           "A5":99, "Series 6":100, "A7":102, "X3":145, "Q5":143,
           "Series 5":165, "A6":163, "E-Klasse":160,
           "X6":205, "Q7":200, "X5":210, "ML-Klasse":212,
           "A8":240, "Series 7":245, "S-Klasse":243}

    type = {"A1":1, "A-Klasse":1, "A3":2, "B-Klasse":2, "Series 1":2,
            "A4":5, "C-Klasse":5, "Series 3":5,
            "A5":15, "Series 6":15, "A7":15,
            "Series 5":10, "A6":10, "E-Klasse":10,
            "A8":12, "Series 7":12, "S-Klasse":12,
            "X1":28, "Q3":28, "GLK-Klasse":28,
            "X3":30, "Q5":30,
            "X5":33, "Q7":33, "ML-Klasse":33,
            "X6":40}

    def __init__(self):
        self.make = ""
        self.model = ""
        self.mileage = 0
        self.year = 0
        self.ccm = 0
        self.power = 0
        self.price = 0

    def __init__(self, str):
        data = str.split(",")
        self.make = data[0]
        self.model = data[1]
        self.mileage = int(data[2])
        self.year = int(data[3])
        self.ccm = int(data[4])
        self.power = int(data[5])
        self.price = int(data[6])

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
               str(self.mileage) + "," + \
               str(self.year) + "," + \
               str(self.ccm) + "," + \
               str(self.power) + "," + \
               str(self.price)

    def get_input_data(self, current_year):
        return str(self.lux[self.model]) + "," + \
               str(self.type[self.model]) + "," + \
               str(self.mileage) + "," + \
               str(self.year) + "," + \
               str(self.ccm) + "," + \
               str(self.power) + "," + \
               str(current_year) + "," + \
               str(self.price) + "\n"


