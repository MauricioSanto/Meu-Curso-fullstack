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
                <p> ${item[produto].valorSemDesconto}</p>
                <p> ${item[produto].valorComDesconto}</p>
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
    for(let item in produtos){
        listdiv.innerHTML += `<h1>${produtos[item].nome}</h1>`
    }

}
busca()
