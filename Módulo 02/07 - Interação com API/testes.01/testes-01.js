async function procurar(){
    let buscar = await fetch ("arranjosOrnamentais.json")
    let flores = await buscar.json()

    let divCards = document.getElementById("lista-div")
    for (let produtos of flores){
        divCards.innerHTML += `
           <div class="card" data-id="${produtos.id}">
                <div class= "imagem">
                    <img src="${produtos.img}" width= "250px" height="200px">
                </div>
                <h3>${produtos.nome}</h3>
                <p>${produtos.descricao}</p>
                <p> Valor R$ ${(produtos.valor).toFixed(2).replace('.',',')}</p>
                
            </div>

        `  
    }
    let arranjosCards = document.querySelectorAll(".card")
    for(let cards of arranjosCards){
        cards.addEventListener("click",clicou)
    
    }
}
procurar()

function clicou(){
    let cardId = this.getAttribute("data-id")
    window.location.href = "detalhes.html?id=" + cardId
}
let meuElemento = document.getElementById("meu-elemento");
meuElemento.style.backgroundImage = "url('https://4.bp.blogspot.com/-3Y4u4ul_SeI/XEfopP7Oi6I/AAAAAAAAV5k/bTnGqJzpEgUUrHYFgzKzEzQTd2n4Ug7FACLcBGAs/s2560/landscape-2880x1800-lake-sunny-day-spain-4k-17123.jpg')"
