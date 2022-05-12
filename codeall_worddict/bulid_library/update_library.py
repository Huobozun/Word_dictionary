

import ahocorasick


import  os
basepath=os.getcwd() #获取当前工作目录路径




class buildlibrary():


    def __init__(self) -> None:
        self.datanum,self.dataword=buildlibrary.readlibrary()
        
        

    def frefile(self,label):#将每个词进行字典匹配，返回每个词对应的字典词的位置，如没找到对应词返回-1
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
            yy.append(-1)

        #print(self.dataword)
        #print(label)
        #每个文件读取查找
        #print(111)
        for item in A.iter(self.dataword):
            

            if(item[0]+1>len(self.dataword)-1 or item[0]+2>len(self.dataword)-1 or item[0]+3>len(self.dataword)-1):#如果查找词在边缘直接查找无效
                continue
            if(item[0]-len(item[1][1])<0 or item[0]-len(item[1][1])-1<0 or item[0]-len(item[1][1])-2<0):#如果查找词在边缘直接查找无效
                continue
   
            t1=self.dataword[item[0]-len(item[1][1])-2]+self.dataword[item[0]-len(item[1][1])-1]+self.dataword[item[0]-len(item[1][1])]
            t2=self.dataword[item[0]+1]+self.dataword[item[0]+2]+self.dataword[item[0]+3]
            
            if(t1!='###' or t2!='###'):#匹配成子集的情况舍掉，只保留完整匹配字典的情况
                continue

            ii=0
            x=''
            while(ii!=-1):
                if(self.dataword[item[0]-len(item[1][1])-3-ii]=="'" or self.dataword[item[0]-len(item[1][1])-3-ii]=='"'):
                    ii=-1
                    break
                x=self.dataword[item[0]-len(item[1][1])-3-ii]+x#根据前面的行标记来判断匹配到字典的第几行
                ii+=1

            yy[item[1][0]]=int(x)


        
        #print(222)
        for i2 in range(0,len(yy)):#将相同的词的结果赋予相同的词典位置（AC查找只能匹配上list中的最后一个，解决这个问题）
            if(yy[i2]==-1):
                strlabel= str(label[i2])          
                for item2 in A.iter(strlabel):
                    if(len(strlabel)==len(item2[1][1])):
                        yy[i2]=yy[item2[1][0]]
        #print(333)
           
            
        return yy

    def readlibrary():#读入文件已有的字典内容
        dataword=[]
        datanum=[]
        with open(basepath+'/word_library.tsv','r',encoding='utf-8')as fr:
            for lines in fr:
                if(len(lines)==1):
                    break

                else:
                    lines=str(lines)
                    word1=''
                    num1=''
                    ti=0
                    i1=0
                    while(i1<len(lines)):
                        if(ti==0):
                            if(lines[i1]+lines[i1+1]+lines[i1+2]=='###'):
                                word1+='###'
                                i1+=3
                                ti=1
                            else:
                                word1+=lines[i1]
                                i1+=1
                        else:
                            #print(word1,i1+3,len(lines))
                            if(lines[i1]+lines[i1+1]+lines[i1+2]=='###' and lines[i1+3].isdigit()==True):
                                word1+='###'
                                i1+=3
                                ti=0
                                break
                            else:
                                word1+=lines[i1]
                                i1+=1
                        

                    for i2 in range(i1,len(lines)):
                        num1+=lines[i2]

                    dataword.append(word1)
                    datanum.append(int(num1.replace('\n','')))   
        fr.close()

        return datanum,str(dataword)


    def addlibrary(self,newword,wordlist,alabel):#给字典添加新词
        if(alabel==0):#方式一，在字典添加新词，同时统计后面有无相同的新词
            self.dataword=eval(self.dataword)
            self.dataword.append(str(len(self.datanum)+1)+'###'+newword+'###')
            self.dataword=str(self.dataword)

            newwordlist=[]
            newwordlist.append(newword)
            B = ahocorasick.Automaton()
            for index,word in enumerate(newwordlist):
                B.add_word(word, (index, word))
        
            B.make_automaton()

            #设置计数器
            yy=0
            yindex=[]
            for item3 in B.iter(str(wordlist)):
                if(str(wordlist)[item3[0]+1]=="'" and str(wordlist)[item3[0]-len(newword)]=="'"):
                    yy+=1
                    yindex.append(item3[0])
                if(str(wordlist)[item3[0]+1]=='"' and str(wordlist)[item3[0]-len(newword)]=='"'):
                    yy+=1
                    yindex.append(item3[0])
                

            self.datanum.append(yy)

            
            i1=0
            countindex=0

            #print(wordlist)
            for i0 in range(0,len(str(wordlist))):

                if(str(wordlist)[i0]==' '):#空格会分隔开两个词比如['', '']
                    countindex+=1
            
                if(i1==len(yindex)):
                    break
                if( yindex[i1]==i0):#匹配到完整的词，赋值为词表的第几个
                    
                    yindex[i1]=countindex
                    i1+=1
                
                    


            #print(len(wordlist),yindex)
            return yindex
        
        else:#方式二只在字典添加一个新词
            self.datanum.append(1)
            self.dataword=eval(self.dataword)
            self.dataword.append(str(len(self.datanum))+'###'+newword+'###')
            self.dataword=str(self.dataword)

            




    def updatelibrary(self,word):#根据读入的word更新字典
        #print(self.dataword)
        
        label=1#判断list中有没有library里面没有的新词，如果有方法一：搜索此表里面有多少该新词并添加；方法二：就在library里面添加一个新词后重新对后面的词进行检测
        while(label!=0):
            label=0
            
            x=buildlibrary.frefile(self,word)#将新来词条与词典列表进行比较

            #判断新词多不多，新词多的话用方式二比较快，新词少用方式一比较快
            ixcount=0
            for ix in range(0,len(x)):
                if(x[ix]==-1):
                    ixcount+=1
            if(ixcount>0.2*len(x)):
                label=1
            else:
                label=0
        
            if(label==0):#方式一：查找一次，另外查找后面一样的新词，进行统计
                for i0 in range(0,len(x)):
                    if('\\/' in word[i0]):
                        continue
                    if(word[i0]=='\/'  or word[i0]=='\\/' or word[i0]=='\\\/' or word[i0]=='\\\\/'or word[i0]=="['" or word[i0]==".']" or word[i0]==".'," ):
                        continue
                    if(x[i0]==-1):#说明在词典里面没有匹配到这个，这个是个新词
                        y=buildlibrary.addlibrary(self,word[i0],word,0)
                        for iy in range(0,len(y)):
                            x[y[iy]]=-2
                        continue
                    else:
                        if(x[i0]==-2):#已经被添加的新词已经统计完了，不需再加
                            continue
                        else:
                            self.datanum[x[i0]-1]+=1
            else:#方式二，每次遇到新词就将后面所有的词查找一次
                for i0 in range(0,len(x)):
                    if('\\/' in word[i0]):
                        continue
                    if(word[i0]=='\/'  or word[i0]=='\\/' or word[i0]=='\\\/' or word[i0]=='\\\\/'or word[i0]=="['" or word[i0]==".']" or word[i0]==".'," ):
                        continue
                    if(x[i0]==-1):#说明在词典里面没有匹配到这个，这个是个新词
                        buildlibrary.addlibrary(self,word[i0],word,1)
                        break
                    else:
                        self.datanum[x[i0]-1]+=1   
                if(label==1):#有新词把新词后面的词重新查找
                    word1=[]
                    for i1 in range(i0+1,len(word)):
                        word1.append(word[i1])
                    word=word1
                if(label==1 and i0==len(x)-1):#新词是最后一个词就不再查找
                    label=0
        print(0)


    def writeinlibrary(self):#将现有字典写入文件
        with open(basepath+'/word_library.tsv','w',encoding='utf-8')as fw:
            self.dataword=eval(self.dataword)
            for i in range(0,len(self.dataword)):
                fw.write('%s%s\n' %(self.dataword[i],self.datanum[i]))
            
        fw.close()
        self.dataword=str(self.dataword)



"""word=['word1','word8','word8','word8','word8','word9','word8','word9']

x=buildlibrary()
x.updatelibrary(word)
x.writeinlibrary()"""



