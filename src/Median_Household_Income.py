import pandas as pd

url = "https://worldpopulationreview.com/state-rankings/median-household-income-by-state" 
tables = pd.read_html(url)

df = tables[0]
df = df [["State" , "Median Household Income↓"]]
df.columns = ["State", "Median Household Income"]
df.to_csv("Median_Household_Income_by_State.csv", index=False)