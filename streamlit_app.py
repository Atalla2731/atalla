import streamlit as st

st.title("selamat datang di situs ini")
st.write(
    "mari mengasah otak di situs ini"
)
st.image("image.jpg",width=2000)

st.title("situs halal")
st.header("Aplikasi Game mengasah otak")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
  st.write(f"{angka} adalah bilangan ganjil")
