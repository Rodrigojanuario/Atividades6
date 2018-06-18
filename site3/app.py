#coding: UTF-8

from flask impot Flask, render_template, request
 
app = Flask (_ name_)

@app.route("/")
def pagina_index():
    return render_template ("index.html")
	
@app.route("/dados/<tipo>/<marca>/<material>/")
def pagina_dados(tipo, marca, material):
    return render_template("index.html",**locals()
