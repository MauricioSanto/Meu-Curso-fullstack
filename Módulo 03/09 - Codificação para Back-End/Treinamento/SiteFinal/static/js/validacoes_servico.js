$(document).ready(function(){
    
    $('#form_servico').submit(function(event){
        let tipo = $('#id_servico').val()
        if(tipo ==''){
            alert('tipo Obrigatório!')
            event.preventDefault();
        }
    });
});