from perguntas import perguntas
from funcoes import *
from ranking import *

ranking_geral = []

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
        print(f"         RESULTADO DE {nome}")
        print("=" * 40)
        print(f"Acertos: {acertos} de {len(perguntas)}")
        print("=" * 40)

        if acertos == 10:
            print("Desempenho: Perfeito! Você é um gênio!")
        elif acertos >= 8:
            print("Desempenho: Excelente desempenho!")
        elif acertos >= 6:
            print("Desempenho: Bom trabalho!")
        elif acertos >= 4:
            print("Desempenho: Você pode melhorar!")
        else:
            print("Desempenho: Continue estudando!")

        ranking_geral = adicionar_ao_ranking(ranking_geral, nome, acertos)    

    elif opcao == "2":
        exibir_ranking(ranking_geral)
    
    elif opcao == "3":
        print("\n😄 | Obrigado por jogado! Até a próxima.")
        break

    else:
        print("Opção inválida! Digite apenas 1, 2  ou 3.")
        
