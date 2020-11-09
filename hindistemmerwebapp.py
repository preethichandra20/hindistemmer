#!/usr/bin/env python
# coding: utf-8

# In[43]:


import streamlit as st
import codecs
import re
html_temp = """
<body> </body>

<h1 style="color:#6da6c7;text-align:center;margin-top:-30px;font-size:60px;">HINDI STEMMER</h1>
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.title("Enter the word")
user_input=st.text_area(" ")
sentences=user_input.split(u"।")
words_list = list()
for sentence in sentences:
    words = sentence.split(' ')
    words_list += words
suffixes_list= [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा",
    u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें",
    u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ओं",u"ाएं",
    u"ुओं",u"ुआं",u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",
    u"ताओं",u"ताएं",u"ियों",u"ियां",u"ियाँ",u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां",u"ीय",u"ीयाँ",u"एँ",u"ाएँ"]
result=" "
for word in words_list:
    n=0
    l=len(word)
    for suffix in suffixes_list:
        if(word.endswith(suffix)):
            k=len(suffix)
            if(k>n):
                n=k
    if(n!=0):
        word=word[:-n]
    result+=word
    result+=" "
if st.button("Generate Stems"):
    st.title("Stemmed Word")
    st.success(result)