// script.js
const form = document.getElementById('cadastro-form');
const conteudo = document.getElementById('conteudo');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;

    // Simule o cadastro (pode ser substituído por uma chamada a um servidor)
    // Aqui, vamos apenas exibir o conteúdo após o cadastro
    conteudo.style.display = 'block';
});
