<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Login - BMVC</title>
</head>
<body>
    <div style="max-width: 300px; margin: 50px auto; font-family: Arial, sans-serif;">
        <h1>Login</h1>
        
        <!-- Esse formulário envia os dados para a rota POST /portal que está no route.py -->
        <form action="/portal" method="post">
            <p>
                <label for="username">Nome:</label><br>
                <input id="username" name="username" type="text" required style="width: 100%; padding: 5px;" />
            </p>

            <p>
                <label for="password">Senha:</label><br>
                <input id="password" name="password" type="password" required style="width: 100%; padding: 5px;" />
            </p>

            <p>
                <input value="Login" type="submit" style="padding: 5px 15px; cursor: pointer;" />
            </p>
        </form>
        
        <br>
        <a href="/">Voltar para a Página Inicial</a>
    </div>
</body>
</html>