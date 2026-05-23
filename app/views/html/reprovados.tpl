<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Alunos Reprovados</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>
    <h1 style="color: red;">⚠️ Alunos de Recuperação (Média &lt; 6.0)</h1>
    <ul>
        <!-- O Bottle vai ler a lista 'reprovados' que enviamos pelo controlador -->
        % for nome in reprovados:
            <li><strong>{{nome}}</strong> - Precisa estudar mais para a final.</li>
        % end
    </ul>
    <br>
    <a href="/helper">Voltar para o Menu Principal</a>
</body>
</html>