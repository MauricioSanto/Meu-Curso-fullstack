<!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cadastro de Postagens</title>
    </head>
    <body>
        <h1>Nova Postagem</h1>

        <form action="{{ route('postagem.store') }}" method="POST">
            @csrf
            <label>Titúlo:</label>
            <input type="text" name="titulo">
            <label>Conteudo:</label>
            <textarea name="conteudo"></textarea>
            <label>Data Postagem:</label>
            <input type="date" name="data_postagem">
            <button type="submit">Salvar</button>
        </form>
    </body>
</html>