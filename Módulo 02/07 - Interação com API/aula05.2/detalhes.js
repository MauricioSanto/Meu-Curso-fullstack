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

    document.getElementById("detalhes").innerHTML += `
    <h3>${produtos[inprod].nome}</h3>
    <p> condições especiais de parcelamento pra você entre em contato 
    conosco através dos nossos canais: instagram, facebook e whatsApp
    </p>
    <div class="img-vd">
        <img src="${produtos[inprod].img[0]}" id="img-frame" height= "280px" width= "435px" style= "border:1px solid #000; border-radius:10px">
        <iframe width="435" height="280" src="${produtos[inprod].video}"
            title="YouTube video player" frameborder="0" 
            allow="accelerometer; autoplay; 
            clipboard-write; encrypted-media; 
            gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
        </iframe>
    </div>
    <div class="mini-img" id="mini-img">
    </div>
    <p> Descrição: ${produtos[inprod].Descrição}</p>
    <p>R$ ${produtos[inprod].Preço.toFixed(2).replace(".",",")}</p>
    <p>Ano: ${produtos[inprod].Ano}</p>
    <p>Km: ${produtos[inprod].Quilometragem}</p>
    
    `
   /* let video = document.createElement("video");
    video.src="https://youtu.be/iIbIBEKl7tc"
    video.autoplay = true;
    let videoconteiner = document.querySelector("#video-conteiner");
    videoconteiner.innerHTML = "";
    videoconteiner.appendChild(video);
    */
    let divmini = document.getElementById("mini-img")
    for ( let i of produtos[inprod].img){
        divmini.innerHTML += `<img src= "${i}" class="miniatura" height= "80" width= "100" style= "border:1px solid #000; border-radius:10px" >`
    }
    let minicards = document.querySelectorAll(".miniatura")
    for ( let card of minicards){
        card.addEventListener("mouseover",alteraImg)

    }
function alteraImg(){
    let frame = document.getElementById("img-frame")
    frame.src = this.getAttribute("src")
}

}

buscar()
let meuElemento = document.getElementById("corpo");
meuElemento.style.backgroundImage = "url('https://img.freepik.com/fotos-gratis/armazem-moderno-banhado-pelo-brilho-do-sol-ao-por-do-sol_91128-4583.jpg')"

/*function inserirImagem(url){
    const img = document.createElement("img");
    img.src = url;
    document.body.appendChild(img);
}
inserirImagem("https://i.pinimg.com/originals/cb/8a/56/cb8a56874b79f36066b8cf28e1393c5e.jpg")
*/