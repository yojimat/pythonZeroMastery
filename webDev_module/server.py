from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)


def valid_login(login, senha):
    if(login == "vinicius" and senha == "neves"):
        return True
    return False


@app.route("/vinicius/<int:id>")
def vinicius(id):
    return f"Como vai vinicius? Mantenha o foco! Id:{id}"


@app.route("/")
def hello_world_html():
    url_for("static", filename="/css/main.css")
    url_for("static", filename="/js/jquery.min.js")
    url_for("static", filename="/js/browser.min.js")
    url_for("static", filename="/js/breakpoints.min.js")
    url_for("static", filename="/js/util.js")
    url_for("static", filename="/js/main.js")
    url_for("static", filename="/images/pic01.jpg")
    url_for("static", filename="/images/pic02.jpg")
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    error = None
    if valid_login(request.form['login'], request.form['senha']):
        return render_template('index.html', resultado=f"Usuário {request.form['login']} correto!", error=False)
    else:
        error = 'Usuário ou senha inválidos'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', resultado=error, error=True)


def salvaMensagemCsv(mensagem, nome):
    with open("mensagem.csv", mode='a') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([mensagem, nome])

@app.route("/mensagempost", methods=["POST"])
def mensagemPost():
    if len(request.form['mensagem']) <= 0:
        return render_template("index.html", resposta="Nenhuma mensagem enviada.")
    salvaMensagemCsv(request.form["mensagem"], request.form["nome"])
    return render_template("index.html", resposta=f"Mensagem -> '{request.form['mensagem']}' foi enviada!")
