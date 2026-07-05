# app/controllers/application.py
from bottle import template, request, redirect
from app.models.aluno import Aluno
from app.controllers.db.datarecord import DataRecord  # 🔄 Usando a infraestrutura correta

class Application():

    def __init__(self):
        # Instancia unicamente o DataRecord como administrador do banco
        self.__model = DataRecord()
        self.__current_username = None
        
        self.pages = {
            'pagina': self.pagina,
            'helper': self.helper,
            'portal': self.portal,
            'alunos': self.alunos,
            'notes': self.notas, 
            'notas': self.notas,
            'aprovados': self.aprovados,
            'reprovados': self.reprovados,
            'editar_aluno': self.editar_aluno
        }

    # ==========================================
    #   MÉTODOS DE AUTENTICAÇÃO (SESSÃO)
    # ==========================================

    def get_session_id(self):
        """Resgata o cookie de sessão do navegador"""
        from bottle import request
        return request.get_cookie('session_id')

    def authenticate_user(self, username, password):
        """Verifica as credenciais e autentica o usuário gerando uma sessão"""
        session_id = self.__model.checkUser(username, password)
        if session_id:
            self.logout_user() 
            self.__current_username = self.__model.getUserName(session_id)
            return session_id, username
        return None

    def logout_user(self):
        """Desconecta o usuário limpando o registro do banco de autenticados"""
        self.__current_username = None
        session_id = self.get_session_id()
        if session_id:
            self.__model.logout(session_id)

    # ==========================================
    #   PÁGINAS DO BOLETIM (READ & FILTROS)
    # ==========================================

    def pagina(self):
        return template('pagina')
    
    def helper(self):
        return template('helper')

    def portal(self, erro=None):
        """Renderiza a página de login e passa mensagem de erro se houver"""
        if erro == 'erro_login':
            return template('portal', erro="Usuário ou senha incorretos!")
        
        # Se não houver erro, passa erro como None para o template não quebrar
        return template('portal', erro=None)

    def render(self, page, parameter=None):
        """Controlador de Acesso: Bloqueia páginas caso não haja cookie ativo"""
        session_id = self.get_session_id()
        user_logado = self.__model.getUserName(session_id)
        
        if not user_logado and page not in ['portal', 'helper']:
            redirect('/portal')
            
        content = self.pages.get(page, self.helper)
        if parameter:
            return content(parameter)
        return content()
    
    def alunos(self):       
        # 🆕 Busca da lista unificada da administradora
        return template('alunos', alunos=self.__model.lista_alunos)

    def notas(self):
        # 🆕 Busca da lista unificada da administradora
        return template('notas', lista_alunos=self.__model.lista_alunos)

    def aprovados(self):
        # 🆕 Filtra a partir dos dados do DataRecord
        alunos_aprovados = [aluno for aluno in self.__model.lista_alunos if aluno.calcular_media() >= 6.0]
        return template('aprovados', aprovados=alunos_aprovados)

    def reprovados(self):
        # 🆕 Filtra a partir dos dados do DataRecord
        alunos_reprovados = [aluno for aluno in self.__model.lista_alunos if aluno.calcular_media() < 6.0]
        return template('reprovados', reprovados=alunos_reprovados)

    # ==========================================
    #   MÉTODOS OPERACIONAIS DO CRUD (C-U-D)
    # ==========================================

    # 1. CREATE: Adiciona na lista do DataRecord e salva no JSON da pasta 'db'
    def cadastrar_aluno(self):
        nome = request.forms.get('nome')
        nota1 = float(request.forms.get('nota1'))
        nota2 = float(request.forms.get('nota2'))
        
        novo_id = max([aluno.id for aluno in self.__model.lista_alunos], default=0) + 1
        novo_aluno = Aluno(novo_id, nome, nota1, nota2)
        
        # Salva utilizando a classe administradora
        self.__model.lista_alunos.append(novo_aluno)
        self.__model.save_alunos()
        
        redirect('/notas')

    # 2. UPDATE (Parte 1): Busca o aluno pelo ID dentro do DataRecord
    def editar_aluno(self, id_aluno):
        aluno_encontrado = None
        for aluno in self.__model.lista_alunos:
            if aluno.id == int(id_aluno):
                aluno_encontrado = aluno
                break
        return template('editar_aluno', aluno=aluno_encontrado)

    # 3. UPDATE (Parte 2): Modifica o aluno no DataRecord e persiste no disco
    def atualizar_aluno(self, id_aluno):
        nome = request.forms.get('nome')
        nota1 = float(request.forms.get('nota1'))
        nota2 = float(request.forms.get('nota2'))
        
        for aluno in self.__model.lista_alunos:
            if aluno.id == int(id_aluno):
                aluno.nome = nome
                aluno.nota1 = nota1
                aluno.nota2 = nota2
                break
        
        self.__model.save_alunos()
        redirect('/notas')

    # 4. DELETE: Filtra a lista da administradora removendo o ID e salva
    def deletar_aluno(self, id_aluno):
        self.__model.lista_alunos = [aluno for aluno in self.__model.lista_alunos if aluno.id != int(id_aluno)]
        
        self.__model.save_alunos()
        redirect('/notas')