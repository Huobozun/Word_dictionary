import json
import re


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