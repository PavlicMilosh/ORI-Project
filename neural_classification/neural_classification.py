import datetime
import keras
import pandas as pd
import numpy
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

from model.Car import Car


def neural_network_model(x, y, model_path):
    model = Sequential()
    model.add(Dense(6, input_dim=6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(8, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(12, activation='elu'))
    model.add(Dense(30, activation='elu'))
    model.add(Dense(12, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(8, activation='elu'))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x, y, batch_size=128, epochs=1000)

    model.save(model_path)

    return model

def read_input(file):
    forecast_col = "price(eur)"
    df = pd.read_csv(file, delimiter=",")
    df["age"] = df["curr_year"] - df["prod_year"]
    df = df.drop(["curr_year", "prod_year"], 1)
    print(df.head())
    y = numpy.array(df[forecast_col])
    arr = []
    for data in y:
        arr.append(int(data / 15000))
    y = numpy.array(arr)
    x = numpy.array(df.drop([forecast_col], 1))
    x_data, x_test, y_data, y_test = train_test_split(x, y, test_size=0.2)
    return x_data, x_test, y_data, y_test


def convert_to_input(car : Car):
    input_array = []
    input_array.append(car.lux_value())
    input_array.append(car.type_value())
    input_array.append(car.mileage)
    input_array.append(car.ccm)
    input_array.append(car.power)
    input_array.append(datetime.datetime.now().year - car.year)
    return numpy.array([numpy.array(input_array)])

if __name__ == '__main__':
    numpy.random.seed(8)
    input_file = "..\\data\\data\\cars500input.csv"
    model_path = "..\\saved_models\\neural_classification_model.h5"
    x_data, x_test, y_data, y_test = read_input(input_file)
    # model = neural_network_model(x_data, y_data, model_path)
    print(x_test)
    model = keras.models.load_model(model_path)
    tested = model.predict(x_test, batch_size=128)
    err = 0
    errDif = 0
    for i, t in enumerate(tested):
        if round(t[0]) != y_test[i]:
            err += 1
        errDif += abs(round(t[0]) - y_test[i])

    print("Err Difference: " + str(errDif))
    print("Wrong Classifications: " + str(err))
    show_lines = ["BMW,Series 7,31400,2015,2993,280,54900",
                  "BMW,X1,136043,2009,1995,130,12920",
                  "Mercedes-Benz,B-Klasse,265000,2010,1991,80,5390",
                  "Audi,A3,350816,2007,1968,100,3000",
                  "BMW,Series 3,270000,2008,1995,143,9200",
                  "BMW,Series 7,0,2017,6592,448,152000"
                  ]
    for line in show_lines:
        car = Car(line)
        print()
        predicted_class = model.predict(convert_to_input(car))
        print("Predicted price between " + str(int(predicted_class[0][0]) * 15000) + " and " + str((int(predicted_class[0][0] + 1)) * 15000))
        print("Car: " + str(car))