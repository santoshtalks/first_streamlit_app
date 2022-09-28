import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('\N{flexed biceps}Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{leafy green}Kale, Spincach & Rocket Smoothie')
streamlit.text('\N{chicken}Hard-Boiled Free Range Egg')
streamlit.text('\N{avocado} Avocado Toast')

streamlit.header('\N{banana} \N{red apple} Build your own fruit smoothie \N{pineapple} \N{pear}')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
