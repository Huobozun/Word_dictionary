0.'filter_data.py'是提取PubMed文件的程序，需要有'pubmed'库，以及'xmlpubmed'文件夹数据  
1.'sam.py'是从PubMed文件中仅抽取title和abstract的文件  
2.'gethersam.py'是把四个文件夹中的sam文件整合到一个文件夹中的程序（这里是因为在filter_data.py的时候分了四次去跑，如果一次跑完则本过程没有必要）  
3.'findfre_dict.py'是在PubMed中用AC自动机查找UMLS的词，并且整理出一个字典文件  
4.'findfre_marker.py'是在PubMed中用AC自动机查找UMLS的词，并且对应UMLS整理出一一对应的词频文件，（'getherfre.py'文件就是将得到每个PUBMED文件对应的的词频文件数据都加起来，得到一个统一的所有PUBMED文件的频率文件）  