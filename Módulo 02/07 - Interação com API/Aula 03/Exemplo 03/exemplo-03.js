async function fabrica(arquivo,id){
    let carros = await fetch(arquivo)
    let modelo = await carros.text()
    document.getElementById(id).textContent = (modelo)
}
fabrica("carro.txt","f1")
fabrica("flores.txt","f2")
 /*
async function vasos(){
    let florista = await fetch ("flores.txt")
    let mudas = await florista.text()
    document.getElementById("f2").textContent = (mudas)
}
vasos()
*/