<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Editar Aluno</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
    <script src="/static/js/interactions.js"></script>
</head>
<body>
    <h1>Editar Cadastro do Aluno</h1>

    <div class="form-container" style="padding: 15px; border: 1px solid #ccc; display: inline-block;">
        <h3>Alterar Notas de {{aluno.nome}}</h3>
        
        <form action="/atualizar/{{aluno.id}}" method="POST">
            
            <p>
                <label for="nome">Nome do Aluno:</label><br>
                <input type="text" id="nome" name="nome" value="{{aluno.nome}}" required>
            </p>
            
            <p>
                <label for="nota1">Nota 1:</label><br>
                <input type="number" step="0.1" id="nota1" name="nota1" value="{{aluno.nota1}}" min="0" max="10" required>
            </p>
            
            <p>
                <label for="nota2">Nota 2:</label><br>
                <input type="number" step="0.1" id="nota2" name="nota2" value="{{aluno.nota2}}" min="0" max="10" required>
            </p>
            
            <button type="submit" style="background-color: #28a745; color: white; padding: 5px 10px; cursor: pointer;">
                Salvar Alterações
            </button>
            <a href="/notas" style="margin-left: 10px; color: gray; text-decoration: none;">Cancelar</a>
        </form>
    </div>

    <script src="/static/js/interactions.js"></script>
</body>
</html>