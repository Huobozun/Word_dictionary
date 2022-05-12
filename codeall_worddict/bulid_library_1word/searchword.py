

import re
import json 


file = open('word_library_1words.txt', 'r') 
js = file.read()
dic = json.loads(js)   
#print(dic[0]) 
file.close() 
worddict=dic

x=1
print('开始进行单个词的查找（输入"O"结束查找')
while(x!='O'):
    print('请输入你想要查找的词:')
    x=input()
    if(x=='O'):
        break
    if x not in worddict:
        print('NONE')
    else:
        print(worddict[x])
