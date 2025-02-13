# Results

Les résultats sont évalués ici pour la MSE et la Custom Metric, en précisant sur quoi ça a été entraîné, et sur quoi c'est évalué.

Pour l'entraînement on distingue on adopte la stratégie suivante:
- On entraîne notre model à prédire y[t+1] en l'ayant entraîner sur y[t] avec t >= 100.
- Exemple pour le baseline :  MSE(y_true_shifted[100:], y_true[100:])

Idem pour l'évaluation on doit préciser sur quoi on évalue:
- On évalue le modèle sur sa prédiction à 1 jour.
- Pourquoi pas à 7 jours plus tard




| Modèle | Entraînement | Évaluation | MSE mean | MSE std |Custom mean| Custom std|
|-----------|-----------|-----------| --------- | ---------| ----- | ----- |
| Baseline (y_pred = y_true[t-1])| Aucun | 1 jour| 83.8 | 1284| 1144.6| 1577|

