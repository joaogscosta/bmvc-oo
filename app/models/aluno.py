class Aluno:
    def __init__(self, id_aluno, nome, nota1, nota2):
        self.id = id_aluno
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    