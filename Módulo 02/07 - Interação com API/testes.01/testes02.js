// script.js
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const cardList = document.querySelector('.card-list');
let currentIndex = 0;

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + cardList.children.length) % cardList.children.length;
    updateCarousel();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % cardList.children.length;
    updateCarousel();
});

function updateCarousel() {
    cardList.style.transform = `translateX(-${currentIndex * 100}%)`;
}
