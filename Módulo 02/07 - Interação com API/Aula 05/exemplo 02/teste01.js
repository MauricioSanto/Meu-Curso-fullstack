async function vai(){
    let procura = await fetch("teste01.json")
    let produtos = await procura.json()
    console.log(produtos)
    let listdiv = document.getElementById("hcard")
    for(let item of produtos){
        listdiv.innerHTML += `
            <div class="card">
                
                <img src="${item.img}" width="200" height="auto">
                
                
                <h3>${item.nome}</h3>
                <p>${item.descrição}</p>
                    
                <span class="comDesconto"> R$ ${item.preçoComDesconto}</span>
                <span class="maior"> R$ ${item.preçoSemDesconto}</span>
                    
            
            </div>
        `
    }

}
vai()
