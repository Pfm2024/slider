import streamlit as st

edad=10

url40="https://www.youtube.com/watch?v=HKStqRFOEWg"
url20="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if edad > 40:
  st.video(url40)
else:
  st.video(url20)

edad=st.slider("edad", min_value=10, max_value=70, step=2)
st.write(f"Tu edad es ...{edad}")

