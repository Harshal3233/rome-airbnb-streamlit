import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Rome Airbnb Dashboard", layout="wide")

df = pd.read_csv("rome_airbnb.csv")

st.title("Rome Airbnb Analysis and Price Prediction")
st.subheader("Author: Harshal Patel")

st.sidebar.header("Filters")

price_range = st.sidebar.slider(
    "Price Range (€)",
    int(df.price.min()),
    int(df.price.max()),
    (50, 200)
)

room_type = st.sidebar.multiselect(
    "Room Type",
    df.room_type.unique(),
    df.room_type.unique()
)

df = df[df.price.between(*price_range) & df.room_type.isin(room_type)]

st.header("Price Distribution")
fig1 = px.histogram(df, x="price", nbins=12)
st.plotly_chart(fig1, use_container_width=True)

st.header("Price by Room Type")
fig2 = px.box(df, x="room_type", y="price")
st.plotly_chart(fig2, use_container_width=True)

st.header("Average Price by Neighbourhood")
neigh_avg = df.groupby("neighbourhood")["price"].mean().reset_index()
fig3 = px.bar(neigh_avg, x="neighbourhood", y="price", text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

st.header("Rome Airbnb Map")
fig_map = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    color="price",
    size="accommodates",
    hover_name="neighbourhood",
    projection="natural earth"
)
st.plotly_chart(fig_map, use_container_width=True)