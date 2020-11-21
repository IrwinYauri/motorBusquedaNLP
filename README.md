MOTOR DE BÚSQUEDA POR CONTENIDO PARA EL DATASET DE WIKIPEDIA
Aum. Irwin L. Yauri Orihuela

1.	Introducción

1.1.	DataSet Wikipedia: Todo el contenido de Wikipedia se encuentra disponible bajo un cierto esquema de licenciamiento que permite que sea copiado, modificado y redistribuido con pocas restricciones. Se encuentra en formato  ZIM (en inglés, Zeno IMprove, en español, Zeno MEjorado). El formato permite la compresión de artículos, cuenta con un índice de búsqueda de texto completo y categorías. El original xml Wikipedia en enero de 2012 contaba con unos 3,8 millones de artículos con imágenes, tenía un tamaño de 7,5 GiB mientras que el archivo ZIM equivalente era de 9.7 GiB (aproximadamente un 30% mayor). El formato de archivo abierto openZIM ofrece apoyo a un lector de ZIM de código abierto.

1.2.	Motor de búsqueda: Un motor de búsqueda es una herramienta que permite a los usuarios localizar información de manera rápida y sencilla. Cada motor de búsqueda utiliza diferentes fórmulas matemáticas complejas para generar resultados de búsqueda. Los algoritmos de los motores de búsqueda toman los elementos clave de una página web, incluido el título de la página, el contenido y la densidad de palabras clave. Los motores de búsqueda solo "ven" el texto en las páginas web y utilizan la estructura HTML subyacente para determinar la relevancia. Las fotos grandes o la animación Flash dinámica no significan nada para los motores de búsqueda, pero el texto real de las páginas sí. 

1.3.	Procesamiento del Lenguaje Natural (NLP): Es una disciplina con una larga trayectoria. Nace en la década de 1960, como un subárea de la Inteligencia Artificial y la Lingüística, con el objeto de estudiar los problemas derivados de la generación y comprensión automática del lenguaje natural.

En sus orígenes, sus métodos tuvieron gran aceptación y éxito, no obstante, cuando sus aplicaciones fueron llevadas a la práctica, en entornos no controlados y con vocabularios genéricos, empezaron a surgir multitud de dificultades. Entre ellas, pueden mencionarse por ejemplo los problemas de polisemia y sinonimia.

En los últimos años, las aportaciones que se han hecho desde este dominio han mejorado sustancialmente, permitiendo el procesamiento de ingentes cantidades de información en formato texto con un grado de eficacia aceptable. Muestra de ello es la aplicación de estas técnicas como una componente esencial en los MOTORES DE BÚSQUEDA WEB, en las herramientas de traducción automática, o en la generación automática de resúmenes.

2.	El procesamiento del lenguaje natural en la recuperación de información textual

La complejidad asociada al lenguaje natural cobra especial relevancia cuando necesitamos recuperar información textual que satisfaga la necesidad de información de un usuario. Es por ello, que en el área de Recuperación de Información Textual las técnicas de NLP son muy utilizadas, tanto para facilitar la descripción del contenido de los documentos, como para representar la consulta formulada por el usuario, y ello, con el objetivo de comparar ambas descripciones y presentar al usuario aquellos documentos que satisfagan en mayor grado su necesidad de información.

Un sistema de recuperación de información textual lleva a cabo las siguientes tareas para responder a las consultas de un usuario (imagen 1):

1.	Indexación de la colección de documentos: en esta fase, mediante la aplicación de técnicas de NLP, se genera un índice que contiene las descripciones de los documentos. Normalmente, cada documento es descrito mediante el conjunto de términos que, hipotéticamente, mejor representa su contenido.
2.	Cuando un usuario formula una consulta el sistema la analiza, y si es necesario la transforma, con el fin de representar la necesidad de información del usuario del mismo modo que el contenido de los documentos.
3.	El sistema compara la descripción de cada documento con la descripción de la consulta, y presenta al usuario aquellos documentos cuyas descripciones más se asemejan a la descripción de su consulta.
4.	Los resultados suelen ser mostrados en función de su relevancia, es decir, ordenados en función del grado de similitud entre las descripciones de los documentos y de la consulta.
 
 
 
Imagen 1: Arquitectura de un sistema de recuperación de información.




2.1.	Procesamiento estadístico del lenguaje natural

El procesamiento estadístico del lenguaje natural  representa el modelo clásico de los sistemas de recuperación de información, y se caracteriza porque cada documento está descrito por un conjunto de palabras clave denominadas términos índice.

Este enfoque es muy simple, y se basa en lo que se ha denominado como "bolsa de palabras" (o "bag of words"). En esta aproximación, todas las palabras de un documento se tratan como términos índices para ese documento. Además se asigna un peso a cada término en función de su importancia, determinada normalmente por su frecuencia de aparición en el documento. De este modo, no se toma en consideración el orden, la estructura, el significado, etc. de las palabras.

