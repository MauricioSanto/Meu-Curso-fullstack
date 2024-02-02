algoritmo "Estrutura SE"

var x: logico
    

inicio
    x <- falso
    escreval("Deseja que seu pedido seja entregue? 0 para Não e 1 para Sim")
    leia(x)
    escreval(x)

    se x = falso faca
        escreva("O usuário optou pela não entrega")
    fimse

    se x = verdadeiro faca
        escreva("O usuário optou pela entrega")
    fimse

fimalgoritmo