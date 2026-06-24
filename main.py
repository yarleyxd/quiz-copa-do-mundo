from perguntas import perguntas
from funcoes import *
from ranking import *


ranking_geral = []

while True:
    opcao = exibir_menu() 
    
    if opcao == "1":
        # ITA 23/06 - removi a lógica da partida para função jogar .
        ranking_geral = jogar(perguntas, ranking_geral)    

    elif opcao == "2":
        exibir_ranking(ranking_geral)
    
    elif opcao == "3":
        print("\n😄 | Obrigado por ter jogado! Até a próxima.")
        break

    else:
        print("Opção inválida! Digite apenas 1, 2  ou 3.")
        
