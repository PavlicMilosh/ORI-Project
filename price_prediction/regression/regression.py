import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, RANSACRegressor, HuberRegressor, TheilSenRegressor
import pickle
import datetime
from model.Car import Car


def predict(clf, X):
    forecast_set = clf.predict(X)
    print(forecast_set)


def load_classifier(path):
    f = open(path, "rb")
    model = pickle.load(f)
    f.close()
    return model


def train(df, save_path):
    forecast_col = "price(eur)"

    Y = np.array(df[forecast_col])
    X = np.array(df.drop([forecast_col], 1))
    X_test, X_train, Y_test, Y_train = train_test_split(X, Y, test_size=0.25)

    clf = LinearRegression()
    clf.fit(X_train, Y_train)

    with open(save_path, "wb") as f:
        pickle.dump(clf, f)

    print('Coefficients: \n', clf.coef_)
    print('Variance score: %.4f' % clf.score(X_test, Y_test))


def load_data(path):
    df = pd.read_csv(path)
    df['age'] = df['curr_year'] - df['prod_year']
    df['mileage(km)'] = df['mileage(km)']
    df['price(eur)'] = df['price(eur)']
    df['ccm'] = df['ccm']
    df['power(kW)'] = df['power(kW)']
    df = df.drop(['curr_year', 'prod_year', 'type'], 1)

    # df = df.drop(['mileage(km)'], 1)
    print(df.head())
    return df


def generate_input_data(car: Car, years):
    now = datetime.datetime.now()
    car_age = now.year - car.year
    added = []
    for i in range(1, years + 1):
        added.append([car.lux_value(),
                      (car.mileage+(i*20000)),
                      car.ccm,
                      car.power,
                      car_age + i])
    df = pd.DataFrame(columns=("lux",
                               "mileage(km)",
                               "ccm",
                               "power(kw)",
                               "age"),
                      data=added)
    X = np.array(df)
    return X


if __name__ == '__main__':
    data_path = "..\\..\\data\\data\\cars500input.csv"
    classifier_path = "..\\..\\saved_models\\linear_regression.pickle"

    train(load_data(data_path), classifier_path)
    clf = load_classifier(classifier_path)

    car = Car("Audi,A1,6500,2017,1000,63,15950")
    years = 5
    X = generate_input_data(car, years)

    predict(clf, X)