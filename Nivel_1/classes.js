class Aluno {
    constructor(nome, idade, matricula) {
        this.nome = nome;
        this.idade = idade;
        this.matricula = matricula;
    } 
    cadastrar() {
        console.log(`Aluno ${this.nome} cadastrado com sucesso!`);      
    }           
}

class Professor {
    constructor(nome, idade, disciplina) {
        this.nome = nome;
        this.idade = idade;
        this.disciplina = disciplina;
    }
    cadastrar() {
        console.log(`Professor ${this.nome} cadastrado com sucesso!`);      
    }
}

class Curso {
    constructor(nome, duracao) {
        this.nome = nome;
        this.duracao = duracao;
    }
    cadastrar() {
        console.log(`Curso ${this.nome} cadastrado com sucesso!`);      
    }
}

class Turma {
    constructor(nome, curso) {
        this.nome = nome;
        this.curso = curso;
    }

    cadastrar() {
        console.log(`Turma ${this.nome} cadastrada com sucesso!`);      
    }           
}