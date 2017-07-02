import datetime

import keras
import numpy
from keras.layers import Dense
from keras.models import Sequential
import pandas as pd
from sklearn.model_selection import train_test_split

from model.Car import Car


def data_converter(input, output):
    inputFile = open(input, "r")
    outputFile = open(output, "w")
    for line in inputFile.readlines():
        car = Car(line)
        outputFile.write(car.get_input_data(datetime.datetime.now().year))

    inputFile.close()
    outputFile.close()


def read_input(file):
    daframe = pd.read_csv(file, delimiter=",")
    x = numpy.array(daframe)
    y = numpy.array()
    xData, yData, xTest, yTest = train_test_split(dataset)
    return x, y


def neural_network_model(x, y):
    model = Sequential()
    model.add(Dense(10, input_dim=7))
    model.add(Dense(10))
    model.add(Dense(10))
    model.add(Dense(10))
    model.add(Dense(1))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x, y, epochs=5000, batch_size=10)
    model.save("carPricePredictionModel")
    return model


if __name__ == '__main__':
    data_converter("..\\data\\cars500fixed.csv", "..\\data\\cars500input.csv")
    xData, yData, xTest, yTest = read_input("..\\data\\cars500input.csv")
    # model = neural_network_model(x, y)
    model = keras.models.load_model("carPricePredictionModel")
    dataset = numpy.loadtxt("..\\data\\cars500input.csv", delimiter=",")
    a = model.evaluate(x, y)


