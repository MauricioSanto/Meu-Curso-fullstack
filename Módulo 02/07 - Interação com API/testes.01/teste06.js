async function busca() {
  let procura = await fetch("carrosImpor.json");
  let produtos = await procura.json();
  let listdiv = document.getElementById("lista-card");
  
  for (let item of produtos) {
      let card = document.createElement('div');
      card.classList.add('card');
      card.dataset.id = item.id;
      card.innerHTML = `
          <div class="miniatura">
              <img src="${item.img[0]}" width="150" height="auto">
              <h3>${item.nome}</h3>
          </div>
          <div class="detalhes">
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
      `;
      listdiv.appendChild(card);
  }

  // Adiciona evento de clique para expandir
  let elementosCards = document.querySelectorAll(".card");
  elementosCards.forEach(card => {
      card.addEventListener("click", expandirCard);
  });
}

function expandirCard() {
  // Adiciona classe para expandir o card clicado
  this.classList.toggle("expandido");
}

busca();
