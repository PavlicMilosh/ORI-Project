import keras
from keras.layers import Dense
from keras.models import Sequential
import datetime
import h5py

import numpy

from dataGathering.Car import Car


def data_converter(input, output):
    inputFile = open(input, "r")
    outputFile = open(output, "w")
    for line in inputFile.readlines():
        car = Car(line)
        outputFile.write(car.get_input_data(datetime.datetime.now().year))

    inputFile.close()
    outputFile.close()


def read_input(file):
    dataset = numpy.loadtxt(file, delimiter=",")
    x = dataset[:, 0:7]
    y = dataset[:, 7]
    return x, y


def neural_network_model(x, y):
    model = Sequential()
    model.add(Dense(10, input_dim=7))
    model.add(Dense(10))
    model.add(Dense(10))
    model.add(Dense(10))
    model.add(Dense(1))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x, y, epochs=1000000, batch_size=10)
    model.save("carPricePredictionModel")
    return model


if __name__ == '__main__':
    data_converter("..\\data\\cars500fixed.csv", "..\\data\\cars500input.csv")
    x, y = read_input("..\\data\\cars500input.csv")
    # model = neural_network_model(x, y)
    model = keras.models.load_model("carPricePredictionModel")
    dataset = numpy.loadtxt("..\\data\\cars500input.csv", delimiter=",")
    x = dataset[:, 0:7]
    values = model.predict(x)
    for index, value in enumerate(values):
        print(dataset[index][7] - value)

