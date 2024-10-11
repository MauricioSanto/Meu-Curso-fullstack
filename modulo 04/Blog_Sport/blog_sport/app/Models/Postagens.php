<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Postagens extends Model
{
    use HasFactory;
    protected $fillable = ['user_id','titulo', 'conteudo' , 'data_postagem','foto'];
    public function users()
    {
        return $this->belongsTo (User::class);

    }
}






