import streamlit as st
import pandas as pd
from functions.config import db


@st.cache_data
def get_data():
    """Get recommendations that have been completed
    """
    query = "SELECT * FROM entry e JOIN song s ON e.song_id = s.song_id;"
    return pd.read_sql(query, 'sqlite:///' + db)
