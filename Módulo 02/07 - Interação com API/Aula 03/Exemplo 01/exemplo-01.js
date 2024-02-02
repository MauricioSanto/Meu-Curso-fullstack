
async function vaiPokemon(){
    let pokedex = await fetch("pokemon.txt")
    //console.log(pokedex)
    let vaiBola = await pokedex.text()
    //console.log(vaiBola)

    document.getElementById("teste").textContent = vaiBola
}

vaiPokemon()
