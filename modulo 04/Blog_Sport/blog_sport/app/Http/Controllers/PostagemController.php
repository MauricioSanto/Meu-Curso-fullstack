<?php

namespace App\Http\Controllers;

use App\Models\Postagens;
use App\Models\User;
use Illuminate\Http\Request;

class PostagemController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $postagens = Postagens::with('User','Avalicao','Comnetario')->get();
        $users = User::all();
        
        return view('postagem.index', compact('postagens','users'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('postagens.create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $request->validate([
            'titulo' => 'required',
            'data_postagem'=>'date',
            'conteudo'=>'text',
            'foto' => 'required|image|mimes:jpeg,png,jpg,gif|max:2048',
            
        ]);

        Postagens::create($request->all());
        return redirect()->route('postagem.index')->with('success', 'Postagem criada com sucesso.');
    
    }

    /**
     * Display the specified resource.
     */
    public function show(Postagens $postagens)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit($id)
    {
        $postagem = Postagens::find($id);
        return view('postagens.editar',compact('postagens'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, $id)
    {
        $request->validate([
            'titulo' => 'required',
            'data_postagem'=>'date',
            'conteudo'=>'text',
            'foto' => 'required|image|mimes:jpeg,png,jpg,gif|max:2048',
           
        ]);
        $postagem = Postagens::find($id);
        $foto_camimho = $request->file('foto')->store('fotos', 'public');
        
        $postagem->titulo =  $request->titulo;
        $postagem->data_postagem = $request->data_postagem;
        $postagem->foto = $foto_camimho;
        $postagem->conteudo= $request->conteudo;
        $postagem->save();

        return redirect()->route('postagem.index')->with('success', 'Postagem atualizada com sucesso.');

    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy($id)
    {
        $postagem = Postagens::find($id);
        $postagem->delete();
        return redirect()->route('postagem.index')->with('success', 'Postagem removida com sucesso.');
    
    }
}
