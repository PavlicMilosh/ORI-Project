import datetime

import numpy
from keras.layers import Dense, Activation
from keras.models import Sequential
import pandas as pd
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from model.Car import Car


def data_converter(read_path, save_path):
    input_file = open(read_path, "r")
    output_file = open(save_path, "w")
    i = 0
    for line in input_file.readlines():
        if i == 0:
            i += 1
            output_file.write("lux,type,mileage(km),prod_year,ccm,power(kW),curr_year,price(eur)\n")
            continue
        car = Car(line)
        output_file.write(car.get_input_data(datetime.datetime.now().year))
    input_file.close()
    output_file.close()


def read_input(file):
    forecast_col = "price(eur)"
    df = pd.read_csv(file, delimiter=",")
    df["age"] = df["curr_year"] - df["prod_year"]
    print(df.head())
    df = df.drop(["curr_year"], 1)
    df = df.drop(["prod_year"], 1)
    y = numpy.array(df[forecast_col])
    x = numpy.array(df.drop([forecast_col], 1))
    x_data, x_test, y_data, y_test = train_test_split(x, y, test_size=0.2)
    return x_data, y_data, x_test, y_test


def neural_network_model():
    model = Sequential()
    model.add(Dense(6, input_dim=6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')

    model.fit(x, y, epochs=100)
    model.save(save_path)
    return model


if __name__ == '__main__':

    save_path = "..\\..\\saved_models\\carPricePredictionModel.h5"
    data_converter("..\\..\\data\\data\\cars500fixed.csv", "..\\..\\data\\data\\cars500input.csv")
    x_data, y_data, x_test, y_test = read_input("..\\..\\data\\data\\cars500input.csv")
    model = neural_network_model(x_data, y_data, save_path)
    # model = keras.models.load_model(save_path)
    model.evaluate(x_test, y_test)
    tested = model.predict(x_test)
    err = 0
    for i, t in enumerate(y_test):
        err += (tested[i] - t) ** 2
        print(abs(tested[i] - t))
    print("\nerror: " + str(err / len(y_test)))




