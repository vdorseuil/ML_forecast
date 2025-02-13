from preprocess import data
from eval import MSE, custom_metric

y_ger = data['y_germany']
y_true = y_ger[1:]
y_pred = y_ger.shift(1)[1:]

print("MSE all:", MSE(y_pred[100:], y_true[100:]))
print("customm all:", custom_metric(y_pred[100:], y_true[100:]))