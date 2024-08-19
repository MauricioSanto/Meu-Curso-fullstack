$(document).ready(function(){
    
    $('#form_produto').submit(function(event){
        let nome = $('#id_produto').val()
        if(nome ==''){
            alert('Nome Obrigatório!')
            event.preventDefault();
        }
    });
});