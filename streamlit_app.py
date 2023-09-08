import streamlit as stl
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


stl.title("My Parent's New Healthy Diner")

stl.header('Breakfast Menu')
stl.text('🥣 Omega 3 and Blueberry Oatmeal')
stl.text('🥗 Kale, Spinach & Rocket Smoothie')
stl.text('🐔 Hard Boiled Free-Range Egg')
stl.text('🥑🍞 Avacado Toast')
   
stl.header('🥝🍇 Build Your Own Fruit Smoothie 🍌🥭')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') #Choose the Fruit name column as index.

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = stl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
stl.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
	fruityvice_normalized = pd.json_normalize(fruityvice_response.json()) #normalize the json version of response
	return fruityvice_normalized


	 #Output of normalization

# New Section to display fruityvice api response
stl.header('Fruityvice Fruit Advice!')
try:
	fruit_choice = stl.text_input('What fruit would you like information about?')
	if not fruit_choice:
		stl.error("Please select a fruit to get information")
	else:
		function_output =  get_fruityvice_data(fruit_choice)
		stl.dataframe(function_output)


except URLError as e:
	stl.error()
#don't run anything past here while we troubleshoot


#stl.stop()



# my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# stl.text("Hello from Snowflake:")
# stl.text(my_data_row)
stl.header("View Our Fruit List - Add Your Favorites!")
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("select * from fruit_load_list")
		return my_cur.fetchall()

#Add a button to load the fruit:
if stl.button('Get Fruit List'):
	my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	my_cnx.close()
	stl.dataframe(my_data_rows) #To display in table format

#Allow the user to add a new fruit to the existing list
def insert_row_in_snowflake(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
		return "Thanks for adding " + new_fruit

add_my_fruit = stl.text_input("What fruit would you like to add?")
if stl.button('Add a fruit to the list'):
	my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
	function_out2 = insert_row_in_snowflake(add_my_fruit)
	stl.text(function_out2)
#stl.write("Thanks for adding",add_my_fruit)



