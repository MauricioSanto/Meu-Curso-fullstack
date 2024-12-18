<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Postagens extends Model
{
    use HasFactory;
    protected $fillable = ['user_id','titulo', 'conteudo' , 'data_postagem','foto','like_id'];

    public function user()
    {
        return $this->belongsTo (User::class);

    }
    public function likes()
    {
        return $this->hasMany(Like::class);
    }
}






