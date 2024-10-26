<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comentario extends Model
{
    use HasFactory;
    protected $fillable = ['conteudo','user_id','publicacao_id'];
    public function user()
    {
        return $this->belongsTo(User::class);

    }
    public function publicacao()
    {
        return $this->belongsTo (Publicacao::class);

    }
}
