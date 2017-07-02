import numpy as np
import skfuzzy as fuzz

from model import Car


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
    return type_function(compared.type_value(), given.type_value()) * \
            lux_function(compared.lux_value(), given.lux_value()) * \
            year_function(compared.year, given.year) * \
            power_function(compared.power, given.power) * \
            ccm_function(compared.ccm, given.ccm) * \
            mileage_function(compared.mileage, given.mileage) * \
            price_function(compared.price, given.price)
