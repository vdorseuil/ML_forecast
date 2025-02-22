from preprocess import data
from eval import MSE, custom_metric, MAE

y_ger = data['y_austria']
y_true = y_ger[1:]
y_pred = 0.8*y_ger.shift(1)[1:] + 0.8

print("MSE all:", MSE(y_pred[100:], y_true[100:]))
print("MAE all:", MAE(y_pred[100:], y_true[100:]))
print("customm all:", custom_metric(y_pred[100:], y_true[100:], country="Austria"))