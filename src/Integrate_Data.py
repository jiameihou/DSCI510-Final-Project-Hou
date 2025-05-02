import pandas as pd
import os

def integrate_data():
    vet = pd.read_csv("Data/Processed/Vet_Visit_Cost_Clean.csv")
    col = pd.read_csv("Data/Processed/Cost_of_Living_Index_Clean.csv")
    income = pd.read_csv("Data/Processed/Median_Household_Income_Clean.csv")

    merged = vet.merge(col, on="State")
    merged = merged.merge(income, on="State")

    os.makedirs("Data/Processed", exist_ok=True)
    merged.to_csv("Data/Processed/Integrated_Data.csv", index=False)
    return merged

if __name__ == "__main__":
    integrate_data()