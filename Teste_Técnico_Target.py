# 
# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?

# REPOSTA: 91 

#----------------------------------------------------------------------------------------------------------------------------------------

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
# valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem
# que desejar onde, informado um número, ele calcule 
# a sequência de Fibonacci e retorne uma mensagem avisando
# se o número informado pertence ou não a sequência.

#----------------------------------------------------------------------------------------------------------------------------------------

# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, _9_

# b) 2, 4, 8, 16, 32, 64, _128_

# c) 0, 1, 4, 9, 16, 25, 36, _49_

# d) 4, 16, 36, 64, _100_

# e) 1, 1, 2, 3, 5, 8, _13_

# f) 2,10, 12, 16, 17, 18, 19, _200_

#----------------------------------------------------------------------------------------------------------------------------------------

# 4) Você está em uma sala com três interruptores, 
# cada um conectado a uma lâmpada em uma sala diferente. 
# Você não pode ver as lâmpadas da sala em que está, 
# mas pode ligar e desligar os interruptores quantas vezes quiser. 
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, 
# qual interruptor controla cada lâmpada?

# RESPOSTA:
# Ligo um dos interruptores. Após, desligo e ligue um segundo interruptor. 
# Vá até a sala. A lâmpada desligada e quente corresponde ao primeiro interruptor, 
# a lâmpada acesa ao segundo e a lâmpada apagada e fria ao terceiro.

#Questao 5

def inverterStr(palavra):
    invertida = ""

    for i in palavra:
        invertida = invertida + i
    print(invertida)

inverterStr("Invertido")
