import streamlit
import pandas
streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('🥗 Omega 3 and blueberry oat meal')
streamlit.text('🍹 Spinach and smoothie')
streamlit.text('🍍 Fruits')
streamlit.text('🥛 Milk')
streamlit.header('Create your own smoothie 🍸')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Apple', 'Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
