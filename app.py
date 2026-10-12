import os
import streamlit as st

st.set_page_config(page_title="Erasmus Günleri", page_icon="🌍", layout="centered")

st.title("🌍 Erasmus Günleri")
st.write("Hangi ülkeyi gezmek istersin?")

UZANTILAR = (".jpg", ".jpeg", ".png", ".webp")

# images klasöründeki görsel dosyaları bulur, dosya adı (uzantısız) ülke adı olur
dosyalar = sorted(f for f in os.listdir("images") if f.lower().endswith(UZANTILAR))
ulkeler = {os.path.splitext(f)[0]: f for f in dosyalar}

secim = st.selectbox("Ülke seç", ["Seçiniz..."] + list(ulkeler.keys()))

if secim != "Seçiniz...":
    st.subheader(f"✈️ {secim}")
    st.image(os.path.join("images", ulkeler[secim]), use_container_width=True)