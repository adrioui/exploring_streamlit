import streamlit as st
import pandas as pd

# Dataset from kaggle
df = pd.read_csv("National Universities Rankings.csv")

# Drop index column
df.drop(columns="index", inplace=True)
# Convert currency to float
df[df.columns[4:]] = df[df.columns[4:]].replace('[\$,]', '', regex=True).astype(float)

# Find a correlation between rank and undergrad enrollment
rank_grp = df.groupby("Rank", as_index=False)["Undergrad Enrollment"].sum()

# Find a correlation between state and undergrad enrollment
df["State"] = df["Location"].str.split(",", expand=True).drop(columns=0).squeeze()
loc_grp = df.groupby("State", as_index=False)["Undergrad Enrollment"].sum()

# Show the plots
st.bar_chart(rank_grp, x="Rank", y="Undergrad Enrollment")
st.bar_chart(loc_grp, x="State", y="Undergrad Enrollment")