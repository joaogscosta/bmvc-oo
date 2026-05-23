from bottle import template
from app.models.aluno import Aluno

class Application():

    def __init__(self):
        
       self.lista_alunos = [
        Aluno("João", 8.5, 9.0),
        Aluno("Maria", 7.0, 6.5),
        Aluno("Carlos", 4.0, 5.5),
        Aluno("Gabriela", 9.5, 10.0),
        Aluno("Breno", 4.6, 2.3),
        Aluno("Vitoria", 10.0, 9.2),
        Aluno("Leonardo", 4.5, 10.0)

    ]
    
        
        
       self.pages = {
        'pagina': self.pagina,
        'helper': self.helper,
        'portal': self.portal,
        'alunos': self.alunos,
        'notas': self.notas,
        'aprovados': self.aprovados,
        'reprovados': self.reprovados
        }
    
    def pagina(self):
        return template('pagina')
    
    def portal(self):
        return template('portal')
    
    

    def render(self, page, parameter=None):
       content = self.pages.get(page, self.pagina)
       return content()
    
    def alunos(self):       
        # Passando apenas o nome simples relativo
        return template('alunos', alunos=self.lista_alunos)

    def notas(self):
        return template('notas', lista_alunos=self.lista_alunos)

    def aprovados(self):
        alunos_aprovados = [aluno.nome for aluno in self.lista_alunos if aluno.calcular_media() >= 6.0]
        return template('aprovados', aprovados=alunos_aprovados)

    def reprovados(self):
       alunos_reprovados = [aluno.nome for aluno in self.lista_alunos if aluno.calcular_media() < 6.0]
       return template('reprovados', reprovados=alunos_reprovados)

    def helper(self):
        return template('helper')