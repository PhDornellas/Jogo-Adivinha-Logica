import random
import json

arquivo = 'ranking.json'  

def carregar_ranking():
    
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_ranking(ranking):
    
    with open(arquivo, 'w') as file:
        json.dump(ranking, file, indent=4)

def exibir_ranking():
    
    ranking = carregar_ranking()
    if ranking:
        print("\nRanking de Jogadores:")
        for posicao, jogador in enumerate(sorted(ranking, key=lambda x: x['pontuacao'], reverse=True), start=1):
            print(f"{posicao}. {jogador['nome']} - Pontuação: {jogador['pontuacao']}")
    else:
        print("Ainda não há jogadores no ranking.")

def pergunta_Silogismo_falácia():
    print("Leia as frases e analise o que cada uma delas e diga se é Silogismo[S] ou falácia[F] \n")

    perguntas = [
        ("Nenhum livro pensa. 'A Odisséia' é um livro. Conclusão: 'A Odisséia' não pensa.", 'S'),
        ("Sempre que João leva seu guarda-chuva, não chove. Hoje, João não levará seu guarda-chuva. CONCLUSÃO: Portanto, hoje vai chover.", 'F'),
        ("Se todos os seres conscientes buscam propósito, então todos os humanos buscam sentido na vida.Todos os humanos são seres conscientes. CONCLUSÃO : Logo, todos os humanos buscam sentido na vida.", 'S'),
        ("Todo aluno estuda. Maria estuda. Conclusão: Maria é aluna.", 'F'),
        ("Nenhuma fruta é carne. A maçã é uma fruta. Conclusão: A maçã não é carne.", 'S'),
        ("Todos os matemáticos são bons em números. João é bom em números. Conclusão: João é matemático.", 'F'),
        ("Todo computador processa dados. Esse laptop é um computador. Conclusão: Esse laptop processa dados.", 'S'),
        ("Nenhum pássaro é mamífero. João não é pássaro. Conclusão: João é mamífero.", 'F'),
        ("Nenhum anfíbio é pássaro. A rã é um anfíbio. Conclusão: A rã não é um pássaro.", 'S'),
        ("Todo jogador de futebol corre. José corre. Conclusão: José é jogador de futebol.", 'F'),
        ("Todo círculo é redondo. Esse objeto é um círculo. Conclusão: Esse objeto é redondo.", 'S'),
        ("Todo peixe tem escamas. Esse animal tem escamas. Conclusão: Esse animal é um peixe.", 'F'),
        ("Nenhum réptil tem pelo. A cobra é um réptil. Conclusão: A cobra não tem pelo.", 'S'),
        ("Todo cientista é curioso. Marta é curiosa. Conclusão: Marta é cientista.", 'F'),
        ("Todos os professores ensinam. Marta é professora. Conclusão: Marta ensina.", 'S'),
        ("Nenhum músico é engenheiro. Pedro não é músico. Conclusão: Pedro é engenheiro.", 'F'),
        ("Todos os filósofos pensam sobre a existência. Sócrates é filósofo. Conclusão: Sócrates pensa sobre a existência.", 'S'),
        ("Todo médico usa jaleco. Pedro usa jaleco. Conclusão: Pedro é médico.", 'F'),
        ("Nenhum ser que tem asas é incapaz de voar sem ajuda. Os morcegos são seres que não possuem asas. Conclusão: Os morcegos são capazes de voar sem ajuda.", 'S'),
        ("Cada célula do corpo humano é invisível a olho nu. O corpo humano é composto por essas células. CONCLUSÃO: Portanto, o corpo humano é invisível a olho nu.", 'F')
    ]

    cont_S = 0
    cont_F = 0
    cont_errado = 0

    random.shuffle(perguntas)

    for pergunta, resp_correta in perguntas:
        resp = input(pergunta + "(Silogismo [S] ou Falácia [F]): ").strip().upper()
        if resp == resp_correta:
            if resp == 'S':
                cont_S += 1
            else:
                cont_F += 1
        else:
            cont_errado += 1

    
    print("\nResultados:")
    print("Silogismos corretos:", cont_S)
    print("Falácias corretas:", cont_F)
    print("Respostas incorretas:", cont_errado)

    
    nome_jogador = input("\nDigite seu nome para salvar no ranking: ")
    pontuacao = cont_S + cont_F  

    novo_jogador = {"nome": nome_jogador, "pontuação": pontuacao}
    ranking = carregar_ranking()
    ranking.append(novo_jogador)
    salvar_ranking(ranking)

    print(f"Pontuação de {nome_jogador} salva com sucesso!")

def main():
    while True:
        print("\n1. Jogar")
        print("2. Ver Ranking")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pergunta_Silogismo_falácia()
        elif opcao == '2':
            exibir_ranking()
        elif opcao == '3':
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
