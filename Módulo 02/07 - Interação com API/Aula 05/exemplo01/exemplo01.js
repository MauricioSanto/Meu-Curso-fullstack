/*
let urlprodutos = "https://raw.githubusercontent.com/MauricioSanto/Meu-Curso-fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Aula%2005/exemplo01/listaprodutos.json"

async function busca(){
    let resposta = await fetch(urlprodutos)
    let item = await resposta.json()
    //console.log(item)
    for(let produto in item){
        document.body.innerHTML += `
        <div class="texto">
            <div class= "secador">
                <img src= "${item[produto].img}"
                alt= "nao renderizou"
                width= "280"
                heigth= "280"
                >
                <p> ${item[produto].nome} </p>
                <p> ${item[produto].descrição} </p>
                <p class="maior">R$ ${item[produto].valorSemDesconto}</p>
                <p> R$ ${item[produto].valorComDesconto}</p>
            </div>
        </div>
        `
    }
  }
  busca()
*/

async function busca(){
    let procura = await fetch("listaprodutos.json")
    let produtos = await procura.json()
    //console.log(produtos)
    let listdiv = document.getElementById("lista-card")
    for(let item of produtos){
        listdiv.innerHTML += `
            <div class="card" data-id="${item.id}">
                <div class="grupo-img">
                    <img src="${item.img}" width="200" height="auto">
                </div>
                <div class="textos">
                    <h3>${item.nome}</h3>
                    <p>${item.descrição}</p>
                    <div>
                        <span>De</span> <span class="maior">R$ ${(item.valorSemDesconto).toFixed(2).replace(".",",")}</span>
                        <span class="comDesconto">Por R$ ${(item.valorComDesconto).toFixed(2).replace(".",",")}</span>
                    </div>
                </div>
            </div>
        `
    }
    let elementoscard = document.querySelectorAll(".card")
    for(let cards of elementoscard){
        cards.addEventListener("click",clicou)

    }

}
busca()

function clicou(){
    let itemId = this.getAttribute("data-id")
    //alert("card"+ itemId)
    window.location.href = "detalhes.html?ID=" + itemId
}

