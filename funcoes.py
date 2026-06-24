from ranking import adicionar_ao_ranking #ITA 23/06 - importação da função existente adicionar_ao_ranking

def exibir_menu():
    """Exibe o menu inicial para o usuário
    e recebe a opção que ele escolher."""

    print("\n" + "=" * 40)
    print("     BEM VINDO AO QUIZ!")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Ver ranking")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

def fazer_pergunta(pergunta):
    """Mostra o enunciado da pergunta, recebe a resposta
    e retorna se é True ou False."""
    
    print(pergunta["enunciado"])

    for alternativa in pergunta["opcoes"]:
        print(alternativa)
    
    while True:
        resposta = input("Sua resposta (A, B, C ou D): ").upper()
        if resposta in ["A", "B", "C", "D"]:
            break
        print("Resposta Inválida. Digite A, B, C ou D.") 

    if resposta == pergunta["resposta"]:
        print("✅ | Parabéns, você acertou!")
        return True
    else:
        print("❌ | Que pena, você errou!")
        print(f"Resposta correta: {pergunta['resposta']}")
        return False

# ITA 23/06 - Criada a função de desempenho do jogador de acordo com a sua pontuação.
def classificar_desempenho(acertos):
    if acertos == 10:
        return "Desempenho: Perfeito! Você é um gênio!"
    elif acertos >= 8:
        return "Desempenho: Excelente desempenho!"
    elif acertos >= 6:
        return "Desempenho: Bom trabalho!"
    elif acertos >= 4:
        return "Desempenho: Você pode melhorar!"
    else:
        return "Desempenho: Continue estudando!"
    

# ITA 23/06 - Criada a função que controla a partida.
def jogar(perguntas, ranking):
    
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

    # Chamando a função de classificação de desempenho criada anteriormente
    mensagem = classificar_desempenho(acertos)
    print(mensagem)

    # Adiciona o jogador atual ao ranking recebido e guarda o resultado
    ranking_atualizado = adicionar_ao_ranking(ranking, nome, acertos)    
    return ranking_atualizado