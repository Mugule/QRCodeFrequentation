import streamlit as st
import qrcode

url = "https://equipements-sportsgouv.contribuer.io/fr/tables/P5m4Puz4NDnxvxgtODuq2gY2L_bkGbVbmKN4HphSjyE/contributions/new?prefill_equip_numero="

equip_numero = "E001I850190001"

st.text_input("Numéro d'équipement", value=equip_numero)

img = qrcode.make(url + equip_numero)
img_pil = img.get_image() if hasattr(img, "get_image") else img
st.image(img_pil, caption="QR code", use_container_width=True)
