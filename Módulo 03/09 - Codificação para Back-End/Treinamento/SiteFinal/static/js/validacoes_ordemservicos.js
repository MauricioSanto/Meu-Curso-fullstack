(document).ready(function(){
    
    $('#form_oredmservicos').submit(function(event){
        let cliente = $('#id_ordemservicos').val()
        if(cliente ==''){
            alert('Cliente Obrigatório')
            event.preventDefault();
        }
    });
});