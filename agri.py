
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pandas as pd

st.title("Exploratory Data Analysis - Indian Agriculture")

# Dataset
df = pd.read_csv("crop_data_cleaned.csv")
st.write(df)

# --- Create plots ---
# Rice Area
top5_rice = df.groupby("state_name")["rice_production"].sum().reset_index().sort_values("rice_production", ascending=False).head(5)
fig1, row1 = plt.subplots()
sns.lineplot(x="state_name", y="rice_production", data=top5_rice, ax=row1, marker='o')
plt.xticks(rotation=50)
row1.set_title("Top 5 Rice Producing States")

# Wheat Production
top5_wheat = df.groupby("state_name")["wheat_production"].sum().reset_index().sort_values("wheat_production", ascending=False).head(5)
fig2, row2 = plt.subplots()
sns.barplot(x="state_name", y="wheat_production", data=top5_wheat, ax=row2, palette='Set2')
plt.xticks(rotation=45)
row2.set_title("Top 5 Wheat Production States")

# st.write("Any negative wheat_production values? ", (df["wheat_production"] < 0).any()) - (to check the true of false)
# st.write("Any NaN wheat_production values? ", df["wheat_production"].isna().any())

top5_wheat = df[df["wheat_production"] > 0].sort_values("wheat_production", ascending=False).head(5)

fig3, ax3 = plt.subplots()
ax3.pie(
    top5_wheat['wheat_production'],
    labels=top5_wheat['state_name'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('magma', 5),
    explode=[0.05]*5
)
ax3.set_title("Wheat Production Percentage of Top 5 States")


# Oilseeds Line Chart
top5_oil = df.groupby("state_name")["oilseeds_production"].sum().reset_index().sort_values("oilseeds_production", ascending=False).head(5)
fig4, row3 = plt.subplots()
sns.barplot(x="state_name", y="oilseeds_production", data=top5_oil, ax=row3, color="yellow")
plt.xticks(rotation=45)
row3.set_title("Oilseeds production by top 5 states")

# Sugarcane Line Chart
last50_sugarcane = df.sort_values("year", ascending=False).head(50)
fig5, row3 = plt.subplots()
sns.barplot(x="year", y="sugarcane_production", data=last50_sugarcane, ax=row3, color="green")
row3.set_title("India's SUGARCANE PRODUCTION (Last 50 years)")

# Rice vs Wheat Comparison
fig6, row4 = plt.subplots()
sns.scatterplot(x="rice_production", y="wheat_production", data=df, ax=row4, color="red")
row4.set_title("Rice vs Wheat Production")




# --- Display in columns ---
col1, col2, = st.columns(2)
with col1:
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
with col2:
    st.pyplot(fig4)
    st.pyplot(fig5)
    st.pyplot(fig6)

    