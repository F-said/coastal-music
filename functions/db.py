import streamlit as st
import pandas as pd
from functions.config import db


@st.cache_data
def get_data():
    """Get recommendations that have been completed
    """
    # get joined data from db
    query = "SELECT * FROM entry e JOIN song s ON e.song_id = s.song_id;"
    return pd.read_sql(query, 'sqlite:///' + db)


def insert_song(song_id, title, musician, album,
                acoustiness, danceability, energy, instrumentalness,
                liveliness, loudness, speechiness, valence, state):
    """Upload song features to db
    """
    # insert data into db
    query = "INSERT INTO"
    insert_entry(song_id, state)


def insert_entry(song_id, state):
    """Upload entry to db
    """
    # insert data into db
    query = "INSERT INTO"
