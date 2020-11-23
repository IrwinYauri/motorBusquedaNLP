from sklearn.feature_extraction.text import TfidfVectorizer 
from nltk.corpus import stopwords
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
from sklearn.metrics.pairwise import cosine_similarity
#from scipy.sparse import csr_matrix
from scipy import sparse
import pandas as pd
#import pickle
from Tratamiento import Depurador
import heapq 
from bs4 import BeautifulSoup
from Tratamiento.zimscan import Reader

class Procesar:

    def __init__(self,
    dT='Data/DFdatalWiki_limpio100000.csv',
    dO='Data/DFdatalWiki_completo100000.dat',
    mD='Data/___matrizdispercion100000_0.npz',
    mDi='Data/___matrizdispercionInv100000_0.csv'):
        self.rutaDataTratada = dT
        self.rutaDataOriginal = dO       
        self.rutaMatrizDisp = mD
        self.rutaMatrizDispInv = mDi
        self.dataOriginal = np.memmap(dO, dtype='S1797600', mode='r')
    
    def buscar(self,cadena,canRes=3):
        Y = sparse.load_npz(self.rutaMatrizDisp)
        #print(Y)
        #================== recorrer matriz inversa =================
        obj=Depurador()
        test_set = obj.depurar(cadena) #Query                
        cosine=cosine_similarity(Y, [self.vectorizarQuery(test_set)]).flatten()        
        arr = heapq.nlargest(canRes, range(len(cosine)), cosine.take)
        coleccion=[]
        
        for i in range(canRes):
            soup = BeautifulSoup(self.dataOriginal[arr[i]], "html.parser")            
            coleccion.append({"indice":arr[i],"titulo":soup.find('title').get_text()})

        return coleccion
        
    def vectorizarQuery(self,test_set):
        lis=test_set.split(" ")
        #vector=[]
        dx = pd.read_csv(self.rutaMatrizDispInv)        
        vector=[0]*(len(dx))        
        for i in lis:
            try:
                aux=dx[dx['tag'] == i]
                vector[int(aux.index.values[0])]=aux["val"]
            except:
                continue
            
        return vector

    def getPagina(self,i):
        #metric_space = np.memmap(self.dataOriginal, dtype='S1797600', mode='r')
        return (self.dataOriginal[i].decode('utf-8'))#.decode('utf-8')        
        #return self.dataOriginal["pagina"].loc[i]
 
    """
    def buscarCero(self,cadena,canRes=3):
        vectorizer = TfidfVectorizer(max_df=1.0, min_df=1, stop_words=stopwords.words("spanish"),norm = None)#ngram_range=(0,2),lowercase=True        
        metric_space = np.memmap(self.dataTratada, dtype='S1797600')
        X = vectorizer.fit_transform(metric_space)#.toarray()                         
        test_set = [cadena] #Query
        testVectorizerArray = vectorizer.transform(test_set).toarray()
        cosine=cosine_similarity(X, testVectorizerArray).flatten()        
        arr = heapq.nlargest(canRes, range(len(cosine)), cosine.take)        
        coleccion=[]        
        metric_space = np.memmap(dO, dtype='S1797600')
        for i in range(canRes):
            soup = BeautifulSoup(self.metric_space[arr[i]], "html.parser")            
            coleccion.append({"indice":arr[i],"titulo":soup.find('title').get_text()})

        return coleccion        
    
    def wikidata(self,i):
        with Reader(open('Data/wikipedia_es_all_nopic_2020-09.zim','rb')) as reader:
            cont=0    
            for record in reader:        
                data = str(record.read().decode('utf-8'))
                result = data.find('</html>')
                #result = data.find(texto)        
                if result != -1:                
                    #docs.append(data)
                    cont+=1    
                if cont>2000000:
                    return data
    """
#Prueba
#obj=Procesar()
#print(obj.buscar("tarma"))
