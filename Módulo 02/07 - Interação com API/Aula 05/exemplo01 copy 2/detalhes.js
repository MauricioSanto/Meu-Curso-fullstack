async function procurar(){
    let buscar = await fetch("listaprodutos.json")
    let produtos = await buscar.json()

    let parametrosUrl = new URLSearchParams(window.location.search)
    let idproduto = parametrosUrl.get("pro-id")

    let indicePro = null
    for(let x in produtos){
        if (produtos[x].id == idproduto){
            indicePro = x
        }
    }
    document.body.innerHTML = `
    <h1>${produtos[indicePro].nome}</h1>
    `
}
procurar()