<!DOCTYPE html>
<html>
    <head>
        <title>Lista de Postagens</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    </head>
    <body>
     
        <div class="container">
            <div class="row align-items-start">
                <div class="col">
                    Uma de três colunas
                </div>
                <div class="col">
                    <div>
                        @foreach ($postagens as $postagem)
                            <div class="col"> 

                                <div class="card" style="width: 18rem;">
                                    <img class="card-img-top" src="{{ asset('storage/' . $postagem->foto) }}" alt="Imagem de capa do card">
                                    <div class="card-body">
                                        <h5 class="card-title">{{ $postagem->titulo }}</h5>
                                        <p class="card-text">{{ $postagem->conteudo }}</p>
                                        <a href="#" class="btn btn-primary">Visitar</a>
                                    </div>
                                </div>
                                                    
                            </div> 
                        @endforeach
                    </div>
                    
                </div>
                <div class="col">
                    Uma de três colunas
                </div>
            </div>
        </div>
           
    </body>
</html>


