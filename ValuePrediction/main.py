import pdb

from model import Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
    if len(inputs) != len(outputs):
        raise Exception('Length of "inputs" does not match length of "outputs".')

    df = pd.DataFrame({'inputs':inputs, 'outputs':outputs})

    X = np.array(df['inputs']).reshape(-1,1)
    y = np.array(df['outputs']).reshape(-1,1)

    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.2)

    model = LinearRegression()
    model.fit(train_X, train_y)

    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    y_test_prediction = model.predict(test_X)
    #pdb.set_trace()
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)


    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y,y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y,y_test_prediction))


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')
    plt.plot(inputs,y_line, color='r')
    plt.show()

if __name__ == '__main__':
    years: list[float] = [2005,2007, 2013, 2015 , 2018, 2020, 2021, 2022, 2023, 2024, 2025]
    salary: list[float] = [0, 13000, 15000, 35000 ,60000, 50000, 55000, 60000, 77000, 98000, 100000]
    my_input: int = 2026
    predicted_salary = make_prediction(inputs=years, outputs=salary, input_value=my_input,plot=True)

    print(predicted_salary)