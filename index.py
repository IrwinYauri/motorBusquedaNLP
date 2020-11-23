from flask import Flask, render_template, request
import controlador
from Tratamiento import Corrector

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if 'q' in request.form:
        p = request.form['q']
        #return "enviado: "+movies  
        obj=controlador.Procesar()
        arr=obj.buscar(p,15)
        #dat=obj.getPagina(arr[0])
        corr=Corrector()
        sug=corr.corregirTexto(p)
        if sug == p:
            corrRpt=""
        else:
            corrRpt=sug

        return render_template('home.html',cadena=p,rpt=arr,mejor=arr[0]["indice"],corrector=corrRpt)
    else:
        return render_template('inicio.html')

@app.route('/<search>')
def search(search):        
    #return "enviado: "+movies  
    obj=controlador.Procesar()
    arr=obj.buscar(search,20)
    #dat=obj.getPagina(arr[0])    
    return render_template('home.html',cadena=search,rpt=arr,mejor=arr[0]["indice"],corrector="")


@app.route("/resultado/<indice>")
def resultados(indice):
    obj=controlador.Procesar()
    #arr=obj.buscar(p,5)
    data=obj.getPagina(int(indice))
    return f"{data}" 

@app.route("/resIndividual/<indice>")
def resIndividual(indice):    
    return render_template('resIndividual.html',indice=indice)

if __name__ == '__main__':
    app.run(debug=True)