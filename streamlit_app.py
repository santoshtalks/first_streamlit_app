import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('\N{flexed biceps}Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green}Kale, Spincach & Rocket Smoothie')
streamlit.text('\N{chicken}Hard-Boiled Free Range Egg')
streamlit.text('\N{avocado} Avocado Toast')

streamlit.header('\N{banana} \N{red apple} Build your own fruit smoothie \N{pineapple} \N{pear}')

# Display the table on the page.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
