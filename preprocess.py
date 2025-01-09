import pandas as pd
import matplotlib.pyplot as plt


def preprocess():
    file_path_demand = (
        "donneesAFRR/LIST_OF_TENDERS_CAPACITY_MARKET_aFRR_2024-01-01_2024-08-31.xlsx"
    )
    df_demand = pd.read_excel(file_path_demand, sheet_name=None)["001"]
    df_demand = df_demand.drop(columns=["APG_AREA_CORE_PORTION_[MW]"])

    file_path_results = (
        "donneesAFRR/RESULT_OVERVIEW_CAPACITY_MARKET_aFRR_2024-01-01_2024-08-31.xlsx"
    )
    df_results = pd.read_excel(file_path_results, sheet_name=None)["001"]
    df_results = df_results.apply(
        lambda col: col.astype("string") if col.dtype == "object" else col
    )

    product = df_results["PRODUCT"][0] #POS_00_04

    x_germany = df_demand.loc[
        df_demand["PRODUCT"] == product,
        [
            "DATE_FROM",
            "GERMANY_BLOCK_DEMAND_[MW]",
            "GERMANY_BLOCK_EXPORT_LIMIT_[MW]",
            "GERMANY_BLOCK_CORE_PORTION_[MW]",
        ],
    ]
    x_austria = df_demand.loc[
        df_demand["PRODUCT"] == product,
        [           
            "DATE_FROM",
            "AUSTRIA_BLOCK_DEMAND_[MW]",
            "AUSTRIA_BLOCK_EXPORT_LIMIT_[MW]",
            "AUSTRIA_BLOCK_CORE_PORTION_[MW]",
        ],
    ]

    x_tl = df_results.loc[
        df_results["PRODUCT"] == product,
        [
            "TOTAL_MIN_CAPACITY_PRICE_[(EUR/MW)/h]",
            "TOTAL_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]",
            "TOTAL_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]",
            "GERMANY_MIN_CAPACITY_PRICE_[(EUR/MW)/h]",
            "GERMANY_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]",
            "GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]",
            "GERMANY_IMPORT(-)_EXPORT(+)_[MW]",
            "AUSTRIA_MIN_CAPACITY_PRICE_[(EUR/MW)/h]",	
            "AUSTRIA_AVERAGE_CAPACITY_PRICE_[(EUR/MW)/h]",
            "AUSTRIA_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]",
            "AUSTRIA_IMPORT(-)_EXPORT(+)_[MW]",
            "GERMANY_SUM_OF_OFFERED_CAPACITY_[MW]",
        ]
    ]

    y_austria = df_results.loc[
        df_results["PRODUCT"] == product,
        [
            "AUSTRIA_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]"
        ],
    ].squeeze() #pandas.Series

    y_germany = df_results.loc[
        df_results["PRODUCT"] == product,
        [
            "GERMANY_MARGINAL_CAPACITY_PRICE_[(EUR/MW)/h]"
        ],
    ].squeeze() #pandas.Series



    return {
            "y_austria": y_austria, 
            "y_germany": y_germany, 
            "x_austria": x_austria,
            "x_germany": x_germany,
            "x_timed_lagged": x_tl
        }


data = preprocess()