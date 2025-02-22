# ML Forecast

This repository contains various machine learning models and experiments aimed at forecasting equilibrium prices in the aFRR (automatic Frequency Restoration Reserve) market for Germany and Austria. The goal is to predict the equilibrium price for a given product using different machine learning techniques. This project was developed as part of the *Machine Learning for Forecasting* course by M. Yannig Goude.

## Project Overview

The aFRR market is a system service market operating in several European countries to help maintain grid balance. Each day, market participants submit bids in an auction, and based on supply and demand, an equilibrium price is determined.

This project applies time series prediction methods to forecast the daily equilibrium price in this market for Austria and Germany.

### Data

The dataset includes market data for Germany and Austria over an 8-month period, consisting of:
- **Demand**: Daily demand data for each product.
- **Auction Results Statistics**: Includes statistics on accepted bids, such as equilibrium prices and volumes.
- **Accepted Bids**: Detailed breakdown of all accepted bids for Germany and Austria on a daily basis.
- **External Features**: Two CSV files (one for Austria and one for Germany) containing daily weather data.

### Project Goal

Using these features, the objective is to predict the equilibrium price for each product. The equilibrium prices are listed in the columns:
- `AUSTRIA_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]`
- `GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]`

within the result overview dataset.

## Models and Experiments

The repository is structured as follows:

### Installation
Install the necessary dependencies using:
  ```
  pip install -r requirements.txt
  ```

### Global Scripts and Files:
- `preprocess.py`: Script for data preprocessing.
- `baseline.py`: Implements a baseline model for comparison.
- `eval.py`: Contains functions for evaluating models using various metrics.


### Jupyter Notebooks for Model Testing and Exploration:
- `exploration.ipynb`: Data exploration and visualization.
- `cart.ipynb`: Decision tree-based models, including a variant incorporating Ridge regression in each leaf.
- `random_forest.ipynb`: Training and evaluation of a Random Forest model.
- `gam.ipynb`: Experiments with Generalized Additive Models (GAM).
- `aggregation.ipynb`: Techniques for aggregating different models to improve prediction performance.

This project provides a comprehensive exploration of machine learning techniques for time series forecasting in the aFRR market, helping to better understand and predict equilibrium prices in Germany and Austria.

