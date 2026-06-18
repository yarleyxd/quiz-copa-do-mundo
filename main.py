
while True:
    print("\n" + "=" * 40)
    print("     BEM VINDO AO QUIZ!")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")

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
            print(pergunta["enunciado"])
            for alternativa in pergunta["opcoes"]:
                print(alternativa)

            while True:
                resposta = input("Sua Resposta (A,B,C ou D):").upper()

                if resposta in ["A", "B", "C", "D"]:
                    break
                print("Resposta Inválida. Digite uma opção (A,B,C ou D).")

            if resposta == pergunta["resposta"]:
                print("✅ | Parabéns, você acertou!")
                acertos += 1
            else:
                print("❌ | Que pena, você errou!")
                
                print(f"Resposta correta: {pergunta['resposta']}")
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
