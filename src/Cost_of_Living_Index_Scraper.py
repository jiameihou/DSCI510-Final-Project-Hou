import pandas as pd

url = "https://worldpopulationreview.com/state-rankings/cost-of-living-index-by-state"
tables = pd.read_html(url)

df = tables[0]
df = df [["State", "Cost of Living Index 2024↓"]]
df.columns = ["State", "Cost of living index"]
df.to_csv("Cost_of_living_index_raw.csv", index=False)