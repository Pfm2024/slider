import streamlit as st
edad=st.slider("edad", min_value=10, max_value=40, step=2)
st.write(f"Tu edad es ...{edad}")
