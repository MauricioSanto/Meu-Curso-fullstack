// script.js
const menuIcon = document.querySelector('.icon');
const dropdownMenu = document.querySelector('.dropdown-menu'); // Seu menu suspenso

menuIcon.addEventListener('mouseenter', () => {
    dropdownMenu.style.display = 'block'; // Exibe o menu suspenso
});

menuIcon.addEventListener('mouseleave', () => {
    dropdownMenu.style.display = 'none'; // Oculta o menu suspenso
});
