import streamlit as st
st.set_page_config(page_title="NMG General Suppliers", page_icon="🛒", layout="centered")
language = st.sidebar.radio("Chagua lugha / Choose Language:", ("🇬🇧 English", "🇹🇿 Kiswahili"))
import os
image_path=os.path.join(os.path.dirname(__file__),
                         "NMG.IMAGE.png")
st.image(image_path,width=300)
if language == "🇬🇧 English":
    st.title("Welcome to NMG General Suppliers")
    st.write("We Offer all sales related to sale and distribution of Products(Electrical items) to individuals and companies,at whole sale and retail Prices.")
else:
    st.title("Karibu NMG General Suppliers")
    st.write("Tunatoa huduma zote zinazohusiana na Uuzaji na usambazaji wa bidhaa(Vifaa vya umeme) kwa kampuni na watu binafsi kwa bei ya jumla na Rejareja.")
st.markdown("---")
st.subheader("🧾 Customer Information / Taarifa za Mteja")
with st.form("customer_form"):
    if language == "🇬🇧 English":
        name = st.text_input("Full Name")
        place = st.text_input("Place / Location")
        phone = st.text_input("Phone Number")
        gender = st.text_input("Male/Female")
        submitted = st.form_submit_button("Submit")
    else:
        name = st.text_input("Jina Kamili")
        place = st.text_input("Mahali / Eneo")
        phone = st.text_input("Namba ya Simu")
        gender = st.text_input("ME/KE")
        submitted = st.form_submit_button("Tuma Taarifa")
if submitted:
    if not (name and place and phone and gender):
        st.warning("⚠️ Please fill in all fields." if language == "🇬🇧 English" 
                   else "⚠️ Tafadhali jaza sehemu zote.")

    elif not phone.isdigit():
        st.error("Phone number must contain only numbers!" if language == "🇬🇧 English"
                 else "Namba ya simu lazima iwe na tarakimu tu!")

    elif len(phone) != 10:
        st.error("Phone number must be exactly 10 digits!" if language == "🇬🇧 English"
                 else "Namba ya simu lazima iwe na tarakimu 10!")

    else:
        st.success("✅ Data saved successfully!" if language == "🇬🇧 English" 
                   else "✅ Taarifa zimehifadhiwa kikamilifu!")

    st.markdown("---")
st.subheader("🏢 Company Information / Taarifa za Kampuni")
if language == "🇬🇧 English":
    st.markdown("""
    **Company Name:** NMG GENERAL SUPPLIERS LTD 
    **Location:** UBUNGO_EAST AFRICA COMMERCIAL AND LOGISTIC CENTER (Former Region Bus" Terminal), Dar es Salaam  
    **Room Number:** A2-12 (GROUND FLOOR)  
    **Working Hours:** 8:00 AM – 7:00 PM (Monday - Sunday)""")
else:
    st.markdown("""
    **Jina la Ofisi:** NMG General Suppliers Ltd  
    **Eneo:** Ubungo Stend ya zamani ya mkoa,Soko Jipya East Africa (EACLC), Dar es Salaam  
    **Room Namba:** A2-12 (Ghorofani Chini)  
    **Muda wa Kazi:** 8:00 AM – 7:00 PM (Jumatatu - Jumapili)  """)
if language == "🇬🇧 English":
    st.subheader("🚚 Delivery Mode")
    st.info("We deliver safely to your location. The customer is responsible for transport cost unless stated otherwise.")
    st.subheader("💰 Payment Method")
    st.info("Payment before or upon receiving goods (Free choice).")
else:
    st.subheader("🚚 Mfumo wa Utoaji Bidhaa")
    st.info("Tunafanya delivery mahali ulipo. Mteja atachangia gharama za usafiri isipokuwa imeelezwa vinginevyo.")
    st.subheader("💰 Mfumo wa Malipo")
    st.info("Malipo ni kabla au baada ya kupokea mzigo (kutoa kabla inapendekezwa zaidi).")
    st.info("Utaratibu wetu wa usafirishaji ni kwamba mzigo unafikia kwa wakala wetu mikoani ndipo utakabidhiwa mzigo na malipo kama hukufanya kabla")
    import os
