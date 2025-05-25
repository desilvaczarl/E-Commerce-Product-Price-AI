import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('E-commerce Price Tracker')
url = st.text_input('Enter product URL')

if url:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.title.text.strip()
        st.write('Product Title:', title)
        # Simulate price for demo
        st.write('Current Price: $99.99')
    except:
        st.error('Failed to fetch product data')