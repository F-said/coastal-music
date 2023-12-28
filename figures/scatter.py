import plotly.express as px
import streamlit as st

from functions import db


@st.cache_resource
def get_scatter(dim1="", dim2=""):
    """Get scatter plot of selected dimensions
    """
    data = db.get_data()

    if __debug__:
        print(data)

    fig = px.scatter(
        data,
        x=dim1,
        y=dim2,
        hover_data=['state', 'title'],
        color='state'
    )
    fig.update_traces(marker={'size': 15})

    return fig
