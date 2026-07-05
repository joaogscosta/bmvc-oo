import json
import os
from app.models.user_adm import UserAdm

class UserRepository:
    """Responsável exclusivamente por ler e salvar usuários no JSON (Model)"""
    
    def __init__(self):
        # Mudamos o caminho para uma pasta 'database' na raiz do projeto
        self.db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../database'))
        self.filename = os.path.join(self.db_dir, "user_accounts.json")
        self.user_accounts = []
        self.read()

    def read(self):
        # Garante que a pasta 'database' exista
        os.makedirs(self.db_dir, exist_ok=True)
        
        try:
            with open(self.filename, "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                # Reconstrói os objetos UserAdm a partir do JSON
                self.user_accounts = [UserAdm(**data) for data in user_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo JSON não encontrado ou vazio. Criando usuários padrão...")
            self.user_accounts.append(UserAdm('admin', 'unb123'))
            self.user_accounts.append(UserAdm('Henrique', '123456'))
            self.save()

    def save(self):
        with open(self.filename, "w") as arquivo_json:
            # Converte os objetos UserAdm para dicionários para poder salvar no JSON
            data = [{"username": user.username, "password": user.password} for user in self.user_accounts]
            json.dump(data, arquivo_json, indent=4)

    def find_all(self):
        return self.user_accounts

    def find_by_username(self, username):
        for user in self.user_accounts:
            if user.username == username:
                return user
        return None

    def add_user(self, username, password):
        # Caso você queira implementar uma tela de cadastro futuramente
        if not self.find_by_username(username):
            novo_usuario = UserAdm(username, password)
            self.user_accounts.append(novo_usuario)
            self.save()
            return True
        return False
    
    # No seu app/models/user_repository.py, adicione estes métodos:

    def create(self, username, password):
        """CREATE: Adiciona um novo usuário se ele não existir"""
        if not self.find_by_username(username):
            novo_usuario = UserAdm(username, password)
            self.user_accounts.append(novo_usuario)
            self.save() # Salva no JSON imediatamente
            return True
        return False # Usuário já existe

    def update(self, username, new_password):
        """UPDATE: Atualiza a senha de um usuário existente"""
        user = self.find_by_username(username)
        if user:
            user.password = new_password
            self.save() # Salva a alteração no JSON
            return True
        return False

    def delete(self, username):
        """DELETE: Remove um usuário da lista"""
        user = self.find_by_username(username)
        if user:
            self.user_accounts.remove(user)
            self.save() # Atualiza o arquivo JSON sem o usuário
            return True
        return False