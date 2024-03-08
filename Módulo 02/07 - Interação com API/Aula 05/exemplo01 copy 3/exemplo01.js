
async function busca(){
    let procura = await fetch("arranjosOrnamentais.json")
    let produtos = await procura.json()
    //console.log(produtos)
    let listdiv = document.getElementById("lista-card")
    for(let item of produtos){
        listdiv.innerHTML += `
            <div class="card">
                <div class="grupo-img">
                    <img src="${item.img}" width="250" height="auto">
                </div>
                <div class="textos">
                    <h3>${item.nome}</h3>
                    <p>${item.descricao}</p>
                    <div>
                        <p> Valor R$: ${item.valor}</p>

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
    window.location.href = "detalhes/copy03.html?id=" + elementoId
}




