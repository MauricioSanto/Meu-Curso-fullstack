<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostagemController;


Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::get('/', [PostagemController::class, 'index'])->name('postagem.index');

Route::middleware('auth')->group(function () {
    
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
    Route::get('/postagem_salvar', [PostagemController::class, 'create'])->name('postagem.create');
    Route::get('/postagem/editar/{id}', [PostagemController::class, 'edit'])->name('postagem.edit');
    Route::post('/postagem', [PostagemController::class, 'store'])->name('postagem.store');
    Route::delete('/postagem/{id}', [PostagemController::class, 'destroy'])->name('postagem.destroy');
    Route::put('/postagem/{id}', [PostagemController::class, 'update'])->name('postagem.update');
    Route::get('/postagem/{id}',[PostagemController:: class,'show'])->name('postagem.show');

});

require __DIR__.'/auth.php';
