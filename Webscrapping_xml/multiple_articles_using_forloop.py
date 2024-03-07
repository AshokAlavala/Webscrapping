import os
import pandas as pd
import numpy as np
import bs4 as bs
import urllib.request
import re
import spacy
import re, string, unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lem=WordNetLemmatizer()

os.chdir(r"D:\Full Stack Data Science AI & ML\ClassNotes\Feb 5_Web scrapping on xml\xml_many articles")

from glob import glob
path=r"D:\Full Stack Data Science AI & ML\ClassNotes\Feb 5_Web scrapping on xml\xml_many articles"
all_files=glob(os.path.join(path,"*.xml"))

import xml.etree.ElementTree as ET

dfs=[]
for filename in all_files:
    tree=ET.parse(filename)
    root=tree.getroot()
    root=ET.tostring(root, encoding="utf8").decode('utf8')
    dfs.append(root)
    
dfs[0]

###########

import bs4 as bs
import urllib.request
import re

parsed_article=bs.BeautifulSoup(dfs[0],'xml')
paragraphs=parsed_article.find_all('p')

article_text_full=""
for p in paragraphs:
    article_text_full+=p.text
    print(p.text)
    
def data_preprocessing(each_file):
    parsed_article=bs.BeautifulSoup(each_file,'xml')
    paragraphs=parsed_article.find_all('para')
    
    article_text_full=''
    for p in paragraphs:
        article_text_full+=p.text
        print(p.text)
        
    return article_text_full

data=[data_preprocessing(each_file) for each_file in dfs]