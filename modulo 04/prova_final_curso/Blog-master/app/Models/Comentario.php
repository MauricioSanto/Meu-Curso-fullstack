<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comentario extends Model
{
    use HasFactory;
    protected $fillable = ['conteudo','user_id','publicacao_id'];
    public function users()
    {
        return $this->hasMany (User::class);

    }
    public function publicacaos()
    {
        return $this->hasMany (Publicacao::class);

    }
}
