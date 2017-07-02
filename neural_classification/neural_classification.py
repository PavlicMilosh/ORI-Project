import pandas as pd
import numpy
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split


def neural_network_model(x, y, model_path):
    model = Sequential()
    model.add(Dense(7, input_dim=7, kernel_initializer='normal', activation='relu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x, y, batch_size=128, epochs=5000)

    return model

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


if __name__ == '__main__':
    