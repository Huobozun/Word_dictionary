

import streamlit as st
import re
import json 
import pandas as pd
import numpy as np

#import plotly_express as px
#df = st.cache(pd.read_csv)("sample_submission.csv")
 
st.title('Search in Pubmed')

#@st.cache
def readinfrequency(n):
    file1 = open('/home/zjg/code3.31/bulid_library_'+str(n)+'word/word_library_'+str(n)+'words.txt', 'r') 
    js1 = file1.read()
    dic1 = json.loads(js1)   
    #print(dic[0]) 
    file1.close() 
    worddict1=dic1

    
    return worddict1





url = st.text_input('The frequency of word you want to search in Pubmed:')
a=st.button('1 word')
b=st.button('2 words')

p=0
if(url!=''):
    if a:
        #st.write('哪里不会点哪里！')
        worddict=readinfrequency(1)
        p=1
    else:
        if b:
            #st.write('哪里不会点哪里！')
            worddict=readinfrequency(2)
            p=1
result=-2
#print(1,url,2,3)

if(url!='' and p==1):
    
    if url not in worddict:
        result=-1
            
    else:
        result=worddict[url]

if(result==-1):
    st.write('%s is not in Pubmed' %(url))
if(result!=-1 and result!=-2):
    st.write('The frequency of %s in Pubmed is %s' %(url,result))







#streamlit run /home/zjg/code3.31/bulid_library_1word/streamlit_show.py