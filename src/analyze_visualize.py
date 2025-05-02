import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("Results", exist_ok=True)

df = pd.read_csv("Data/Processed/Integrated_Data.csv")

df["VCBI"] = (df["Average Vet Visit Cost"] * df["Cost of Living Index"])/df["Median Household Income"]

# Plot 1: Horizontal Bar Chart of VCBI Ranked by State
vcbi_sorted = df.sort_values("VCBI", ascending=False)

plt.figure(figsize=(10,12))
sns.barplot(x="VCBI", y="State", data=vcbi_sorted, palette="coolwarm")
plt.xlabel("Veterinary Cost Burden Index (VCBI)")
plt.ylabel("State")
plt.title("VCBI by State (Ranked)")
plt.tight_layout()
plt.savefig("Results/VCBI_Ranked_By_State.png")
plt.close()

# Plot 2: Scatter Plot of Vet Cost vs. Median Household Income
plt.figure(figsize=(8,6))
sns.regplot(x="Median Household Income", y="Average Vet Visit Cost", data=df)
plt.xlabel("Median Household Income ($)")
plt.ylabel("Average Vet Visit Cost ($)")
plt.title("Vet Visit Cost vs. Median Household Income")
plt.tight_layout()
plt.savefig("Results/Vet_Cost_vs_Median_Income.png")
plt.close()

# Plot 3: Scatter Plot - Vet Cost vs. Cost of Living Index
plt.figure(figsize=(8,6))
sns.regplot(x="Cost of Living Index", y="Average Vet Visit Cost", data=df)
plt.xlabel("Cost of Living Index")
plt.ylabel("Average Vet Visit Cost ($)")
plt.title("Vet Visit Cost vs. Cost of Living Index")
plt.tight_layout()
plt.savefig("Results/Vet_Cost_vs_Cost_of_Living.png")
plt.close()

# Plot 4: Bubble Chart

bins = [0, 0.0999, 0.1172, float('inf')]
labels = ['Low', 'Medium', 'High']

df['burden_category'] = pd.cut(
    df["VCBI"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

plt.figure(figsize=(10,7))
colors = {"Low": 'green', "Medium": 'orange', "High": 'red'}
size_scaled = (df["Cost of Living Index"] - df["Cost of Living Index"].min()) * 500

top_high = df.sort_values("VCBI", ascending=False).head(3)
top_low = df.sort_values("VCBI").head(3)
highlight_df = pd.concat([top_high, top_low])
non_highlight_df = df.drop(highlight_df.index)

plt.scatter(
    non_highlight_df["Median Household Income"],
    non_highlight_df["Average Vet Visit Cost"],
    s=(non_highlight_df["Cost of Living Index"] - df["Cost of Living Index"].min()) * 500,
    c=non_highlight_df["burden_category"].map(colors),
    alpha=0.7,
    edgecolors="w",
    linewidths=0.5
)

plt.scatter(
    highlight_df["Median Household Income"],
    highlight_df["Average Vet Visit Cost"],
    s=(highlight_df["Cost of Living Index"] - df["Cost of Living Index"].min()) * 500,
    c=highlight_df["burden_category"].map(colors),
    alpha=0.9,
    edgecolors="black", 
    linewidths=1
)

top_high = df.sort_values("VCBI", ascending=False).head(3)
top_low = df.sort_values("VCBI").head(3)

for i in top_high.index:
    plt.text(
        df.loc[i, "Median Household Income"],
        df.loc[i, "Average Vet Visit Cost"],
        df.loc[i, "State"],
        fontsize=8,
        ha="center",
        va="center"
    )

for i in top_low.index:
    plt.text(
        df.loc[i, "Median Household Income"],
        df.loc[i, "Average Vet Visit Cost"],
        df.loc[i, "State"],
        fontsize=8,
        ha="center",
        va="center" 
    )

plt.xlabel("Median Household Income ($)")
plt.ylabel("Average Vet Visit Cost ($)")
plt.title("Veterinary Cost Burden by State\n(Bubble Size = COL Index, Color = Burden Level)")

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker="o", color="w", label="Low Burden", markerfacecolor="green", markersize=10),
    Line2D([0], [0], marker="o", color="w", label="Medium Burden", markerfacecolor="orange", markersize=10),
    Line2D([0], [0], marker="o", color="w", label="High Burden", markerfacecolor="red", markersize=10),
]
plt.legend(handles=legend_elements, title="Burden Level")
plt.tight_layout()
plt.savefig("Results/Vet_Cost_Bubble_Chart.png")
plt.close()