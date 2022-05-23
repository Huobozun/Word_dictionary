#import urllib2
import re
import string
import operator
import os
import json

path=os.getcwd()


def cleanText(input):
    input = re.sub('\n+', " ", input).lower() # 匹配换行用空格替换成空格
    input = re.sub('\[[0-9]*\]', "", input) # 剔除类似[1]这样的引用标记
    input = re.sub(' +', " ", input) #  把连续多个空格替换成一个空格
    input = bytes(input.encode('utf-8'))#.encode('utf-8') # 把内容转换成utf-8格式以消除转义字符
    
    print(type(input))#input = input.decode("ascii", "ignore")
    return input

def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.decode().split(' ') #以空格为分隔符，返回列表


    for item in input:
        item = item.strip(string.punctuation) # string.punctuation获取所有标点符号

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'): #找出单词，包括i,a等单个单词(其他的单个字母的查找没有意义)
            cleanInput.append(item)
    return cleanInput

def getNgrams(output,input, n):
    input = cleanInput(input)

    
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])#.encode('utf-8')
        if ngramTemp not in output: #词频统计
            output[ngramTemp] = 0 #典型的字典操作
        output[ngramTemp] += 1
    return output


if __name__=='__main__':
    path1=path+'/sampm10years/'
    Filelist=os.listdir(path)
    #Filelist里面为新加的文章

    file1 = open(path+'word_library.txt', 'r') #原字典位置
    js1 = file1.read()
    dic1 = json.loads(js1)   
    #print(dic[0]) 
    file1.close() 

    output = dic1 # 以之前的字典为基础字典
    for i0 in range(0,len(Filelist)):
        print(i0,Filelist[i0])
        content = open(path+'/sampm10years/'+Filelist[i0]).read()
        ngrams = getNgrams(output,content, 1)
        sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True) #=True 降序排列
        output=ngrams

    fr = open('word_library.txt','w')
    for i in range(0,len(sortedNGrams)):
        fr.write('%s\t%s\n' %(sortedNGrams[i][0],sortedNGrams[i][1]))
    fr.close()
    #print(sortedNGrams)
