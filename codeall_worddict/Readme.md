0.这是一个建立指定文件夹内的文章集合的词频字典的过程，‘1-gram’‘2-gram’‘3-gram’分别代表连续的一个词，两个词，三个词的所有组合情况的词频统计。（其中三个词文件太大，跑不下来）  
1.需要提前将待跑的文章集合放到目录下的'sampm10years'文件夹中，然后运行'n-garm.py'就可以了  
2.'n-garm.py'不区分大小写的词频字典统计，'n-gram_bold.py'区分大小写的词频字典统计  
3.当'sample10years'文件夹中收录的是新的文章，并且已有一个词频统计库'word_library.txt',也可以运行'n-gram_update.py'对词库进行更新。  
4.'streamlit_show3.py'是用streamlit编写的一个可以展示查频信息的demo  