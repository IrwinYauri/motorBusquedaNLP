import re, string, unicodedata
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.util import ngrams 

#from collections import Counter 
#from zimscan import Reader
#import re, string
#from nltk.corpus import stopwords
#import numpy as np
#import numpy.linalg as LA
#from sklearn.metrics.pairwise import cosine_similarity
#============================== ELIMINAR RUIDO ===============

class Depurador:
    #def __init__(self,c):
        #self.cadena=c

    def strip_html(self,text):
        text=text.replace('<', ' <')
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()
        #return soup.find('body').get_text()

    def remove_between_square_brackets(self,text):
        return re.sub('\[[^]]*\]', '', text)

    def denoise_text(self,text):
        text = self.strip_html(text)
        text = self.remove_between_square_brackets(text)
        #text = clean_text(text)
        return text

    #sample = denoise_text(sample)
    #print(sample)

    #============================== TOKENIZAR ===============
    #words = nltk.word_tokenize(sample,"spanish")
    #print(words)

    #============================== NORMALIZACIÓN ===============
    def remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def to_lowercase(self,words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words

    def remove_punctuation(self,words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words
    
    def numero_to_letras(self,numero):
        indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"),
                    ("MIL", "MIL"), ("BILLON", "BILLONES")]
        entero = int(numero)
        decimal = int(round((numero - entero)*100))
        # print 'decimal : ',decimal
        contador = 0
        numero_letras = ""
        while entero > 0:
            a = entero % 1000
            if contador == 0:
                en_letras = self.convierte_cifra(a, 1).strip()
            else:
                en_letras = self.convierte_cifra(a, 0).strip()
            if a == 0:
                numero_letras = en_letras+" "+numero_letras
            elif a == 1:
                if contador in (1, 3):
                    numero_letras = indicador[contador][0]+" "+numero_letras
                else:
                    numero_letras = en_letras+" " + \
                        indicador[contador][0]+" "+numero_letras
            else:
                numero_letras = en_letras+" " + \
                    indicador[contador][1]+" "+numero_letras
            numero_letras = numero_letras.strip()
            contador = contador + 1
            entero = int(entero / 1000)
        numero_letras = numero_letras+" con " + str(decimal) + "/100"
        #print('numero: ', numero)
        return numero_letras


    def convierte_cifra(self,numero, sw):
        lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS","TRESCIENTOS","CUATROCIENTOS","QUINIENTOS","SEISCIENTOS","SETECIENTOS","OCHOCIENTOS","NOVECIENTOS"]
        lista_decena = ["", ("DIEZ", "ONCE", "DOCE","TRECE","CATORCE","QUINCE","DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE"),
                                        ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y "),("CUARENTA" , "CUARENTA Y "),
                        ("CINCUENTA", "CINCUENTA Y "), ("SESENTA" , "SESENTA Y "),
                        ("SETENTA", "SETENTA Y "), ("OCHENTA" , "OCHENTA Y "),
                        ("NOVENTA", "NOVENTA Y ")
                        ]
        lista_unidad = ["", ("UN" , "UNO"), "DOS", "TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]
        centena = int(numero / 100)
        decena = int((numero - (centena * 100))/10)
        unidad = int(numero - (centena * 100 + decena * 10))
        # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

        texto_centena = ""
        texto_decena = ""
        texto_unidad = ""

        # Validad las centenas
        texto_centena = lista_centana[centena]
        if centena == 1:
            if (decena + unidad) != 0:
                texto_centena = texto_centena[1]
            else:
                texto_centena = texto_centena[0]

        # Valida las decenas
        texto_decena = lista_decena[decena]
        if decena == 1:
            texto_decena = texto_decena[unidad]
        elif decena > 1:
            if unidad != 0:
                texto_decena = texto_decena[1]
            else:
                texto_decena = texto_decena[0]
        # Validar las unidades
        # print "texto_unidad: ",texto_unidad
        if decena != 1:
            texto_unidad = lista_unidad[unidad]
            if unidad == 1:
                texto_unidad = texto_unidad[sw]

        return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)

    def replace_numbers(self,words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        #p = inflect.engine()
        
        new_words = []
        for word in words:
            if word.isdigit() and len(word) <= 15:
                #print("==> ",word,len(word))
                #new_word = p.number_to_words(word)
                new_word = self.numero_to_letras(int(word))                
                new_words.append(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
                
        return new_words

    def remove_stopwords(self,words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in stopwords.words('spanish'):
                new_words.append(word)
        return new_words

    def stem_words(self,words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self,words):
        """Lemmatize verbs in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas

    def normalize(self,words):
        words = self.remove_non_ascii(words)
        words = self.to_lowercase(words)
        words = self.remove_punctuation(words)
        words = self.replace_numbers(words)
        #words = remove_stopwords(words)#************************************
        return words

    #words = normalize(words)
    #print(words)

    #Falta corregir errores tipográficos

    #===================== LEMMING ========================

    def stem_and_lemmatize(self,words):
        stems = self.stem_words(words)
        lemmas = self.lemmatize_verbs(words)
        return stems, lemmas

    #stems, lemmas = stem_and_lemmatize(words)

    #Stemmed: Extrae la base de la palabra
    #comiendo, comera -> comer
    ##############################################################print('Stemmed:\n', stems)#ajustar la lematización comer
    #print("----------------------------------------")
    #Lemmatized: Dada una forma flexionada, hallar el lema correspondiente
    # reducir palabras a su lema
    ##############################################################print('\nLemmatized:\n', lemmas)

    #print("*********************************")
    """
    print(words)

    print("3333333333333333333333333333")
    ongrams = ngrams(words,1)
    bigrams = ngrams(words,2) 
    trigrams = ngrams(words,3) 
    fourgrams = ngrams(words,4) 
    fivegrams = ngrams(words,5) 

    print(Counter(ongrams))

    """

    #print('============================================')
    #=================== UNIR PALABRAS =====================
    def textJoin(self,words):
        text_words = ""
        for word in words:
            text_words+=word+" "
        return text_words

    def depurar(self,sample):
        sample = self.denoise_text(sample)
        words = nltk.word_tokenize(sample,"spanish")
        words = self.normalize(words)
        stems, lemmas = self.stem_and_lemmatize(words)
        return self.textJoin(stems)

    def quitarlinks(self,textPagina):
        soup = BeautifulSoup(textPagina, 'html.parser')
        for s in soup.select('script'):
            s.extract()
        for s in soup.select('link'):
            s.extract()
        return soup

#obj=Depurador()
#print(obj.depurar("bienvenidos a las tardes"))