import streamlit as st
import pandas as pd

st.write("""
my first app
hello *world!*
""")

dados = [1,2,3,4,5,7,8,9,10,14,15,16,18,22,25,44,33,54]
df = pd.DataFrame(dados)
st.line_chart(df)
