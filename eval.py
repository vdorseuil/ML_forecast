import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error



def MSE(y_pred, y_true):
    "Computes the MSE and the std of the squared errors"
    squared_errors = (np.array(y_true) - np.array(y_pred)) ** 2
    plt.hist(squared_errors, bins=1000, label="MSE")
    plt.xscale('log')
    return squared_errors.mean(), squared_errors.std()
def MAE(y_pred, y_true):
    absolute_errors = np.abs(np.array(y_true)-np.array(y_pred))
    return absolute_errors.mean(), absolute_errors.std()


def custom_metric(y_pred, y_true, country):
    """Computes the custom metric, mean and std

    Args:
        y_pred (np.array): pred
        y_true (np.array): ground truth
        country (str): Germany or Austria

    """
    a = 0.
    if country == "Germany":
        a = 36.97
    elif country == "Austria":
        a = 59.89


    # a = df_results[(df_results["GERMANY_IMPORT(-)_EXPORT(+)_[MW]"]>0) & (df_results["PRODUCT"] == "POS_00_04")]["GERMANY_IMPORT(-)_EXPORT(+)_[MW]"].mean()
    # C = a*avg_cap_price --> you lost all
    y_t = np.array(y_true)
    y_p= np.array(y_pred)
    loss = (a*np.maximum(y_t-y_p, 0) + a*y_p*(y_t-y_p<0))*4. #*4 because it lasts 4hours.
    # plt.hist(loss, bins=1000, label="Custom")
    # plt.xscale('log')
    # plt.legend()
    # plt.savefig("losses_hist.png")
    return loss.mean(), loss.std()

def S(x, k, p):
    return 1 / (1 + np.exp(-k * (x - p)))

def smooth_custom(y_pred, y_true, a = 36.97, k=3):
    p = np.array(y_true)
    x = np.array(y_pred)
    linear_part = a * np.maximum(p - x, 0)
    constant_part = a * p + a/10*(x-p)
    return (4 * ((1 - S(x, k, p)) * linear_part + S(x, k, p) * constant_part)).mean()

