<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem-vindo ao BMVC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .welcome-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        p {
            color: #666;
            margin-bottom: 30px;
            line-height: 1.5;
        }
        .btn-login {
            display: inline-block;
            background-color: #28a745; /* Cor verde para destacar */
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        .btn-login:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="welcome-container">
        <h1>Seja Bem-vindo!</h1>
        <p>Ao Sistema de Gestão Acadêmica FullStack desenvolvido sobre a arquitetura BMVC.</p>
        
        <!-- O segredo está aqui: o link aponta para a rota do portal -->
        <a href="/portal" class="btn-login">Ir para o Login</a>
    </div>
</body>
</html>