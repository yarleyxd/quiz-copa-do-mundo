from perguntas import perguntas
from funcoes import *

while True:
    opcao = exibir_menu() 
    
    if opcao == "1":
        while True:
            nome = input("Digite seu nome: ")
            
            if len(nome) >= 2:
                break
            print("Nome inválido! Digite pelo menos 2 caractéres.")

        acertos = 0
        print(f"\nBoa sorte, {nome}!")

        for numero, pergunta in enumerate(perguntas, start = 1):
            print(f"\nQuestão {numero}")

            if fazer_pergunta(pergunta):
                acertos += 1

        print("\n" + "=" * 40)
        print(f"Jogador: {nome}")
        print(f"Acertos: {acertos} de {len(perguntas)}")
        print("=" * 40)

        continue 

    elif opcao == "2":
        print("\n😄 | Obrigado por jogado! Até a próxima.")
        break

    else:
        print("Opção inválida! Digite apenas 1 ou 2.")
        
