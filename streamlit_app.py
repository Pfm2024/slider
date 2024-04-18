import streamlit as st
edad=st.slider("edad", min_value=10, max_value=40, step=2)
st.write(f"Tu edad es ...{edad}")

url40="https://www.youtube.com/watch?v=HKStqRFOEWg"
url20="https://www.youtube.com/shorts/vjtftw7dyxM"

if edad > 40:
  st.video(url40)
else:
  st.video(url20)
