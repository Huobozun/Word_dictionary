import json
import re 


#转化为用json.dumps写入文件
worddict=dict()


fr=open('word_library.txt','r')
for lines in fr:
    lines = re.sub('\n+', "", lines)#剔除文件中换行符
    lines0=lines.split('\t')
    worddict[lines0[0]]=lines0[1]

fr.close()


js = json.dumps(worddict)   
file = open('word_library_1words.txt', 'w')  
file.write(js)  
file.close()  