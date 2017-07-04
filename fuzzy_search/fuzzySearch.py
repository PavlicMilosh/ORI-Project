import numpy as np
import skfuzzy as fuzz

from model.Car import Car


# m treba da se postavi na trazeni auto, a primer je ret vrednost
# x - vrednost sa kojom se uporedjuje
# c - centar (ono sto korisnik trazi)
def lux_function(x, c):
    compared = np.arange(x, x+1, 1)
    val = fuzz.gbellmf(compared, 4, 0.5, c)
    return val


def type_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.trimf(compared, [c-8, c, c+8])
    return val


def year_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.sigmf(compared, c - 3, 1)
    return val


def power_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.gbellmf(compared, 25, 5, c+10)
    return val


def ccm_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.trimf(compared, [c-600, c, c+110])
    return val


def mileage_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.sigmf(compared, c + 25000, -1 / 10000)
    return val


def price_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.sigmf(compared, c * 1.3, -20 / c)
    return val


def calculate(compared: Car, given: Car):
    search_val = type_function(compared.type_value(), given.type_value()) * \
                 lux_function(compared.lux_value(), given.lux_value()) * \
                 year_function(compared.year, given.year) * \
                 power_function(compared.power, given.power) * \
                 ccm_function(compared.ccm, given.ccm) * \
                 mileage_function(compared.mileage, given.mileage) * \
                 price_function(compared.price, given.price)
    compared.search_val = search_val


def read_data(path):
    f = open(path, "r")
    i = 0
    cars_data = []
    for line in f.readlines():
        if i == 0:
            i += 1
            continue
        cars_data.append(Car(line))
    f.close()
    return cars_data


def sort(given: Car, data):
    for car in data:
        calculate(compared=car, given=given)
    return sorted(data)


if __name__ == '__main__':

    data_path = "..\\data\\data\\cars500fixed.csv"
    data = read_data(data_path)

    show_lines = ["BMW,Series 7,31400,2015,2993,280,54900",
                  "BMW,X1,136043,2009,1995,130,12920",
                  "Mercedes-Benz,B-Klasse,265000,2010,1991,80,5390",
                  "Audi,A3,350816,2007,1968,100,3000",
                  "BMW,Series 3,270000,2008,1995,143,9200",
                  "BMW,Series 7,0,2017,6592,448,152000"
                  ]
    for line in show_lines:
        print("============================================================")
        given = Car(line)
        data = sort(given=given, data=data)
        for i in range(0, 100):
            print(str(data[i]))
