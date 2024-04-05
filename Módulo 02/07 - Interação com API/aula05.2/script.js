
async function busca(){
    let procura = await fetch("carrosImpor.json")
    let produtos = await procura.json()
    //console.log(produtos)
    let listdiv = document.getElementById("lista-card")
    for(let item of produtos){
        listdiv.innerHTML += `   
            <div class="card" data-id = "${item.id}">
                <div class="grupo-img">
                    <img src="${item.img[0]}" width="250" height="auto" >
                </div>
                <div class="textos">
                     <h3>${item.nome}</h3>
                    <p> Descrição: ${item.Descrição}</p>
                    <p> Valor R$ ${(item.Preço).toFixed(2).replace(".",",")}</p>
                    <p> Ano ${item.Ano}</P>
                    <p> KM ${item.Quilometragem}</p>
                        
                </div>
            </div>  
            
        `
    }
    
    let elementosCards = document.querySelectorAll(".lista-card")
    for(let card of elementosCards){
        card.addEventListener("click",cliquei)
    }
    /*
    document.addEventListener(".lista-card", function () {
        let carousel = document.querySelector(".carousel");
        let items = carousel.querySelectorAll(".item");
        let dotsContainer = document.querySelector(".dots");
      
        // Insert dots into the DOM
        items.forEach((_, index) => {
          let dot = document.createElement("span");
          dot.classList.add("dot");
          if (index === 0) dot.classList.add("active");
          dot.dataset.index = index;
          dotsContainer.appendChild(dot);
        });
      
        let dots = document.querySelectorAll(".dot");
      
        // Function to show a specific item
        function showItem(index) {
          items.forEach((item, idx) => {
            item.classList.remove("active");
            dots[idx].classList.remove("active");
            if (idx === index) {
              item.classList.add("active");
              dots[idx].classList.add("active");
            }
          });
        }
      
        // Event listeners for buttons
        document.querySelector(".prev").addEventListener("click", () => {
          let index = [...items].findIndex((item) =>
            item.classList.contains("active")
          );
          showItem((index - 1 + items.length) % items.length);
        });
      
        document.querySelector(".next").addEventListener("click", () => {
          let index = [...items].findIndex((item) =>
            item.classList.contains("active")
          );
          showItem((index + 1) % items.length);
        });
      
        // Event listeners for dots
        dots.forEach((dot) => {
          dot.addEventListener("click", () => {
            let index = parseInt(dot.dataset.index);
            showItem(index);
          });
        });
      });
      
  */

}
busca()

function cliquei(){
    let elementoId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?id=" + elementoId
}
//inserir uma imagem como plano de fundo 
let meuElemento = document.getElementById("meu-elemento");
meuElemento.style.backgroundImage = "url('https://img.freepik.com/fotos-gratis/armazem-moderno-banhado-pelo-brilho-do-sol-ao-por-do-sol_91128-4583.jpg')"








