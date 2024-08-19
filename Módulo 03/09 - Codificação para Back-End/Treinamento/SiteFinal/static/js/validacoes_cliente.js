$(document).ready(function(){
    
    $('#form_cliente').submit(function(event){
        let nome = $('#id_cliente').val()
        if(nome ==''){
            alert('Nome Obrigatório')
            event.preventDefault();
        }
    });
});