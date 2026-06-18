perguntas = [
{
    "enunciado": "Qual país venceu a primeira copa do mundo em 1930?",
    "opcoes": ["A) Brasil", "B) Uruguai", "C) Argentina", "D) Itália"],
    "resposta": "B"
},
{
    "enunciado": "Qual a seleção que possui mais títulos da Copa do Mundo?",
    "opcoes": ["A) Alemanha", "B) Itália", "C) Brasil", "D) Argentina"],
    "resposta": "C"
},
{
    "enunciado": "Em que país foi realizada a Copa do Mundo de 2014?",
    "opcoes": ["A) Alemanha", "B) África do Sul", "C) Rússia", "D) Brasil"],
    "resposta": "D"
},
{
    "enunciado": "Quem foi o campeão da Copa do Mundo de 2022?",
    "opcoes": ["A) França", "B) Brasil", "C) Argentina", "D) Croácia"],
    "resposta": "C"
},
{
    "enunciado": "Quantos títulos mundiais o Brasil possui?",
    "opcoes": ["A) 4", "B) 5", "C) 6", "D) 7"],
    "resposta": "B"
},
{
    "enunciado": "Qual jogador é conhecido como 'Rei do Futebol'?",
    "opcoes": ["A) Maradona", "B) Pelé", "C) Messi", "D) Cristiano Ronaldo"],
    "resposta": "B"
},
{
    "enunciado": "A Copa do Mundo de 2026 será realizada em quantos países?",
    "opcoes": ["A) 1", "B) 2", "C) 3", "D) 4"],
    "resposta": "C"
},
{
    "enunciado": "8. Quem é o jogador que marcou o gol conhecido como 'A mão de Deus'?",
    "opcoes": ["A) Michael Platini", "B) Zico", "C) Gary Lineker", "D) Maradona"],
    "resposta": "D"
},
{
    "enunciado": "Quem marcou o gol do título da Alemanha na final da Copa de 2014?",
    "opcoes": ["A) Klose", "B) Neuer", "C) Kroos", "D) Götze"],
    "resposta": "D"
},
{
    "enunciado": "Que país sediou a Copa do Mundo de 2022?",
    "opcoes": ["A) Brasil", "B) Argentina", "C) Catar", "D) Emirados Árabes"],
    "resposta": "C"
}
]

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