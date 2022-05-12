import json
import re

"""file = open('word_library_2word.txt', 'r') 
js = file.read()
dic = json.loads(js)   
print(dic[0]) 
file.close() 
"""
"""fr = open("word_library_2word.txt",'r+')
dic = eval(fr.read())   #读取的str转换为字典
print(dic[0])
fr.close()

worddict=dic"""

#转化为用json.dumps写入文件
worddict=dict()
fr=open('word_library_2word.txt','r')
for lines in fr:
    lines = re.sub('\n+', "", lines)#剔除文件中换行符
    #print(1)
    lines0=lines.split('\t')
    #print(2)
    worddict[lines0[0]]=lines0[1]

fr.close()


js = json.dumps(worddict)   
file = open('word_library_2words.txt', 'w')  
file.write(js)  
file.close()  