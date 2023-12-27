import plotly.express as px
import streamlit as st

from functions import setup


@st.cache_resource
def get_scatter(dim1="", dim2=""):
    """Get scatter plot of selected dimensions
    """
    data = setup.get_data()
    return px.scatter(data, x=dim1, y=dim2, hover_data=['state'])
