async function buscar(){
    let buscaparametro = new URLSearchParams(window.location.search)
    let parametroid = buscaparametro.get("id")
    //alert(parametroid)
    let procura = await fetch("listaprodutos.json")
    let produtos = await procura.json()

    let indice = null
    for(let x in produtos){
        if(produtos[x].id == parametroid){
            indice = x
        }
    }
    alert(indice)
    document.body.innerHTML = `<h1>${produtos[indice].nome}</h1>
    `
}
buscar()