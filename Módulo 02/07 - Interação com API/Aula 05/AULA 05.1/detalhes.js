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
    document.title = produtos[inprod].nome //para mudar o nome do titulo de acordo com o produto clicado.

    document.body.innerHTML = `
    <h3>${produtos[inprod].nome}</h3>
    <p> condições especiais de parcelamento pra você entre em contato 
    conosco através dos nossos canais: instagram, facebook e whatsApp</p>
    <img src="${produtos[inprod].img}" height=280 widht=auto style= "border:1px solid #000; border-radius:10px">
    <p> Descrição: ${produtos[inprod].Descrição}</p>
    <p>R$ ${produtos[inprod].Preço.toFixed(2).replace(".",",")}</p>
    <p>Ano: ${produtos[inprod].Ano}</p>
    <p>Km: ${produtos[inprod].Quilometragem}</p>
        
    
    `

}

buscar()
const meuElemento = document.getElementById("corpo");
meuElemento.style.backgroundImage = "url('https://img.freepik.com/fotos-gratis/armazem-moderno-banhado-pelo-brilho-do-sol-ao-por-do-sol_91128-4583.jpg')"

/*function inserirImagem(url){
    const img = document.createElement("img");
    img.src = url;
    document.body.appendChild(img);
}
inserirImagem("https://i.pinimg.com/originals/cb/8a/56/cb8a56874b79f36066b8cf28e1393c5e.jpg")
*/