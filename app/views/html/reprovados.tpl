<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Alunos Reprovados</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>

    <nav class="navbar">
        <a href="/notas">📋 Ver Boletim</a>
        <a href="/aprovados">✅ Alunos Aprovados</a>
        <a href="/reprovados">❌ Alunos Reprovados</a>
        <a href="/logout" style="color: #e74c3c;">🚪 Sair</a>
    </nav>

    <h1>Lista de Alunos Reprovados</h1>

    <table>
        <thead>
            <tr>
                <th>Aluno</th>
                <th>Nota 1</th>
                <th>Nota 2</th>
                <th>Média</th>
            </tr>
        </thead>
        <tbody>
            % for aluno in reprovados:
                <tr>
                    <td>{{aluno.nome}}</td>
                    <td>{{aluno.nota1}}</td>
                    <td>{{aluno.nota2}}</td>
                    <td>{{aluno.calcular_media()}}</td>
                </tr>
            % end
        </tbody>
    </table>

    <a href="/notas" class="btn-voltar">Voltar para o Boletim</a>

    <script src="/static/js/interactions.js"></script>
</body>
</html>