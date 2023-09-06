import streamlit as stl
stl.title("My Parent's New Healthy Diner")

stl.header('Breakfast Menu')
stl.text('🥣 Omega 3 and Blueberry Oatmeal')
stl.text('🥗 Kale, Spinach & Rocket Smoothie')
stl.text('🐔 Hard Boiled Free-Range Egg')
stl.text('🥑🍞 Avacado Toast')
   
stl.header('🥝🍇 Build Your Own Fruit Smoothie 🍌🥭')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') #Choose the Fruit name column as index.

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = stl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
stl.dataframe(fruits_to_show)

# New Section to display fruityvice api response
stl.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
stl.text(fruityvice_response.json())
