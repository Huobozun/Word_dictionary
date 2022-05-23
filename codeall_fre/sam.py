import json
import os
path=os.getcwd()

def get_file(file):
    with open(path+"/pm1000-/"+file,'r',encoding='utf-8')as fr:
        with open(path+"/sampm2.3/Sam1-"+file,'w',encoding='utf-8',newline='')as fw:
            #data=json.load(fr)
            for lines in fr:
                lines=eval(lines)
                x=[]
                x.append(lines.get('title'))
                a=lines.get('abstract')
                for i in range(0,len(a)):
                    if(a[i].get('text')!=None):
                        x.append(a[i].get('text'))
                fw.write('%s\n' %(x))
            fw.close()
            fr.close()
            

if __name__=='__main__':
    path1=path+"/pm/"
    Filelist=os.listdir(path1)
    for i in range(0,len(Filelist)):
        q=get_file(Filelist[i])
