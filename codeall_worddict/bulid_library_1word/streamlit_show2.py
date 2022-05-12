

import streamlit as st
import re
import json 
import pandas as pd
import numpy as np

#import plotly_express as px
#df = st.cache(pd.read_csv)("sample_submission.csv")
 
st.title('Search in Pubmed')

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def read_in_frequency_dictionary():
    st.write('1-word dictionary is loading ...')
    file1 = open('/home/zjg/code3.31/bulid_library_1word/word_library_1words.txt', 'r') 
    js1 = file1.read()
    dic1 = json.loads(js1)   
    #print(dic[0]) 
    file1.close() 
    worddict1=dic1
    st.write('2-words dictionary is loading ...')
    file2 = open('/home/zjg/code3.31/bulid_library_2word/word_library_2words.txt', 'r') 
    js2 = file2.read()
    dic2 = json.loads(js2)   
    #print(dic[0]) 
    file2.close() 
    worddict2=dic2
    st.write('dictionaries are ready!')
    
    return worddict1,worddict2





url = st.text_input('The frequency of word/words you want to search in Pubmed:')
a=st.button('1 word')
b=st.button('2 words')
print(222)

worddict1,worddict2=read_in_frequency_dictionary()

p=0
if(url!=''):
    if a:
        #st.write('哪里不会点哪里！')
        #worddict=readinfrequency(1)
        p=1
    else:
        if b:
            #st.write('哪里不会点哪里！')
            #worddict=readinfrequency(2)
            p=2
result=-2
#print(1,url,2,3)

if(url!='' and p==1):
    
    if url not in worddict1:
        result=-1
            
    else:
        result=worddict1[url]
if(url!='' and p==2):
    
    if url not in worddict2:
        result=-1
            
    else:
        result=worddict2[url]

if(result==-1):
    st.write('"%s" is not in Pubmed' %(url))
if(result!=-1 and result!=-2):
    st.write('The frequency of "%s" in Pubmed is %s' %(url,result))







#streamlit run /home/zjg/code3.31/bulid_library_1word/streamlit_show2.py