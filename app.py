import sys
import pandas as pd
import numpy as np
import streamlit as st
from tempfile import NamedTemporaryFile
import urllib

st.set_page_config(page_title='Lapangbola - Player Roles', layout='wide')
st.header('Lapangbola - Player Roles')
st.markdown('Created by: Prana - R&D Division Lapangbola.com')

@st.cache_data(ttl=600)
def load_data(sheets_url):
    xlsx_url = sheets_url.replace("/edit#gid=", "/export?format=xlsx&gid=")
    return pd.read_excel(xlsx_url)

df = load_data(st.secrets["roles"])
rlz = load_data(st.secrets["rlz"])

col1, col2, col3 = st.columns(3)
with col1:
    s_filter = st.selectbox('Select Position', ['Center Back', 'Fullback', 'Midfielder',
                                                'Attacking 10', 'Winger', 'Forward'])
    role_search = st.checkbox('Search Player by Roles')
with col2:
    p_filter = st.selectbox('Select Player', ['Ilija Spasojevic', 'David da Silva'])
with col3:
    r = rlz[rlz['Position']==s_filter].reset_index(drop=True)
    r_filter = st.selectbox('Select Role', pd.unique(r['Roles']))

if role_search:
    fls = df[['Name', 'Minutes Played', r_filter]]
    fls[r_filter] = round(fls[r_filter], 2)
    fls = fls[fls[r_filter].notna()].sort_values(by=r_filter, ascending=False).reset_index(drop=True)
    st.write(fls)
else:
    st.write('Player Search test')