Estos modelos se limitan, por tanto, a emparejar las palabras en los documentos con las palabras en las consultas. Su simplicidad y eficacia los han convertido hoy en los modelos más utilizados en los sistemas de recuperación de información textual.

En este modelo el procesamiento de los documentos consta de las siguientes etapas:

1.	Pre-procesado de los documentos: consiste fundamentalmente en preparar los documentos para su parametrización, eliminando aquellos elementos que se consideran superfluos.

2.	Parametrización: es una etapa de complejidad mínima una vez se han identificado los términos relevantes. Consiste en realizar una cuantificación de las características (es decir, de los términos) de los documentos.
Vamos a ilustrar su funcionamiento mediante el uso del primer párrafo de este mismo documento, suponiendo que éste está etiquetado en XML. Así, el documento sobre el que aplicaríamos las técnicas de pre-procesado y parametrización sería el siguiente:

 
Ejemplo 2. Documento HTML
 




A.	El pre-procesado de los documentos: consta de tres fases básicas:

1. Eliminación de los elementos del documento que no son objeto de indexación (o stripping), como podrían ser ciertas etiquetas o cabeceras de los documentos (ejemplo 3).
 
 
 
Ejemplo 3. Documento sin cabeceras ni etiquetas

2. Normalización de textos, que consiste en homogeneizar todo el texto de la colección de documentos sobre la que se trabajará, y que afecta por ejemplo a la consideración de los términos en mayúscula o minúscula; el control de determinados parámetros como cantidades numéricas o fechas; el control de abreviaturas y acrónimos, eliminación de palabras vacías mediante la aplicación de listas de palabras función (preposiciones, artículos, etc.), la identificación de N-Gramas (los términos compuestos, subrayados en el ejemplo), etc. (Ejemplo 4).
 
 
 
Ejemplo 4. Documento normalizado

3. Lematización de los términos, que es una parte del procesamiento lingüístico que trata de determinar el lema de cada palabra que aparece en un texto. Su objetivo es reducir una palabra a su raíz, de modo que las palabras clave de una consulta o documento se representen por sus raíces en lugar de por las palabras originales. El lema de una palabra comprende su forma básica más sus formas declinadas. Por ejemplo, "informa" podría ser el lema de "información", "informaciones", e "informar". El proceso de lematización (ejemplo 5) se lleva a cabo utilizando algoritmos de radicación (o stemming), que permiten representar de un mismo modo las distintas variantes de un término, a la vez que reducen el tamaño del vocabulario y mejoran, en consecuencia, la capacidad de almacenamiento de los sistemas y el tiempo de procesamiento de los documentos. No obstante, estos algoritmos presentan el inconveniente de no agrupar en ocasiones palabras que deberían estarlo, y viceversa, mostrar como iguales palabras que realmente son distintas.
 
 
 
Ejemplo 5. Documento con términos lematizados.

Por último, y aunque se han mencionado de pasada, es necesario describir dos técnicas muy utilizadas en el procesamiento estadístico del lenguaje natural, a saber:
a)	La detección de N-Gramas: consiste en la identificación de aquellas palabras que suelen aparecer juntas (palabras compuestas, nombres propios, etc.) con el fin de tratarlas como una sola unidad conceptual. Suele hacerse estimando la probabilidad de que dos palabras que aparecen con cierta frecuencia juntas constituyan realmente un solo término (compuesto). Estas técnicas tratan de identificar términos compuestos tales como "accomodation service" o "European Union".

b)	Listas de palabras vacías o palabras función (stopwords lists): una lista de palabras vacías es un listado de términos (preposiciones, determinantes, pronombres, etc.) considerados de escaso valor semántico, que cuando se identifican en un documento se eliminan, sin considerarse términos índices para la colección de textos a analizar. La supresión de todos estos términos evita los problemas de ruido documental y supone un considerable ahorro de recursos, ya que aunque se trata de un número relativamente reducido de elementos tienen una elevada tasa de frecuencia en los documentos.

B.	La parametrización de los documentos: Consiste en asignar un peso a cada uno de los términos relevantes asociados a un documento. El peso de un término se calcula normalmente en función de su frecuencia de aparición en el documento, e indica la importancia de dicho término como descriptor del contenido de ese documento (ejemplo 6).

 

Ejemplo 6. Fragmento de un documento parametrizado (nótese que las frecuencias asociadas a cada término cambiarían a medida que se avanzara en la cuantificación de los restantes términos del documento).

Uno de los métodos más utilizados para estimar la importancia de un término es el conocido sistema TF.IDF (Term Frecuency, Inverse Document Frecuency). Está pensado para calcular la importancia de un término en función de su frecuencia de aparición en un documento, pero supeditado a su frecuencia de aparición total en el conjunto de documentos de la colección. Es decir, el hecho de que un término aparezca muchas veces en un documento es indicativo de que ese término es representativo del contenido del mismo, pero siempre y cuando este término no aparezca con una frecuencia muy alta en todos los documentos. De ser así, no tendría ningún valor discriminatorio (por ejemplo, en una base de datos de recetas no tendría ningún sentido representar el contenido de un documento por la palabra alimento, por más veces que ésta aparezca).


