import streamlit as st
import requests

url = f"https://api.nasa.gov/planetary/apod?api_key=MmcAr6bvv73jwyADg6LnuAhYk7ZdtlGI4bkzCI9Z"

response = requests.get(url)
data = response.json()

response_img = requests.get(data['url'])
with open('images/apod.png', 'wb') as fo:
    fo.write(response_img.content)

st.title(data['title'])

st.image('images/apod.png')

st.write(data['explanation'])
