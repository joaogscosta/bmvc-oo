// interactions.js

document.addEventListener("DOMContentLoaded", function() {
    const image = document.querySelector("img");

    if (image) {
        image.addEventListener("click", function() {
            // Mudar a cor de fundo aleatoriamente
            document.body.style.backgroundColor = getRandomColor();

            // Criar e mostrar a mensagem animada
            showAnimatedMessage("Você clicou na imagem!");
        });
    }

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    function showAnimatedMessage(message) {
        // Criar o elemento da mensagem
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('animated-message');
        messageDiv.innerText = message;
        document.body.appendChild(messageDiv);

        // Remover a mensagem após um tempo
        setTimeout(() => {
            document.body.removeChild(messageDiv);
        }, 2000);
    }
});

function confirmarDelecao(event, nomeAluno) {
    const confirmacao = confirm(`Tem certeza que deseja remover o(a) aluno(a) ${nomeAluno}?`);
    if (!confirmacao) {
        event.preventDefault(); // Intercepta e cancela a rota do Bottle se clicar em Cancelar
        return false;
    }
    return true;
}
