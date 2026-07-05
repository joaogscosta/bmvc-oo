<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Notas dos Alunos</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>
    <h1>Boletim de Notas</h1>

    <div class="form-container">
        <h3>Cadastrar Novo Aluno</h3>
        <form action="/cadastrar" method="POST">
            <p>
                <input type="text" name="nome" placeholder="Nome do Aluno" required>
            </p>
            <p>
                <input type="number" step="0.1" name="nota1" placeholder="Nota 1" min="0" max="10" required>
            </p>
            <p>
                <input type="number" step="0.1" name="nota2" placeholder="Nota 2" min="0" max="10" required>
            </p>
            <div class="form-actions" style="justify-content: flex-end;">
                <button type="submit" class="btn-save">Adicionar Aluno</button>
            </div>
        </form>
    </div>

    <table>
        <thead>
            <tr>
                <th>Aluno</th>
                <th>Nota 1</th>
                <th>Nota 2</th>
                <th>Média</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for aluno in lista_alunos:
                <tr>
                    <td>{{aluno.nome}}</td>
                    <td>{{aluno.nota1}}</td>
                    <td>{{aluno.nota2}}</td>
                    <td>{{aluno.calcular_media()}}</td>
                    <td class="action-links">
                        <a href="/editar/{{aluno.id}}" class="action-edit">Editar</a>
                        <a href="/deletar/{{aluno.id}}" class="action-delete" onclick="return confirmarDelecao(event, '{{aluno.nome}}')">Deletar</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
    
    <a href="/helper" class="btn-voltar">Voltar para o Menu Principal</a>

    <script src="/static/js/interactions.js"></script>
</body>
</html>