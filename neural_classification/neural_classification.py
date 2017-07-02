import keras
import pandas as pd
import numpy
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split


def neural_network_model(x, y, model_path):
    model = Sequential()
    model.add(Dense(6, input_dim=6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(8, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(12, activation='elu'))
    model.add(Dense(25, activation='elu'))
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
    print(df.head())
    df = df.drop(["curr_year", "prod_year"], 1)
    y = numpy.array(df[forecast_col])
    arr = []
    for data in y:
        arr.append(int(data / 15000))
    y = numpy.array(arr)
    print(y)
    x = numpy.array(df.drop([forecast_col], 1))
    x_data, x_test, y_data, y_test = train_test_split(x, y, test_size=0.2)
    return x_data, x_test, y_data, y_test


if __name__ == '__main__':
    numpy.random.seed(7)
    input_file = "..\\data\\data\\cars500input.csv"
    model_path = "..\\saved_models\\neural_classification_model.h5"
    x_data, x_test, y_data, y_test = read_input(input_file)
    model = neural_network_model(x_data, y_data, model_path)
    # model = keras.models.load_model(model_path)
    tested = model.predict(x_test, batch_size=128)
    err = 0
    for i, t in enumerate(tested):
        if round(t[0]) != y_test[i]:
            err += 1
        print("\n" + str(t) + "\t" + str(y_test[i]))

    print("\n" + str(err))