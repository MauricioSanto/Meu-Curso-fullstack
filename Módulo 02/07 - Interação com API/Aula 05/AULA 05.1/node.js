async function busca() {
    let procura = await fetch("carrosImpor.json");
    let produtos = await procura.json();
    let listdiv = document.getElementById("lista-card");
    
    for (let item of produtos) {
        let card = document.createElement('div');
        card.classList.add('card');
        card.innerHTML = `
            <div class="grupo-img">
                <img src="${item.img[0]}" width="250" height="auto">
            </div>
            <div class="textos">
                <h3>${item.nome}</h3>
                <p> Descrição: ${item.Descrição}</p>
                <div>
                    <p> R$ ${(item.Preço).toFixed(2).replace(".", ",")}</p>
                    <p> Ano ${item.Ano}</p>
                    <p> KM ${item.Quilometragem}</p>
                </div>
            </div>
        `;
        listdiv.appendChild(card);
    }

    // Adiciona efeito de carrossel
    let currentIndex = 0;
    let cardWidth = 300; // Largura de cada card em pixels
    let visibleCards = 3; // Número de cards visíveis por vez
    let totalCards = produtos.length;

    function showCards() {
        let offset = -currentIndex * cardWidth;
        listdiv.style.transform = `translateX(${offset}px)`;
    }

    function prevCard() {
        currentIndex = Math.max(0, currentIndex - 1);
        showCards();
    }

    function nextCard() {
        currentIndex = Math.min(totalCards - visibleCards, currentIndex + 1);
        showCards();
    }

    // Event listeners para os botões de navegação
    document.getElementById("prevBtn").addEventListener('click', prevCard);
    document.getElementById("nextBtn").addEventListener('click', nextCard);

    // Exibe os cards iniciais
    showCards();
    let elementosCards = document.querySelectorAll(".card")
    for(let card of elementosCards){
        card.addEventListener("click",cliquei)
    }
}


busca();
function cliquei(){
    let elementoId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?id=" + elementoId
}

/*
async function busca(){
    let procura = await fetch("carrosImpor.json")
    let produtos = await procura.json()
    //console.log(produtos)
    let listdiv = document.getElementById("lista-card")
    for(let item of produtos){
        listdiv.innerHTML += `
            <div class="card" data-id = "${item.id}">
                <div class="grupo-img">
                    <img src="${item.img[0]}" width="250" height="auto">
                </div>
                <div class="textos">
                    <h3>${item.nome}</h3>
                    <p> Descrição: ${item.Descrição}</p>
                    <div>
                       <p> R$ ${(item.Preço).toFixed(2).replace(".",",")}</p>
                       <p> Ano ${item.Ano}</P>
                       <p> KM ${item.Quilometragem}</p>
                        
                    </div>

                </div>
            </div>
        `
    }
    
    let elementosCards = document.querySelectorAll(".card")
    for(let card of elementosCards){
        card.addEventListener("click",cliquei)
    }
   
}
busca()

function cliquei(){
    let elementoId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?id=" + elementoId
}
//inserir uma imagem como plano de fundo 

const meuElemento = document.getElementById("meu-elemento");
meuElemento.style.backgroundImage = "url('https://img.freepik.com/fotos-gratis/armazem-moderno-banhado-pelo-brilho-do-sol-ao-por-do-sol_91128-4583.jpg')"
*/