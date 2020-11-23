text = [
    'El mundo es ancho y ajeno',
    'Este terreno es el doble de ancho',
    'El doble del triangulo',
    'El mundo da vueltas'] 
from sklearn.feature_extraction.text import TfidfVectorizer 
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import heapq

#============= ********************** ===============
vectorizer = TfidfVectorizer(max_df=1.0, min_df=1, stop_words=stopwords.words("spanish"),norm = None)#ngram_range=(0,2),lowercase=True
#   X = vectorizer.fit_transform(text)
dx = pd.read_csv('Data/DFdatalWiki_limpio100000.csv')
data_cv=vectorizer.fit_transform(dx["pagina"])

#============ GENERAR MATRIZ DE DISPERCIÓN INVERSA ==============
#df = pd.DataFrame()
#df['tag']=list(vectorizer.get_feature_names())
#df['val']=list(vectorizer.idf_)
#df.to_csv('Data/___matrizdispercionInv100000_0.csv',columns=["tag","val"])
#============ GENERAR MATRIZ DE DISPERCIÓN ==============

tag=list(vectorizer.get_feature_names())
vale=list(vectorizer.idf_)
arra=[]
for i in range(len(tag)):
    arra.append([tag[i],vale[i]])
np.save('Data/good/___matrizdispercionInv100000_0.npy', arra) 

sparse.save_npz("Data/good/___matrizdispercion100000_0.npz", data_cv)
#============= ********************** ===============

#data2 = np.load('array.npy') 
"""
#PARA PRUEBAS DE BUSQUEDA SOBRE MATRIZ ALMACENADA
#============ CARGAR MATRIZ DE DISPERCIÓN ==============
Y = sparse.load_npz("Data/___matrizdispercion100000_0.npz")
#print(Y)
#================== recorrer matriz inversa =================
import depurador
obj=depurador.Depurador()

test_set = [obj.depurar("tarma wey")] #Query
#print(test_set)
lis=test_set[0].split(" ")#falta depurar tildes mayusculas etc
#print(lis)

#dx = np.load('Data/good/___matrizdispercionInv100000_0.npy') 
dx = pd.read_csv('Data/___matrizdispercionInv100000_0.csv')
#cont=0
#print(dx["tag"].loc[4])
#print(len(dx))
vector=[0]*(len(dx))
#print(vector)

for i in lis:
    #print(dx['tag'][10])
    try:
        aux=dx[dx['tag'] == i]
        vector[int(aux.index.values[0])]=aux["val"]
    except:
        continue
    #vector[int(aux.index.values[0])]=aux["val"]
print(vector)



#print(dx["val"].tolist())
#print("Fin")
#test_set = ["mundo"] #Query
#testVectorizerArray = vectorizer.transform(test_set).toarray()
cosine=cosine_similarity(Y, [vector]).flatten()
print("==) ",cosine) # ==)  [0.32591355 0.         0.         0.78648108]
arr = heapq.nlargest(2, range(len(cosine)), cosine.take)
print(arr)
print("===============")
#dataOriginal = np.memmap('Data/DFdatalWiki_completo100000.dat', dtype='S1797600', mode='r')
#print (dataOriginal[1])
#dx = pd.read_csv('Data/good/___DFdatalWiki_original10000.csv')
#print(dx["pagina"].loc[arr[0]])
"""