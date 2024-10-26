<?php

namespace App\Http\Controllers;

use App\Models\Publicacao;
use App\Models\Avaliacao;
use App\Models\User;
use Illuminate\Http\Request;

class PublicacaoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $publicacoes = Publicacao::with('empresa','comentario','avaliacao')->get();
        $avaliacoes = Avaliacao::all();
        $users = User::all();

        $quantidade_like = 0;
        $quantidade_deslike = 0;

        foreach($avaliacoes as $avaliacao){
            
            if($avaliacao->like){
                $quantidade_like = $quantidade_like + $avaliacao->like;
            }

            if($avaliacao->deslike){
                $quantidade_deslike = $quantidade_deslike + $avaliacao->deslike;
            }
        
        }

        return view('publicacao.index', compact('publicacoes','users','avaliacoes','quantidade_like','quantidade_deslike'));
    }
    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Publicacao $publicacao)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Publicacao $publicacao)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Publicacao $publicacao)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Publicacao $publicacao)
    {
        //
    }
}
