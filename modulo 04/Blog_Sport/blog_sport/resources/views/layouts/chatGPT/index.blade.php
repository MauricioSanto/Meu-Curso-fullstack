<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sabor do Brasil</title>
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            display: flex;
            height: 100vh;
        }
        .column {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
        }
        .column img {
            max-width: 100%;
            border-radius: 50%;
        }
        .cards {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .card {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
<div class="container">
    <!-- Coluna 1: Foto da Empresa/Usuário -->
    <div class="column" id="user-photo">
        @guest
            <img src="{{ asset('images/empresa.jpg') }}" alt="Sabor do Brasil">
        @else
            <img src="{{ asset('storage/'.auth()->user()->photo) }}" alt="{{ auth()->user()->name }}">
        @endguest
    </div>

    <!-- Coluna 2: Cards dos Pratos -->
    <div class="column cards">
        @foreach ($dishes as $dish)
            <div class="card">
                <img src="{{ asset('storage/'.$dish->image) }}" alt="{{ $dish->name }}">
                <h2>{{ $dish->name }}</h2>
                <div class="actions">
                    <button class="btn btn-primary">Like</button>
                    <button class="btn btn-danger">Dislike</button>
                    <button class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#commentModal-{{ $dish->id }}">Comentar</button>
                </div>
            </div>

            <!-- Modal para Comentários -->
            <div class="modal fade" id="commentModal-{{ $dish->id }}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Comentar em {{ $dish->name }}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form action="{{ route('comments.store') }}" method="POST">
                                @csrf
                                <textarea name="content" class="form-control" required></textarea>
                                <input type="hidden" name="dish_id" value="{{ $dish->id }}">
                                <button type="submit" class="btn btn-primary mt-3">Enviar</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        @endforeach
    </div>

    <!-- Coluna 3: Botão de Login -->
    <div class="column">
        @guest
            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#loginModal">Login</button>
        @else
            <a href="{{ route('logout') }}" class="btn btn-danger">Logout</a>
        @endguest
    </div>
</div>

<!-- Modal de Login -->
<div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="loginModalLabel">Login</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form action="{{ route('login') }}" method="POST">
                    @csrf
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" class="form-control" id="email" name="email" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Senha</label>
                        <input type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Entrar</button>
                </form>
            </div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
