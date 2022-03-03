import streamlit as st
import wget
import requests  
from io import BytesIO
from PIL import Image
      


st.title("My Streamlit App!")

with st.form("app_form"):
  status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))
  url = 'https://http.cat/' + status_code

  response = requests.get(url)

  submitted = st.form_submit_button("Submit")
  if submitted:
 
    #Saving Image
    img = Image.open(BytesIO(response.content))    
    img = img.save("response.jpg")
    
    #Reading Image
    image = Image.open('response.jpg')
    #Showing Image
    st.image(image, caption=status_code)
   
    st.write("You pressed submit!")
