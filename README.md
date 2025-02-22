# ML Forecast

This repository contains various machine learning models and experiments for forecasting equilibrium prices in the aFRR (automatic Frequency Restoration Reserve) market for Germany and Austria. The project aims to predict the equilibrium price for a given product using different machine learning techniques. This project took place for the course *Machine Learning for Forecasint* by M.Yannig Goude.

## Project Overview

The aFRR market is a system service market in several European countries designed to help maintain grid balance. Participants in the market submit offers to either increase or decrease electricity production based on real-time demand, providing flexibility to the electricity system.

### How it Works

1. **Auction Setup**:
   - The aFRR auctions occur daily around 8 a.m., for electricity delivery the next day.
   - Each day features 12 product types, which represent the need to either increase or decrease production within four-hour slots (e.g., POS_00_04 for increased production from 00:00–04:00).
   - These products are treated as independent, each having a specific demand published in advance.

2. **Pricing Mechanism**:
   - Market participants submit bid curves (volume/price), which are sorted by price.
   - The equilibrium price for each product is set by the highest-priced offer that meets the required demand.

### The Data

The datasets contain data about the aFRR market for Germany and Austria over a period of 8 months:
- **Demand**: Data on the demand for each product for each day over a period of 8 months.
- **Auction Results Stats**: File with statistics of the accepted bids (equilibrium price, volume, etc.).
- **Accepted Bids**: Files showing all accepted bids, with breakdowns for Germany and Austria, for each product daily.
- **External Features** : Two csv (Austria and Germany) with daily weather data.

### The Project

Given all these features, the goal is to predict the equilibrium price for a given product (or for all products if possible). The equilibrium prices are listed in the columns "AUSTRIA_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]" and "GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]" in the result overview dataset.

## Models and Experiments

### Generalized Additive Models (GAM)

The `gam.ipynb` notebook contains experiments with Generalized Additive Models (GAM) using the `pyGAM` library. The models are trained to predict the equilibrium prices using various features and smoothing terms.

### Decision Trees and Random Forests

The `cart.ipynb` and `random_forest.ipynb` notebooks contain experiments with Decision Trees and Random Forests using the `scikit-learn` library. The models are trained to predict the equilibrium prices using various features and hyperparameters.

## Baseline 

The `baseline.py` script contains baseline models for comparison. The baseline models use simple heuristics to predict the equilibrium prices.

## Evaluation

The `eval.py` script contains functions for evaluating the models using various metrics, including Mean Squared Error (MSE), Mean Absolute Error (MAE), and a custom metric specific to the aFRR market.

## Preprocessing

The `preprocess.py` script contains functions for preprocessing the data, including loading the datasets, merging external features, and preparing the data for modeling.

## Requirements
You can install the requirements needed for this projecte as follow : 
```pip install - r requirements.txt```