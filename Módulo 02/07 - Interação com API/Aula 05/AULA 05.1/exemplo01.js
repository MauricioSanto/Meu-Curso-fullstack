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
    let procura = await fetch("carrosImpor.json")
    let produtos = await procura.json()
    //console.log(produtos)
    let listdiv = document.getElementById("lista-card")
    for(let item of produtos){
        listdiv.innerHTML += `
            <div class="card" data-id = "${item.id}">
                <div class="grupo-img">
                    <img src="${item.img}" width="250" height="auto">
                </div>
                <div class="textos">
                    <h3>${item.nome}</h3>
                    <p> Descrição: ${item.Descrição}</p>
                    <div>
                       <p> Valor R$ ${(item.Preço).toFixed(2).replace(".",",")}</p>
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

/*inserir uma imagem no corpo da pagina ou body
function inserirImagem(url){
    const img = document.createElement("img");
    img.src = url;
    document.body.appendChild(img);
}
inserirImagem("https://i.pinimg.com/originals/cb/8a/56/cb8a56874b79f36066b8cf28e1393c5e.jpg")
*/




