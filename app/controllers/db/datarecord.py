import json
import os
import uuid
from app.models.user_adm import UserAdm
from app.models.aluno import Aluno

class DataRecord:
    """
    Classe Administradora do Banco de Dados (Infraestrutura)
    Centraliza a persistência em disco dos modelos UserAdm e Aluno.
    """

    def __init__(self):
        # Define o caminho apontando para dentro de app/controllers/db
        self.db_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(self.db_dir, "user_accounts.json")
        self.alunos_file = os.path.join(self.db_dir, "alunos.json")
        
        # Listas internas que espelham o "banco de dados" em memória
        self.user_accounts = []
        self.lista_alunos = []
        
        # Controle de sessões (autenticação em memória)
        self.__authenticated_users = {}
        
        # Carrega os dados do disco ao iniciar
        self.read_all()

    # ==========================================
    #   PERSISTÊNCIA EM DISCO (LEITURA E ESCRITA)
    # ==========================================

    def read_all(self):
        """Lê todos os arquivos JSON do disco"""
        # --- Carga de Usuários ---
        try:
            with open(self.users_file, "r") as f:
                user_data = json.load(f)
                self.user_accounts = [UserAdm(**data) for data in user_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.user_accounts = [UserAdm('admin', 'unb123'), UserAdm('Henrique', '123456')]
            self.save_users()

        # --- Carga de Alunos ---
        try:
            with open(self.alunos_file, "r") as f:
                aluno_data = json.load(f)
                self.lista_alunos = [Aluno(d['id'], d['nome'], d['nota1'], d['nota2']) for d in aluno_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista_alunos = [
                Aluno(1, "João", 8.5, 9.0),
                Aluno(2, "Maria", 7.0, 6.5),
                Aluno(3, "Carlos", 4.0, 5.5)
            ]
            self.save_alunos()

    def save_users(self):
        """Salva a lista de usuários no arquivo JSON"""
        with open(self.users_file, "w") as f:
            data = [{"username": u.username, "password": u.password} for u in self.user_accounts]
            json.dump(data, f, indent=4)

    def save_alunos(self):
        """Salva a lista de alunos no arquivo JSON"""
        with open(self.alunos_file, "w") as f:
            data = [{"id": a.id, "nome": a.nome, "nota1": a.nota1, "nota2": a.nota2} for a in self.lista_alunos]
            json.dump(data, f, indent=4)

    # ==========================================
    #   MÉTODOS DE GERENCIAMENTO DE USUÁRIOS/SESSÃO
    # ==========================================

    def checkUser(self, username, password):
        for user in self.user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())
                self.__authenticated_users[session_id] = user
                return session_id
        return None

    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id]

    def getUserName(self, session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id].username
        return None

    def getCurrentUser(self, session_id):
        return self.__authenticated_users.get(session_id, None)