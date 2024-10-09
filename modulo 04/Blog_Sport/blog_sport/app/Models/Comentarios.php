<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comentarios extends Model
{
    use HasFactory;
    protected $fillable = ['conteudo', 'data_comentario'];
    public function users()
    {
        return $this->belongsTo (User::class);

    }
    public function postagem()
    {
        return $this->belongsTo (Postagens::class);

    }
}
