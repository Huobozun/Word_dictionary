import os
import nltk
from nltk.tokenize import WordPunctTokenizer,WhitespaceTokenizer

from update_library import buildlibrary


def get_filelist(dir):#依次遍历.json文件
 
    Filelist = []
 
    for home, dirs, files in os.walk(path):
 
        for filename in files:
 
            # 文件名列表，包含完整路径
            #Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            Filelist.append( filename)
    return Filelist


if __name__=='__main__':
    path='/home/zjg/code3.31/sampm10years/'
    Filelist=get_filelist(dir)
    x=buildlibrary()
    for ii0 in range(0,len(Filelist)):
        print(Filelist[ii0])
        with open('/home/zjg/code3.31/sampm10years/'+Filelist[ii0],'r',encoding='utf-8')as fr:
            filedata=[]
            for lines in fr:
                filedata.append(str(lines))
        fr.close()

        ic=7580
        iw=0
        while(ic<len(filedata)):
            
            i0=0
            #print(filedata[ic])
            data=''
            while(i0<1 and i0<len(filedata)):
                
                data+=filedata[ic+i0]
                i0+=1
            token0 = WordPunctTokenizer().tokenize(data)
            x.updatelibrary(token0)

            iw+=1
            if(iw==20):
                print(Filelist[ii0],ic+i0)
                x.writeinlibrary()
                iw=0

            ic+=i0
            
            

            
        x.writeinlibrary()

    """txt = 'red foxes <emotion>scare</emotion> me.'
    token = WordPunctTokenizer().tokenize(txt)
    print(repr(token))
    x.updatelibrary(token)

    token1 = WhitespaceTokenizer().tokenize(txt)
    print(token1)


    x.writeinlibrary()"""
