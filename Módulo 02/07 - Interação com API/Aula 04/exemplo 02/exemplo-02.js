let urlProdutos = "https://raw.githubusercontent.com/MauricioSanto/Meu-Curso-fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Consumir%20API/produtos.json"

async function procurar(){
    let resposta = await fetch(urlProdutos)
    let produtos = await resposta.json()
    console.log(produtos)
    for(let produto in produtos){
        //document.body.innerHTML += "<h1 class= 'titulo'>" +produtos[produto].nome + "</h1>"
        document.body.innerHTML += `
        <div class="texto">
            <div class= "secador">
                <img src= "${produtos[produto].img}"
                alt= "nao renderizou"
                width= "280"
                heigth= "280"
                >
                <p> ${produtos[produto].nome} </p>
                <p>${produtos[produto].descricao}</p>
                <div class="valores">
                    <span>R$ ${produtos[produto].valorComDesconto}</span>
                    <span class="menor">R$ ${produtos[produto].valorSemDesconto}</span>
                </div>
                <p>${produtos[produto].tipoEntrega}</p>
                
            </div>
        </div>
        `
    }
}

procurar()