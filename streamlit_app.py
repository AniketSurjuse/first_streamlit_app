import streamlit as st

st.title('My Parents New Healthy Dinner')

    
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Bluberry Oatmeal')
st.text('🥗 Kale, Spinach & Roacket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocadp Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.iloc[fruits_selected]
st.dataframe(fruits_to_show)
