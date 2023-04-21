#   2) Desenvolva um programa para verificar se a palavra 'Python' está presente na variável mensagem a seguir.
#   mensagem = "Hello Python world!"

mensagem = "Hello Python world!"

palavra = "Python"

mensagem_contem_palavra = palavra in mensagem

if (mensagem_contem_palavra):
    print("A mensagem contém a palavra Python")
else:
    print("A mensagem não contém a palavra Python")