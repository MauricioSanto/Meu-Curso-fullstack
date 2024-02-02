algoritmo "Comando Escolha"

var x, y: inteiro
    operacao: caractere

inicio

    x <- 2
    y <- 3

    escreval ("Digite a Operação a ser efetuada (+, -, *, /):")
    leia (operacao)
    escreval (operacao)

    escolha operacao

        caso "+"
            escreval (x + y)

        caso "-"
            escreval (x - y)

        caso "*"
            escreval (x * y)

        caso "/"
            escreval (x / y)

        outrocaso
            escreval ("Operação Inválida")

    fimescolha

fimalgoritmo
