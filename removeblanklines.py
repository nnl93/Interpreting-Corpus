import os
import codecs
import itertools

clean_lines = []
with open('/users/nannanliu/Downloads/Parallel Corpora/2013-ST.xml','r',encoding='utf-8') as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open ('/users/nannanliu/Downloads/Parallel Corpora/2013-ST.xml','w',encoding='utf-8') as f:
    f.writelines('\n'.join(clean_lines))

# remove the blank lines of all text files in a folder
import glob
import shutil

path='users/nannanliu/Downloads/Parallel Corpora'
clean_lines=[]

for infile in glob.glob (os.path.join(path,'*.txt')):
    output=infile+ 'out.txt'
    with open (infile,'r',encoding='utf-8') as oldfile:
        lines=oldfile.readlines()
        clean_lines=[l.strip() for l in lines if l.strip()]

    with open (output,'w',encoding='utf-8') as newfile:
        newfile.writelines('\n',join(clean_lines))
        
        


    
