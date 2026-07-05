<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Login - BMVC</title>
    <link rel="stylesheet" type="text/css" href="/static/css/portal.css">
</head>
<body class="login-body">

    <div class="login-container">
        <h1>Login</h1>
        
       
        % if erro:
            <div style="color: #c0392b; background-color: #fce4e4; padding: 10px; border: 1px solid #f5c6cb; border-radius: 4px; margin-bottom: 15px; text-align: center; font-size: 14px; font-weight: bold;">
                ⚠️ {{erro}}
            </div>
        % end
        
        <form action="/portal" method="post">
            <p>
                <label for="username">Nome:</label>
                <input id="username" name="username" type="text" required />
            </p>

            <p>
                <label for="password">Senha:</label>
                <input id="password" name="password" type="password" required />
            </p>

            <p>
                <input value="Login" type="submit" class="btn-login" />
            </p>
        </form>
        
        <a href="/" class="login-back-link">Voltar para a Página Inicial</a>
    </div>

</body>
</html>