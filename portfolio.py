import streamlit as st

tab1, tab2, tab3 = st.tabs(["Home", "Resume", "Projects"])

with tab1:
   st.header("Home")
   st.subheader("Welcome to my portfolio!")

with tab2:
   st.header("Resume")
   st.link_button("View resume", "https://docs.google.com/document/d/1MaIHCb7SVyWOiLhTeXQBPaVLeiAhWb5NWFMMtfYmi7s/edit?usp=sharing")

with tab3:
   st.header("Projects")
   st.image('phplogo.png', width=100)
   st.link_button("Real Estate Website", "http://areawebsites.org/kDavis/php/home/home.php")
   st.link_button("Crab Dashboard", "http://areawebsites.org/kDavis/php/crab/dashboard.php?id=ht")
   st.text("")
   st.image('officelogo.png', width=150)
   st.link_button("Word Dream Job", "http://areawebsites.org/kDavis/pdf/dream-job.pdf")
   st.link_button("Excel Customer Invoice", "http://areawebsites.org/kDavis/pdf/customer.pdf")