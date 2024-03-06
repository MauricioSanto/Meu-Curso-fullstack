
async function busca(){
    let procura = await fetch("carrosImpor.json")
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
                    <p>${item.Descrição}</p>
                    <div>
                        <p> Valor R$: ${item.Preço}</p>
                        <p> Ano: ${item.Ano}</p>
                        <p> Km : ${item.Quilometragem}</p>

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




