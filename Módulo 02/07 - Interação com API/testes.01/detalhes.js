async function buscar(){
    let procura = await fetch ("arranjosOrnamentais.json")
    let produtos = await procura.json()

    let buscaparametros = new URLSearchParams(window.location.search)
    let idproduto = buscaparametros.get("id")

    let prods = null
    for (let x in produtos){
        if(produtos[x].id == idproduto){
            prods = x
        }
    }
    document.title = produtos[prods].nome //para mudar o nome do titulo de acordo com o produto clicado.

    document.body.innerHTML += `
    <div class="cards">
        <img src="${produtos[prods].img}" height=280 widht=auto style= "border:1px solid #000; border-radius:10px">
        <h3>${produtos[prods].nome}</h3>
        <P>${produtos[prods].descricao}</p>
        <p> Valor R$ ${(produtos[prods].valor).toFixed(2).replace(".",",")}</P>
    </div>
    `
}
buscar()
let meuElemento = document.getElementById("canuto");
meuElemento.style.backgroundImage = "url('https://4.bp.blogspot.com/-3Y4u4ul_SeI/XEfopP7Oi6I/AAAAAAAAV5k/bTnGqJzpEgUUrHYFgzKzEzQTd2n4Ug7FACLcBGAs/s2560/landscape-2880x1800-lake-sunny-day-spain-4k-17123.jpg')"
