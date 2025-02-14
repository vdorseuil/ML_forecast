# Results

Les résultats sont évalués ici pour la MSE et la Custom Metric, en précisant sur quoi ça a été entraîné, et sur quoi c'est évalué.

Pour l'entraînement on distingue on adopte la stratégie suivante:
- On entraîne notre model à prédire y[t+1] en l'ayant entraîner sur y[t] avec t >= 100.
- Exemple pour le baseline :  MAE(y_true_shifted[100:], y_true[100:])

Idem pour l'évaluation on doit préciser sur quoi on évalue:
- On évalue le modèle sur sa prédiction à 1 jour.
- Pourquoi pas à 7 jours plus tard




| Modèle | Pays | Entraînement | Évaluation | MAE mean | MAE std |Custom mean| Custom std|
|-----------|-----|-----------|-----------| --------- | ---------| ----- | ----- |
| Baseline (y_pred = y_true[t-1])|Germany| Aucun | 1 jour| 2.6 | 8.7| 1144.6| 1577|
| Baseline (y_pred = y_true[t-1])|Austria| Aucun | 1 jour| 0.7 | 1.23| 1165| 953|

