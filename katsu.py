import streamlit as st
from selenium import webdriver
from streamlit import uploaded_file_manager
from streamlit.elements.selectbox import SelectboxMixin
from time import sleep

st.title("K.M=")
select = st.selectbox("Login",["ミライシードchrome","ミライシードEdge"])

if st.button("open"):
    if select == "ミライシードEdge":
    
     st.text("open Edge")
     browser = webdriver.Edge(executable_path= "msedgedriver.exe")
     browser.get("https://miraiseed.benesse.ne.jp/seed/vw020101/displayLogin/nX45j28W")
     sleep(2)

     elem_number3_btn =browser.find_element_by_name("number")
     elem_number3_btn.click()
  
    


     sleep(4)

     elem_ketei44_btn =browser.find_element_by_id("btn_positive_number")
     elem_ketei44_btn.click()

     elem_class_btn =browser.find_element_by_id("classSelect")
     elem_class_btn.click()

     elem_gr_btn = browser.find_element_by_xpath("//*[@id='gradeList']/li[2]")
     elem_gr_btn.click()

     elem_ku_btn = browser.find_element_by_xpath("//*[@id='classList']/li[2]")
     elem_ku_btn.click()
     sleep(1)
  


     elem_pass_btn =browser.find_element_by_name("pass")
     elem_pass_btn.click()
 
     elem_l_btn =browser.find_element_by_id("key_l")
     elem_l_btn.click()

     elem_n_btn =browser.find_element_by_id("key_n")
     elem_n_btn.click()

     elem_ll_btn =browser.find_element_by_id("key_l")
     elem_ll_btn.click()

     elem_g_btn =browser.find_element_by_id("key_g")
     elem_g_btn.click()

     elem_5_btn =browser.find_element_by_id("key_5")
     elem_5_btn.click()

     elem_e_btn =browser.find_element_by_id("key_e")
     elem_e_btn.click()

     sleep(1)
     elem_konn_btn =browser.find_element_by_id("btn_positive")
     elem_konn_btn.click()




     elem_okkk_btn =browser.find_element_by_name("inputLoginChild")
     elem_okkk_btn.click()
     
    
    else: 
       st.text("open chrome")
       browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://miraiseed.benesse.ne.jp/seed/vw020101/displayLogin/nX45j28W")
    sleep(4)

    elem_number3_btn =browser.find_element_by_name("number")
    elem_number3_btn.click()

                                                                


    sleep(5)

    elem_ketei44_btn =browser.find_element_by_id("btn_positive_number")
    elem_ketei44_btn.click()

    elem_class_btn =browser.find_element_by_id("classSelect")
    elem_class_btn.click()

    elem_gr_btn = browser.find_element_by_xpath("//*[@id='gradeList']/li[2]")
    elem_gr_btn.click()

    elem_ku_btn = browser.find_element_by_xpath("//*[@id='classList']/li[2]")
    elem_ku_btn.click()
    sleep(1)



    elem_pass_btn =browser.find_element_by_name("pass")
    elem_pass_btn.click()

    elem_l_btn =browser.find_element_by_id("key_l")
    elem_l_btn.click()

    elem_n_btn =browser.find_element_by_id("key_n")
    elem_n_btn.click()

    elem_ll_btn =browser.find_element_by_id("key_l")
    elem_ll_btn.click()

    elem_g_btn =browser.find_element_by_id("key_g")
    elem_g_btn.click()

    elem_5_btn =browser.find_element_by_id("key_5")
    elem_5_btn.click()

    elem_e_btn =browser.find_element_by_id("key_e")
    elem_e_btn.click()

    elem_konn_btn =browser.find_element_by_id("btn_positive")
    elem_konn_btn.click()




    elem_okkk_btn =browser.find_element_by_name("inputLoginChild")
    elem_okkk_btn.click()

st.title("画像表示") 
from PIL import Image
import numpy as np
uploaded_file = st.file_uploader("画像", type='jpg')
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  img_array = np.array(img)
  st.image(img_array, caption = 'Uploaded Image',use_column_width = True)

st.title("動画表示") 

a = st.file_uploader("動画", type='MP4')
if a is not None:
  img = Image.open(a)
  img_array = np.array(img)
  st.image(img_array, caption = 'Uploaded Image',use_column_width = True)

st.title("なんか書け") 
c = st.text_input("","")
st.write(c)  
if c == "宮野功至は神様":
    st.title("You are perfect person　よくわかってる")
    
elif c == "":
    st.title("")
    
else:
    st.title("kimi sindahouga iiyo ?")
   


