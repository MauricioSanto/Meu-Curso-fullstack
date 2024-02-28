async function buscar(){
    let procura = await fetch ("listaprodutos.json")
    let produtos = await procura.json()

    let buscaparametros = new URLSearchParams(window.location.search)
}
buscar()