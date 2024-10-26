<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('publicacao', function (Blueprint $table) {
            $table->id();
            $table->string('foto');
            $table->string('titulo_prato');
            $table->string('local');
            $table->string('cidade');
            $table->unsignedBigInteger('empresa_id');
            $table->foreign('empresa_id')
                    ->references('id')
                    ->on('empresas')
                    ->onDelete('cascade');
            $table->unsignedBigInteger('comentario_id');
            $table->foreign('comentario_id')
                    ->references('id')
                    ->on('comentarios')
                    ->onDelete('cascade');
            $table->unsignedBigInteger('avaliacao_id');
            $table->foreign('avaliacao_id')
                    ->references('id')
                    ->on('avaliacoes')
                    ->onDelete('cascade');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('publicacaos');
    }
};
