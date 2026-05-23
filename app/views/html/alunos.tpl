<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Lista de Alunos</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>
    <h1>Alunos Cadastrados</h1>
    <ul>
        <!-- O '%' indica linha de código Python no Bottle -->
        % for aluno in alunos:
            <!-- Se você passou o objeto, usamos aluno.nome -->
            <li>{{aluno.nome}}</li>
        % end
    </ul>
    <br>
    <a href="/helper">Voltar para o Menu Principal</a>
</body>
</html>