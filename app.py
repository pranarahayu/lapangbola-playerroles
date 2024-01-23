import sys
import pandas as pd
import numpy as np
import streamlit as st
from tempfile import NamedTemporaryFile
import urllib

st.set_page_config(page_title='Lapangbola - Player Roles', layout='wide')
st.header('Lapangbola - Player Roles')
st.markdown('Created by: Prana - R&D Division Lapangbola.com')

col1, col2, col3 = st.columns(3)
with col1:
    s_filter = st.selectbox('Select Position', ['Center Back', 'Forward'])
    role_search = st.checkbox('Search Player by Roles')
with col2:
    p_filter = st.selectbox('Select Player', ['Ilija Spasojevic', 'David da Silva'])
with col3:
    r_filter = st.selectbox('Select Role', ['Ball Playing Defender', 'Advanced Forward'])

if role_search:
    st.write('Role Search test')
else:
    st.write('Player Search test')

