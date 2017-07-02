

if __name__ == '__main__':

    makes = ["Audi", "BMW", "Mercedes-Benz"]
    models = {
        "BMW": ["Series 1", "Series 3", "Series 5", "Series 6", "Series 7", "X1", "X3", "X4", "X5", ""
                                                                                                    "X6"],
        "Mercedes-Benz": ["A-Klasse", "B-Klasse", "C-Klasse", "E-Klasse", "S-Klasse", "G-Klasse", "GLA-Klasse", "GLC-Klasse", "GLE-Klasse", "GLK-Klasse", "GL-Klasse"],
        "Audi": ["A1", "A3", "A4", "A5", "A6", "A7", "A8", "Q3", "Q5", "Q7"]}

    make = model = year = price = ccm = power = mileage = 0

    while True:
        print(">> 1. Audi")
        print(">> 2. BMW")
        print(">> 3. Mercedes-Benz")
        make = input(">> Make: ")
        try:
            make = int(make)
            if make > 3 or make < 1:
                print(">> Error: Please enter value in {1, 2, 3}")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        valid_set = []
        for i, model in enumerate(models[makes[make]]):
            print(">> " + str(i) + ". " + str(model))
            valid_set.append(i)
        model = input(">> Model: ")
        try:
            model = int(model)
            if model not in valid_set:
                print(">> Error: Please enter value in " + str(valid_set))
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        year = input(">> Production year: ")
        try:
            year = int(year)
            if year < 2007 or year > 2017:
                print(">> Error: Please enter a year between 2007 and 2017")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        price = input(">> Price: ")
        try:
            price = int(price)
            if price < 0:
                print(">> Error: Please enter a value greater than or equal to 0")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        ccm = input(">> Cubic capacity: ")
        try:
            ccm = int(ccm)
            if ccm < 0:
                print(">> Error: Please enter a value greater than or equal to 0")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        power = input(">> Power: ")
        try:
            power = int(power)
            if power < 0:
                print(">> Error: Please enter a value greater than or equal to 0")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")

    while True:
        mileage = input(">> Mileage: ")
        try:
            mileage = int(mileage)
            if mileage < 0:
                print(">> Error: Please enter a value greater than or equal to 0")
            else:
                break
        except ValueError:
            print(">> Error: Please enter a number")


    print("E SADE KIDA FUZIKA")