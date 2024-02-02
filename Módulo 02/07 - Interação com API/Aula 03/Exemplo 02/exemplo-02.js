async function broca(){
    let parafuso = await fetch("pescaria.txt")
    let convertido = await parafuso.text()
    console.log(convertido)
}
broca()