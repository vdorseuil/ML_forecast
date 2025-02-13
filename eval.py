import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error



def MSE(y_pred, y_true):
    return mean_squared_error(y_true, y_pred)

def custom_metric(y_pred, y_true, a=36.97):
    "Return the average loss in € for Germany"
    # a = df_results[(df_results["GERMANY_IMPORT(-)_EXPORT(+)_[MW]"]>0) & (df_results["PRODUCT"] == "POS_00_04")]["GERMANY_IMPORT(-)_EXPORT(+)_[MW]"].mean()
    # C = a*avg_cap_price --> you lost all
    y_t = np.array(y_true)
    y_p= np.array(y_pred)
    loss = (a*np.maximum(y_t-y_p, 0) + a*y_p*(y_t-y_p<0)).mean()*4. #*4 because it lasts 4hours.
    return loss

def S(x, k, p):
    return 1 / (1 + np.exp(-k * (x - p)))

def smooth_custom(y_pred, y_true, a = 36.97, k=3):
    p = np.array(y_true)
    x = np.array(y_pred)
    linear_part = a * np.maximum(p - x, 0)
    constant_part = a * p + a/10*(x-p)
    return (4 * ((1 - S(x, k, p)) * linear_part + S(x, k, p) * constant_part)).mean()