Imagen 7: Frecuencia de Término (FT)
(A mayor número de operaciones mayor score)

 

Imagen 8: Frecuencia inversa de documento (IDF)
(Mayor será el score cuanto menos frecuente sea el término a lo largo de los documentos)

TF-IDF, es la combinación de la frecuencia de término y la frecuencia inversa de documento, esto permite definir un peso para cada término en cada documento.
      
Imagen 9: Formula TF-IDF

Características:
•	Alto para aquellos términos que aparecen muchas veces en pocos documentos.
•	Bajo para aquellos términos que aparezcan pocas veces o en muchos documentos.
•	Bajo para aquellos términos que aparezcan en prácticamente todos los documentos (stop words)




2.2.	Modelo espacio vectorial

•	Al trabajar con vectores se puede calcular el producto escalar entre los documentos.
•	El conjunto de documentos debe verse como un conjunto de vectores en un espacio vectorial donde cada eje será cada término

 
Imagen 10: Similitud Coseno

Para poder calcular el espacio vectorial, necesitamos de la matríz de incidencia.(Imagen 11) Dicha estructura podría ser alimentada con los valores obtenidos con el sistema TF-IDF  o por coincidencias. Como se puede notar es un cruce de información entre el corpus y las palabras tokenizadas. 
Imagen 11: Similitud Coseno

Al trabajar con vectores se puede calcular el producto escalar entre los documentos y es útil para comparar documentos

 
Imagen 12: Similitud Coseno
3. Sugerencias
	Para un proceso de búsqueda más rápido se sugiere generar la matriz de incidencia antes de correr el programa. Es decir almacenarlo en un dataframe o matriz sparse en forma inversa.

	Para alivianar el peso de la matriz de incidencia debemos almacenarla como una matriz inversa dejando los 0s de lado.

	Existen funciones que deberían revisarse, como el proceso de lematización. Porque estas funciones utilizadas están escritas por personas de habla inglesa; a pesar de que tiene la opción de ponerlo en español se nota que no manipula bien las palabras del idioma.

	Para mejorar la salida del sistema se debería de involucrar al usuario (feedback). 

Feedback explícito: Entrenar al sistema de la siguiente forma:

1.	Un usuario realiza una consulta
2.	El sistema devuelve un conjunto de resultados
3.	El usuario anota algunos resultados como relevantes y no relevantes
4.	El sistema recalcula una mejor representación de la información
5.	El sistema devuelve una versión revisada de los resultados.

Feedback implícito: En este caso la relevancia de los documentos se infiere en base al comportamiento de los usuarios:
•	Qué documentos se seleccionan y cuáles no
•	Acciones en la búsqueda y scrolling
•	Duración del tiempo que un usuario pasa leyendo un documento (Dwell time)

	Para expansión de consultas se sugiere involucrar tareas de búsqueda de sinónimos y corrección de faltas ortográficas.

	Por último hace falta aplicar algunas técnicas más de NLP para mejorar el los sistemas de recuperación:
•	Corrección de errores
•	Detección de sinónimos
•	Desambiguación lingüística
•	Detección de términos relevantes en la consulta
•	Detección de la intención en la consulta
•	Detención de entidades en la consulta
•	Clasificación de documentos.
 
4. Links
•	https://es.wikipedia.org/wiki/Wikipedia:Descargas
•	https://pypi.org/project/zimscan/
•	https://www.upf.edu/hipertextnet/numero-5/pln.html
•	https://www.notion.so/NLP-Natural-Language-Processing-32a706bbb0b64481ab597146e8b7abdc
•	https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-busqueda
•	https://jordycuan.github.io/2016/03/27/indexado-1/
•	https://jarroba.com/scraping-python-beautifulsoup-ejemplos/
•	https://medium.com/datos-y-ciencia/preprocesamiento-de-datos-de-texto-un-tutorial-en-python-5db5620f1767
•	https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-search-and-dom-modification--cms-28276
•	https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
•	https://www.w3resource.com/numpy/input-and-output/memmap.php
•	https://www.diegocalvo.es/dataframes-in-python/
•	https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
•	https://www.researchgate.net/post/How_to_append_TF-IDF_vector_into_pandas_dataframe
•	https://stackoverflow.com/questions/44193154/notfittederror-tfidfvectorizer-vocabulary-wasnt-fitted
•	http://thiagomarzagao.com/2015/12/08/saving-TfidfVectorizer-without-pickles/
•	https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a
•	https://medium.com/@hdezfloresmiguelangel/implementando-un-corrector-ortogr%C3%A1fico-en-python-utilizando-la-distancia-de-levenshtein-498ec0dd1105
•	https://flask.palletsprojects.com/en/1.1.x/
•	https://es.wikipedia.org/wiki/Wikipedia:Descargas
