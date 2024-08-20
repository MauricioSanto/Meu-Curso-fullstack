$(document).ready(function(){
    
    $('#form_produto').submit(function(event){
        let nome = $('#nome').val()
        let valor = $('#valor').val()
        let descricao = $('#descricao').val()
        if(nome ==''){
            alert('Nome Obrigatório!')
            event.preventDefault();
        }
        if(valor ==''){
            alert('Valor Obrigatório!')
            event.preventDefault();
        }
        if(descricao ==''){
            alert('Descrição Obrigatório!')
            event.preventDefault();
        }
    });
});