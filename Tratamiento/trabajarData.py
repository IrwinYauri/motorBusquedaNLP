import numpy as np
from zimscan import Reader
import re, string

import re, string, unicodedata
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import word_tokenize,sent_tokenize
#import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

from nltk.util import ngrams 
from collections import Counter 

import re, string
from bs4 import BeautifulSoup 
#===============================================
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import numpy.linalg as LA
from sklearn.metrics.pairwise import cosine_similarity

#N = 10000
#filename = '../Data/_datacompleta_O_1000.dat'
#metric_space = np.memmap(filename, dtype='S1797600', mode='w+', shape=(N,1))#fila * columna

import depurador

obj=depurador.Depurador()
    #quitarlinks(self,textPagina)
dict = {'pagina': []}  
df = pd.DataFrame(dict) 

#N = 100000
#filename = '___DatosIndices_O_100000.dat'
#metric_space = np.memmap(filename, dtype='S1797600', mode='w+', shape=(N,1))#fila * columna
#metric_space = np.memmap('___DatosIndices_O_100000.dat', dtype='S1797600', mode='r+', shape=(N,1))

with Reader(open('Data/wikipedia_es_all_nopic_2020-09.zim','rb')) as reader:#1735072
    i=0
    docs=[]
    for record in reader:        
        data = str(record.read().decode('utf-8'))
        #data = str(record.read())
        result = data.find('</html>')
        #result = data.find(texto)        
        if result != -1:      
            df.loc[len(df)]=[obj.depurar(data)] #limpio              
            #df.loc[len(df)]=[data.strip()]  #original
            
            #if i>11000:
                #metric_space[i]=data.encode('utf-8').strip() #original

            #metric_space[i]=obj.quitarlinks(data).encode('utf-8').strip()
              
            i+=1            
        
        if i>100000:#1735072            
            #print(data)
            break
    
    df.to_csv('DFdatalWiki_limpio100000.csv') #limpio
    #df.to_csv('DFdatalWikiOriginal250000.csv') #original
        
    print("Terminé")

#prueba
#metric_space = np.memmap('___DatosIndices_O_100000.dat', dtype='S1797600', mode='r', shape=(N,1))
#print(metric_space[8000])