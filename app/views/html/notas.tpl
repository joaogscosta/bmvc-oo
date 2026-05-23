<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Notas dos Alunos</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>
    <h1>Boletim de Notas</h1>
    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>Aluno</th>
                <th>Nota 1</th>
                <th>Nota 2</th>
                <th>Média</th>
            </tr>
        </thead>
        <tbody>
            <!-- Varre a lista de objetos Aluno -->
            % for aluno in lista_alunos:
                <tr>
                    <!-- Acessa as propriedades do objeto diretamente -->
                    <td>{{aluno.nome}}</td>
                    <td>{{aluno.nota1}}</td>
                    <td>{{aluno.nota2}}</td>
                    <!-- Chama o método calcular_media() que você criou na classe! -->
                    <td>{{aluno.calcular_media()}}</td>
                </tr>
            % end
        </tbody>
    </table>
    <br>
    <a href="/helper">Voltar para o Menu Principal</a>
</body>
</html>