import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

from dataGathering import Car


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
    val = fuzz.gbellmf(compared, 5, 3, c)
    return val


def power_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.gbellmf(compared, 5, 3, c)
    return val


def ccm_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.gbellmf(compared, 5, 3, c)
    return val


def mileage_function(x, c):
    compared = np.arange(x, x + 100, 1)
    val = fuzz.sigmf(compared, c + 25, -0.1)
    plt.plot(compared, val, linewidth=2.0)
    plt.show()
    return val


def price_function(x, c):
    compared = np.arange(x, x + 1, 1)
    val = fuzz.gbellmf(compared, 0.15*c, 3, c)
    return val


def calculate(compared: Car, given: Car):
    return type_function(compared.type_value(), given.type_value()) * \
            lux_function(compared.lux_value(), given.lux_value()) * \
            year_function(compared.year, given.year) * \
            power_function(compared.power, given.power) * \
            ccm_function(compared.ccm, given.ccm) * \
            mileage_function(compared.mileage/1000, given.mileage/1000) * \
            price_function(compared.price, given.price)

if __name__ == '__main__':
    print(mileage_function(170, 200))
