import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression, RANSACRegressor, HuberRegressor, TheilSenRegressor
import pickle


def predict(clf, input):
    print('Coefficients: \n', clf.coef_)
    #print('Variance score: %.4f' % clf.score(X_test, Y_test))


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

    clf = LinearRegression(n_jobs=-1, normalize=True)
    clf.fit(X_train, Y_train)

    with open(save_path, "wb") as f:
        pickle.dump(clf, f)

    print('Coefficients: \n', clf.coef_)
    print('Variance score: %.4f' % clf.score(X_test, Y_test))


def load_data(path):
    df = pd.read_csv(path)
    df['age'] = df['curr_year'] - df['prod_year']
    df = df.drop(['model'], 1)
    df = df.drop(['curr_year'], 1)
    df = df.drop(['prod_year'], 1)
    df = df.drop(['mileage(km)'], 1)
    return df


if __name__ == '__main__':

    data_path = "..\\..\\data\\data\\cars500input.csv"
    classifier_path = "..\\..\\saved_models\\linear_regression.pickle"

    #train(load_data(data_path), classifier_path)

    clf = load_classifier(classifier_path)
    predict(clf, "")





