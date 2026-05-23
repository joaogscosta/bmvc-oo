import os
import bottle
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response

# Força o Bottle a escanear unicamente a pasta onde estão as suas páginas HTML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIEWS_DIR = os.path.join(BASE_DIR, 'app', 'views', 'html')
bottle.TEMPLATE_PATH = [VIEWS_DIR]

app = Bottle()
ctl = Application()

#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')

#-----------------------------------------------------------------------------
@app.route('/')
@app.route('/pagina')
def pagina():
    return ctl.render('pagina')




@app.route('/alunos')
def alunos():
    return ctl.render('alunos') 

@app.route('/notas')
def notas():
    return ctl.render('notas')  

@app.route('/aprovados')
def aprovados():
    return ctl.render('aprovados')

@app.route('/reprovados')
def reprovados():     
    return ctl.render('reprovados') 

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)