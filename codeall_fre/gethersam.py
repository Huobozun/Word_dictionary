
import os


path=os.getcwd()



if __name__=='__main__':
    path1=path+"/sampm"
    Filelist=os.listdir(path1)
    for i0 in range(0,len(Filelist)):
        with open(path+'/sampm8years/'+Filelist[i0],'w',encoding='utf-8',newline='')as fw:
            for i1 in range(0,4):
                try:
                    with open(path+'/home/zjg/code3.31/sampm2.'+str(i1)+'/'+Filelist[i0],'r',encoding='utf-8')as fr:
                        for lines in fr:
                            fw.write('%s' %(lines))

                    fr.close()
                except FileNotFoundError:
                    continue
        fw.close()

