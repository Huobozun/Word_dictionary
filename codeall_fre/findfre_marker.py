

import json
import os
import ahocorasick


def get_filelist(dir):#依次遍历.json文件
 
    Filelist = []
 
    for home, dirs, files in os.walk(path):
 
        for filename in files:
 
            # 文件名列表，包含完整路径
            #Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            Filelist.append( filename)
    return Filelist

def file_word(file):
     #读入要查找词的文件
    data=''
    with open("/home/zjg/code3.31/sampm10years/"+file,'r',encoding='utf8')as fr:  
        for lines in fr:
            json_data=lines
            data+=str(json_data)
        fr.close()
    return data#data就是一个文件的所有内容的str形式

def frefile(filedata,label):
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
        ii=y[0]
        yy[ii]+=1  




    for i2 in range(0,len(yy)):#将相同的词的结果赋予相同的词典位置（AC查找只能匹配上list中的最后一个，解决这个问题）
        if(yy[i2]==0):
            strlabel= str(label[i2])          
            for item2 in A.iter(strlabel):
                if(len(strlabel)==len(item2[1][1])):
                    yy[i2]=yy[item2[1][0]]
                    break

    return yy



if __name__ == "__main__":
    #读入文章列表
    path ="/home/zjg/code3.31/sampm10years"
    Filelist = get_filelist(dir)
    #print(Filelist)
    """path ="/home/zjg/code3.31/result-word"
    Filelistword = get_filelist(dir)"""
    for ida in range(0,len(Filelist)):
        print(Filelist[ida])
    #for ida in range(0,1):
        #读入文件中的数据（文件夹中的所有文件的title和text）
        filedata=file_word(Filelist[ida])


        #for iff in range(0,2):
            #读入要查找频率的词条
        with open('/home/zjg/code3.31/findfre_test.tsv','r',encoding='utf-8')as fc:
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
        with open('/home/zjg/code3.31/fre/fretest/fre0-'+Filelist[ida].replace('.json','')+'.tsv','w',encoding='utf-8')as ff:
            ix=0
            while(ix<len(z)):
                word=[]
                iy=0
                while(iy<len(z) and ix+iy<len(z)):
                    zz=z[ix+iy]
                    for j in range(0,len(z[ix+iy])):
                        word.append(zz[j])  
                    iy+=1
                a=frefile(filedata,word)
                i=0
                i2=ix
                while(i<len(a)):
                    freres=[]
                    for jj in range(0,len(z[i2])):
                        freres.append(a[i+jj])
                    ff.write('%s\n' %(json.dumps(freres)))
                    i+=len(z[i2])
                    i2+=1
                ix+=iy
            ff.close()