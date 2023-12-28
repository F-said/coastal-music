import streamlit as st

from functions.config import states, dims

from figures.config import margins_css
from figures.scatter import get_scatter

# not a fan of this
st.markdown(margins_css, unsafe_allow_html=True)

# create title
st.title(":blue[MUSIC CLUSTERING]")
# st.title("MUSIC CLUSTERING")
st.subheader("Enter your choice of waiting room music to explore\
             quantitative similarities.")

# Sidebar
with st.sidebar:
    st.subheader("Enter a Song")
    with st.form("my_form"):
        st.text_input(label="Enter a song that would be appropriate\
                    for a waiting room.")
        st.divider()
        state = st.selectbox(label="Select your state", options=states)

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.spinner(text="Uploading song", cache=False)

    st.subheader("Change Dimensions")
    # init scatter with default args
    x_ax = st.selectbox(label="Select x-axis", options=dims, index=0)
    y_ax = st.selectbox(label="Select y-axis", options=dims, index=1)
    st.markdown("An explanation of the dimensions here...")

    fig = get_scatter(dim1=x_ax, dim2=y_ax)

# Scatter Plot
st.plotly_chart(fig, use_container_width=True)
