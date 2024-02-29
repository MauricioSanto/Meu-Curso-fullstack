async function buscar(){
    let procura = await fetch ("carrosImpor.json")
    let produtos = await procura.json()

    let buscaparametros = new URLSearchParams(window.location.search)
    
    let idproduto = buscaparametros.get("id")

    let inprod = null
    for (let x in produtos){
        if(produtos[x].id == idproduto){
            inprod = x
        }
    }
    document.body.innerHTML = `
    <h3>${produtos[inprod].nome}</h3>
    <p> condições especiais de parcelamento pra você entre em contato 
    conosco através dos nossos canais: instagram, facebook e whatsApp</p>
    
    `

}

buscar()
/*function inserirImagem(url){
    const img = document.createElement("img");
    img.src = url;
    document.body.appendChild(img);
}
inserirImagem("https://i.pinimg.com/originals/cb/8a/56/cb8a56874b79f36066b8cf28e1393c5e.jpg")
*/