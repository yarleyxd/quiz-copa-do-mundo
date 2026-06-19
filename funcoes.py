def exibir_menu():
    """Exibe o menu inicial para o usuário
    e recebe a opção que ele escolher."""

    print("\n" + "=" * 40)
    print("     BEM VINDO AO QUIZ!")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Sair")

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
