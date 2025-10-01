import streamlit as st
import qrcode

url = "https://equipements-sportsgouv.contribuer.io/fr/tables/P5m4Puz4NDnxvxgtODuq2gY2L_bkGbVbmKN4HphSjyE/contributions/new?prefill_equip_numero="

equip_numero = "E001I850190001"

img = qrcode.make(url + equip_numero)

display(img)
