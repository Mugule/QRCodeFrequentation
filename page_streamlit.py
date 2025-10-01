import streamlit as st
import qrcode
import requests

url = "https://equipements-sportsgouv.contribuer.io/fr/tables/P5m4Puz4NDnxvxgtODuq2gY2L_bkGbVbmKN4HphSjyE/contributions/new?prefill_equip_numero="

if st.query_params["numero"] :
    numero = st.query_params["numero"]
else :
    numero = "E001I850190001"

equip_numero = st.text_input("Numéro d'équipement", numero)

request = "https://equipements.sports.gouv.fr/api/explore/v2.1/catalog/datasets/data-es/records?select=inst_nom%2C%20equip_nom%2C%20equip_type_name&where=equip_numero%20%3D%20%27" + equip_numero +"%27&limit=1"

data = requests.get(request).json()

if len(data["results"]) > 0 :
    installation = data["results"][0]['inst_nom']
    equipement = data["results"][0]['equip_nom']
    type = data["results"][0]['equip_type_name']
    st.write(installation + ' - ' + equipement + " (" + type +")")
    
    img = qrcode.make(url + equip_numero)
    img_pil = img.get_image() if hasattr(img, "get_image") else img
    st.image(img_pil, caption="QR code", width=400)
else :
    st.write("Numéro équipement invalide")
