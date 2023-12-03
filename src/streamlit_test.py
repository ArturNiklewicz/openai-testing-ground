import streamlit as st
import pandas as pd

def table(title):
    st.write(title)
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))