async function verDateBase(){
    let procurar= await fetch("listaprodutos.json")
    let produtos = await procurar.json()

    let buscar = new URLSearchParams(window.location.search)
    let idproduto = buscar.get("id")

    let inprod = null
    for (let x in produtos){
        if(produtos[x].id == idproduto){
            inprod = x
        }
    }
    document.body.innerHTML = `
    <h3>${produtos[inprod].nome}</h3>
    `

}
verDateBase()