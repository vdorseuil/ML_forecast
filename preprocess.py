import pandas as pd
import matplotlib.pyplot as plt


file_path_demand = 'donneesAFRR/LIST_OF_TENDERS_CAPACITY_MARKET_aFRR_2024-01-01_2024-08-31.xlsx'
df_demand = pd.read_excel(file_path_demand, sheet_name=None)["001"]
df_demand = df_demand.drop(columns=['APG_AREA_CORE_PORTION_[MW]'])


file_path_results = "donneesAFRR/RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2024-01-01_2024-08-31.xlsx"
# Read all sheets into a dictionary of DataFrames
df_results = pd.read_excel(file_path_results, sheet_name=None)["001"]

df_results = df_results.apply(lambda col: col.astype('string') if col.dtype == 'object' else col)
result = df_results["PRODUCT"][0]


y_austria = df_results.loc[df_results['PRODUCT'] == result, ["AUSTRIA_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]"]].squeeze()
y_germany = df_results.loc[df_results['PRODUCT'] == result, ["GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]"]].squeeze()


df_info = {"y_austria" : y_austria, "y_germany" : y_germany}