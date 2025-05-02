import pandas as pd
import os

os.makedirs("Data/Processed", exist_ok=True)

# 1. Clean Vet_Visit_Cost_Raw.csv
def clean_vet_visit_costs():
    df = pd.read_csv("Data/Raw/Vet_Visit_Cost_Raw.csv")
    df.columns = ["State", "Average Vet Visit Cost"]
    df["Average Vet Visit Cost"] = df["Average Vet Visit Cost"].replace(r'[$,]', '', regex=True).astype(int)

    df.to_csv("Data/Processed/Vet_Visit_Cost_Clean.csv", index=False)
    return df

# 2. Clean Cost_of_living_index_raw.csv
def clean_cost_of_living_index():
    df = pd.read_csv("Data/Raw/Cost_of_living_index_raw.csv")
    df.columns = ["State", "Cost of Living Index"]
    
    df['Cost of Living Index'] = df['Cost of Living Index'].astype(float).round(1)
    
    df.to_csv("Data/Processed/Cost_of_Living_Index_Clean.csv", index=False)
    return df

# 3. Clean Median_Household_Income_Raw.csv
def clean_median_household_income():
    df = pd.read_csv("Data/Raw/Median_Household_Income_by_State.csv")
    df.columns = ["State", "Median Household Income"]
    
    df = df[df["State"] != "United States"]
    
    df['Median Household Income'] = (
        df['Median Household Income']
        .replace(r'[$,]', '', regex=True) 
        .astype(int))

    df.to_csv("Data/Processed/Median_Household_Income_Clean.csv", index=False)
    return df

if __name__ == "__main__":
    clean_vet_visit_costs()
    clean_cost_of_living_index()
    clean_median_household_income()