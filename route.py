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
# Rotas de Arquivos Estáticos (CSS e JS):

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    # Cria um caminho absoluto e seguro até a pasta app/static
    static_path = os.path.join(BASE_DIR, 'app', 'static')
    return static_file(filepath, root=static_path)

#-----------------------------------------------------------------------------
# Rotas de Leitura Existentes:

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')

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

@app.route('/logout')
def logout():
    ctl.logout_user()
    redirect('/portal')

# Rota para CARREGAR a página (quando você entra no link)
@app.route('/portal', method='GET')
def login():
    return ctl.render('portal')

# Rota para PROCESSAR o formulário (quando você clica no botão Login)
# ATENÇÃO: Verifique se o método está exatamente como 'POST'
@app.route('/portal', method='POST')
def action_portal():
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    # Faz a autenticação usando o DataRecord
    result = ctl.authenticate_user(username, password)
    
    if result:
        session_id, user_nome = result
        # Define o cookie de sessão (secure=False para rodar em localhost)
        response.set_cookie('session_id', session_id, httponly=True, secure=False, max_age=3600)
        redirect('/notas') # Login deu certo, vai pro CRUD
    else:
        # Se falhar, recarrega a página exibindo o erro na tela!
        return ctl.render('portal', parameter='erro_login')
#-----------------------------------------------------------------------------
# 🆕 NOVAS ROTAS ADICIONADAS PARA O CRUD COMPLETO:
#-----------------------------------------------------------------------------

# 1. ROTA DO CREATE (Envia os dados do formulário de cadastro)
@app.route('/cadastrar', method='POST')
def cadastrar():
    return ctl.cadastrar_aluno()

# 2. ROTA DO UPDATE - PARTE 1 (Abre a página com o formulário de edição)
@app.route('/editar/<id_aluno>')
def editar(id_aluno):
    # Passamos o id_aluno como parâmetro para o render buscar o aluno certo
    return ctl.render('editar_aluno', parameter=id_aluno)

# 3. ROTA DO UPDATE - PARTE 2 (Recebe os dados editados e atualiza a lista)
@app.route('/atualizar/<id_aluno>', method='POST')
def atualizar(id_aluno):
    return ctl.atualizar_aluno(id_aluno)

# 4. ROTA DO DELETE (Remove o aluno da lista)
@app.route('/deletar/<id_aluno>')
def deletar(id_aluno):
    return ctl.deletar_aluno(id_aluno)

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)