if language == "🇬🇧 English":
    st.subheader("📄 Sample Product Catalogs with Prices")
    st.write("Click below to download sample catalogs with product names and prices:")
    if os.path.exists("lighting_catalog.pdf"):
        with open("lighting_catalog.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Lighting Catalog,decoration,surface,etc",
                data=file,
                file_name="lighting_catalog.pdf",
                mime="application/pdf"
            )
    if os.path.exists("Bulbs_cables_wires.pdf"):
        with open("Bulbs_cables_wires.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Bulbs,Cables_wire Catalog",
                data=file,
                file_name="Bulbs_cables_wires.pdf",
                mime="application/pdf")
    if os.path.exists("Surface_Dowlighting.pdf"):
        with open("Surface_Dowlighting.pdf", "rb") as file:
            st.download_button(
                label="📄 Dowload lighting :gipsum,dowlights,spotlight",
                data=file,
                file_name="Surface_Dowlighting.pdf",
                mime="application/pdf") 
    if os.path.exists("Sockets_price.pdf"):
        with open("Sockets_price.pdf", "rb") as file:
            st.download_button(
                label="📄 Dowload Socket catalog",
                data=file,
                file_name="Sockets_price.pdf",
                mime="application/pdf")                
    if os.path.exists("switchs_price.pdf"):
        with open("switchs_price.pdf", "rb") as file:
            st.download_button(
                label="📄 Dowload Switch catalog",
                data=file,
                file_name="switchs_price.pdf",
                mime="application/pdf")    

else:
    st.subheader("📄 Sampuli za Bidhaa na Bei Zake (Catalogs PDF)")
    st.write("Bonyeza chini kupakua catalog yenye sampuli za bidhaa na bei:")
    if os.path.exists("lighting_catalog.pdf"):
        with open("lighting_catalog.pdf", "rb") as file:
            st.download_button(
                label="📄 Pakua Catalog ya Taa za Urembo,kutani,gipsamu,kuchimbia,nk",
                data=file,
                file_name="lighting_catalog.pdf",
                mime="application/pdf")
    if os.path.exists("Bulbs_cables_wires.pdf"):
        with open("Bulbs_cables_wires.pdf", "rb") as file:
            st.download_button(
                label="📄 Pakua Catalog ya Balbu & Nyaya",
                data=file,
                file_name="Bulbs_cables_wires.pdf",
                mime="application/pdf")
    if os.path.exists("Surface_Dowlighting.pdf"):
        with open("Surface_Dowlighting.pdf", "rb") as file:
            st.download_button(
                label="📄 Pakua Catalog  ya taa aina:gipsamu,kuchimbia,spotlight",
                data=file,
                file_name="Surface_Dowlighting.pdf",
                mime="application/pdf")
    if os.path.exists("Sockets_price.pdf"):
        with open("Sockets_price.pdf", "rb") as file:
            st.download_button(
                label="📄 pakua Socket catalog",
                data=file,
                file_name="Sockets_price.pdf",
                mime="application/pdf") 
    if os.path.exists("switchs_price.pdf"):
        with open("switchs_price.pdf", "rb") as file:
            st.download_button(
                label="📄 pakua Switch catalog",
                data=file,
                file_name="switchs_price.pdf",
                mime="application/pdf")                   

st.markdown("---")
if language == "🇬🇧 English":
    st.subheader("📞 Contact Us")
    st.write("""
    For orders or inquiries:  
    **WhatsApp:** [Chat here](https://wa.me/255743117143)  
    **Phone:** +255 743 117 143""")
else:
    st.subheader("📞 Wasiliana Nasi")
    st.write("""
    Kwa oda au taarifa zaidi:  
    **WhatsApp:** [Bonyeza hapa kuwasiliana](https://wa.me/255743117143)  
    **Simu:** +255 743 117 143  """)
st.markdown("---")
st.info("Not all Electrical items are listed in this page,these are just samples, we have more than these Products | Tuna aina nyingi za Bidhaa Za vifaa vya umeme na vingine havijawekwa kwenye ukurasa huu kama unahitaji wasiliana nasi"
)
st.caption("© 2026 NMG General Suppliers | All Rights Reserved")
import csv
import os
from datetime import datetime

file_name = "NMG_customers.csv"

def save_customer(name,place, phone,gender):

    file_exists = os.path.isfile(file_name)
    file_is_empty=False
    if file_exists:
        if os.stat(file_name).st_size == 0:
            file_is_empty = True
    else:
        file_is_empty=True        

    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists or file_is_empty:
            writer.writerow(["Name", "Gender", "Place", "Phone","Date"])
        current_date=datetime.now().strftime("%Y-%m-%d")
        writer.writerow(["Name", "Gender", "Place", "Phone","current_date"])
print("Customer data saved successfully!")







