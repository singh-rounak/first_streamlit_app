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
stl.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
stl.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
