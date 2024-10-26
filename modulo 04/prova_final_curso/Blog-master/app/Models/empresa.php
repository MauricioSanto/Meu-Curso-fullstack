<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Empresa extends Model
{
    use HasFactory;
    protected $fillable = ['nome','logo','publicacao_id'];
    
    public function publicacao()
    {
        return $this->hasMany (Publicacao::class);

    }
}
