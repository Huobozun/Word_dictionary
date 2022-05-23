

import json
import os
import ahocorasick



def file_word(file):
     #读入要查找词的文件
    data=''
    with open("/home/zjg/code3.31/sampm10years/"+file,'r',encoding='utf8')as fr:  
        for lines in fr:
            json_data=lines
            data+=str(json_data)
        fr.close()
    return data#data就是一个文件的所有内容的str形式

class bulid_UMLSlibrary():
    def __init__(self) -> None:
        self.worddict=dict()
        pass

    def frefile(self,filedata,label):
        A = ahocorasick.Automaton()

        # 向trie树中添加单词
        for index,word in enumerate(label):
            A.add_word(word, (index, word))
        # 用法分析add_word(word,[value]) => bool
        # 根据Automaton构造函数的参数store设置，value这样考虑：
        # 1. 如果store设置为STORE_LENGTH，不能传递value，默认保存len(word)
        # 2. 如果store设置为STORE_INTS，value可选，但必须是int类型，默认是len(automaton)
        # 3. 如果store设置为STORE_ANY，value必须写，可以是任意类型
        # 将trie树转化为Aho-Corasick自动机
        A.make_automaton()



        #设置计数list
        yy=[]
        for i in range(0,len(label)):
            yy.append(0)

        #每个文件读取查找
        for item in A.iter(filedata):
            y=item[1]#比对查找结果
            if y[1] not in self.worddict:
                self.worddict[y[1]]=0
            self.worddict[y[1]]+=1
              



if __name__ == "__main__":
    #读入文章列表
    path ="/home/zjg/code3.31/sampm10years"
    Filelist = os.listdir(path)
    #print(Filelist)
    path ="/home/zjg/code3.31/result-word"
    Filelistword = os.listdir(path)
    xdictionary=bulid_UMLSlibrary()
    for ida in range(0,len(Filelist)):
        print(ida)
        #print(Filelist[ida])
    #for ida in range(0,1):
        #读入文件中的数据（文件夹中的所有文件的title和text）
        filedata=file_word(Filelist[ida])

        for iff in range(0,len(Filelistword)):
            #print(Filelistword[iff])
        #for iff in range(0,2):
            #读入要查找频率的词条
            with open('/home/zjg/code3.31/result-word/'+Filelistword[iff],'r',encoding='utf-8')as fc:
                dataci=[]
                for line in fc:
                    dataci.append(line)
                fc.close()
            z=[]
            for ii in range(0,len(dataci)):
                x=dataci[ii]
                y=''
                for i in range(9,len(x)):
                    y+=x[i]
                z.append(eval(y))
            #z是读取完之后为list[['','',''],[]]格式
        
        
            #按照每篇所有单词依次进行词条在所有文章的出现频率
            ix=0
            word=[]
            while(ix<len(z)):
                zz=z[ix]
                for j in range(0,len(zz)):
                    word.append(zz[j])  
                ix+=1
            xdictionary.frefile(filedata,word)

                  
    js = json.dumps(xdictionary.worddict)   
    file = open('/home/zjg/code3.31/fre/UMLS_fre_dictionary.txt', 'w',encoding='utf-8')  
    file.write(js)  
    file.close()  