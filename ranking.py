
def adicionar_ao_ranking(ranking, nome, pontuacao):
    """Adiciona o jogador e a pontuação ao ranking"""
    jogador = {"nome": nome, "pontuacao": pontuacao}
    ranking.append(jogador)
    return ranking

def exibir_ranking(ranking):
    """Exibe o ranking ordenado por pontuação do maior para menor."""
    print("\n" + "=" * 40)
    print("         RANKING DE JOGADORES")
    print("=" * 40)

    if not ranking:
        print("O ranking está vazio. Jogue uma partida!")
        return False
    
    ranking_ordenado = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)

    for posicao, jogador in enumerate(ranking_ordenado, start=1):
        print(f"{posicao}º - {jogador['nome']} - {jogador['pontuacao']} pontos")

    return True
