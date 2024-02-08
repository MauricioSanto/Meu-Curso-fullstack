/*
const nome = 'Maria';
const idade = 30;
const profissao = 'Designer';

const json2 = `{
  "nome": "${nome}",
  "idade": ${idade},
  "profissao": "${profissao}"
}`;

console.log(json)
*/
let urlpessoas = "https://raw.githubusercontent.com/MauricioSanto/Meu-Curso-fullstack/master/M%C3%B3dulo%2002/07%20-%20Intera%C3%A7%C3%A3o%20com%20API/Aula%2004/exemplo%2003/pessoas.json"

async function procurar(){
  let resposta = await fetch(urlpessoas)
  let humano = await resposta.json()
  console.log(humano)
  for(let vida in humano){
      document.body.innerHTML += `
      <div class="texto">
          <div class= "secador">
              <img src= "${humano[vida].img}"
              alt= "nao renderizou"
              width= "280"
              heigth= "280"
              >
              <p> ${humano[vida].nome} </p>
              <p>${humano[vida].idade} anos</p>
              <p> ${humano[vida].profissão}</p>
          </div>
      </div>
      `
  }
}

procurar()