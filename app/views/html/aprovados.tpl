<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Alunos Aprovados</title>
    <link rel="stylesheet" type="text/css" href="/static/css/boletim.css">
</head>
<body>
    <h1 style="color: green;">🎉 Alunos Aprovados (Média &ge; 6.0)</h1>
    <ul>
        <!-- O Bottle vai ler a lista 'aprovados' que enviamos pelo controlador -->
        % for nome in aprovados:
            <li><strong>{{nome}}</strong> - Parabéns!</li>
        % end
    </ul>
    <br>
    <a href="/helper">Voltar para o Menu Principal</a>
</body>
</html>