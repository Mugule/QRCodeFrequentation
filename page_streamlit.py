import streamlit as st
import qrcode

url = "https://equipements-sportsgouv.contribuer.io/fr/tables/P5m4Puz4NDnxvxgtODuq2gY2L_bkGbVbmKN4HphSjyE/contributions/new?prefill_equip_numero="

equip_numero = "E001I850190001"

img = qrcode.make(url + equip_numero)
img_pil = img.get_image() if hasattr(img, "get_image") else img

label = "oui"
st.text_input(label, value="Numéro d'équipement")
st.image(img_pil, caption="QR code", use_container_width=True)
