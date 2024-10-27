import time

def erro_jogar_novamente():
    """Pergunta se o usuário deseja jogar novamente."""
    resposta = input("ANIMAL NÃO ENCONTRADO :( \nDeseja jogar novamente? [S/N] ").upper()
    if resposta == 'S':
        main()
    else:
        print("ENCERRANDO PROGRAMA...")
        time.sleep(2)
        print("PROGRAMA ENCERRADO")

def jogar_novamente():

    escolha = str(input("Deseja jogara novamente? ")).upper()

    if escolha == 'S':
        main()
    else:
        print("ENCERRANDO PROGRAMA...")
        time.sleep(2)
        print("PROGRAMA ENCERRADO")

def adivinhe_servivo():
    """Tenta adivinhar um ser vivo."""
    resposta = input("Esse ser vivo é um mamífero? [S/N] ").upper()
    if resposta == 'S':
        resposta = input("Esse mamífero é do mar? [S/N] ").upper()
        if resposta == 'S':
            resposta = input("É uma BALEIA? [S/N] ").upper()
            if resposta == 'S':
                print("Acertei!! O animal que você pensou foi uma BALEIA")
                jogar_novamente()
            else:
                resposta = input("É um GOLFINHO? [S/N] ").upper()
                if resposta == 'S':
                    print("Acertei!! O animal que você pensou foi um GOLFINHO")
                    jogar_novamente()
                else:
                    resposta = input("É um PEIXE-BOI? [S/N] ").upper()
                    if resposta == 'S':
                        print("Acertei!! O animal que você pensou foi um PEIXE-BOI")
                        jogar_novamente()
                    else:
                        erro_jogar_novamente()
        else:
            resposta = input("Esse mamífero é terrestre? [S/N] ").upper()
            if resposta == 'S':
                resposta = input("É um LEÃO? [S/N] ").upper()
                if resposta == 'S':
                    print("Acertei!! O animal que você pensou foi um LEÃO")
                    jogar_novamente()
                else:
                    resposta = input("É um CACHORRO? [S/N] ").upper()
                    if resposta == 'S':
                        print("Acertei!! O animal que você pensou foi um CACHORRO")
                        jogar_novamente()
                    else:
                        resposta = input("É um GATO? [S/N] ").upper()
                        if resposta == 'S':
                            print("Acertei!! O animal que você pensou foi um GATO")
                            jogar_novamente()
                        else:
                            # Adicione mais perguntas para mamíferos terrestres aqui.
                            erro_jogar_novamente()
            else:
                erro_jogar_novamente()
    elif resposta == 'N':
        # Perguntas para aves
        resposta = input("Esse ser vivo é uma ave? [S/N] ").upper()
        if resposta == 'S':
            resposta = input("É uma ARARA? [S/N] ").upper()
            if resposta == 'S':
                print("Acertei!! O animal que você pensou foi uma ARARA")
                jogar_novamente()
            else:
                resposta = input("É um URUBU? [S/N] ").upper()
                if resposta == 'S':
                    print("Acertei!! O animal que você pensou foi um URUBU")
                    jogar_novamente()
                else:
                    resposta = input("É um PAPAGAIO? [S/N] ").upper()
                    if resposta == 'S':
                        print("Acertei!! O animal que você pensou foi um PAPAGAIO")
                        jogar_novamente()
                    else:
                        resposta = input("É um PAVÃO? [S/N] ").upper()
                        if resposta == 'S':
                            print("Acertei!! O animal que você pensou foi um PAVÃO")
                            jogar_novamente()
                        else:
                            resposta = input("É um PINGUIM? [S/N] ").upper()
                            if resposta == 'S':
                                print("Acertei!! O animal que você pensou foi um PINGUIM")
                                jogar_novamente()
                            else:
                                erro_jogar_novamente()
        
        # Perguntas para répteis
        elif resposta == 'N':
            resposta = input("Esse ser vivo é um réptil? [S/N] ").upper()
            if resposta == 'S':
                resposta = input("É uma COBRA? [S/N] ").upper()
                if resposta == 'S':
                    print("Acertei!! O animal que você pensou foi uma COBRA")
                    jogar_novamente()
                else:
                    resposta = input("É uma TARTARUGA? [S/N] ").upper()
                    if resposta == 'S':
                        print("Acertei!! O animal que você pensou foi uma TARTARUGA")
                        jogar_novamente()
                    else:
                        resposta = input("É uma LAGARTIXA? [S/N] ").upper()
                        if resposta == 'S':
                            print("Acertei!! O animal que você pensou foi uma LAGARTIXA")
                            jogar_novamente()
                        else:
                            erro_jogar_novamente()

            # Perguntas para anfíbios
            elif resposta == 'N':
                resposta = input("Esse ser vivo é um anfíbio? [S/N] ").upper()
                if resposta == 'S':
                    resposta = input("É um SAPO? [S/N] ").upper()
                    if resposta == 'S':
                        print("Acertei!! O animal que você pensou foi um SAPO")
                        jogar_novamente()
                    else:
                        resposta = input("É uma RÃ? [S/N] ").upper()
                        if resposta == 'S':
                            print("Acertei!! O animal que você pensou foi uma RÃ")
                            jogar_novamente()
                        else:
                            erro_jogar_novamente()
                
                # Perguntas para peixes
                elif resposta == 'N':
                    resposta = input("Esse ser vivo é um peixe? [S/N] ").upper()
                    if resposta == 'S':
                        resposta = input("É uma BORBOLETA? [S/N] ").upper()
                        if resposta == 'S':
                            print("Acertei!! O animal que você pensou foi uma BORBOLETA")
                            jogar_novamente()
                        else:
                            resposta = input("É um MOSQUITO? [S/N] ").upper()
                            if resposta == 'S':
                                print("Acertei!! O animal que você pensou foi um MOSQUITO")
                                jogar_novamente()
                            else:
                                resposta = input("É um CAMARÃO? [S/N] ").upper()
                                if resposta == 'S':
                                    print("Acertei!! O animal que você pensou foi um CAMARÃO")
                                    jogar_novamente()
                                else:
                                    resposta = input("É uma ESPONJA? [S/N] ").upper()
                                    if resposta == 'S':
                                        print("Acertei!! O animal que você pensou foi uma ESPONJA")
                                        jogar_novamente()
                                    else:
                                        resposta = input("É uma ÁGUA-VIVA? [S/N] ").upper()
                                        if resposta == 'S':
                                            print("Acertei!! O animal que você pensou foi uma ÁGUA-VIVA")
                                            jogar_novamente()
                                        else:
                                            erro_jogar_novamente()
            else:
                erro_jogar_novamente()
    else:
        erro_jogar_novamente()



def adivinhe_fruta():
    print("FRUTA")



def adivinhe_objeto():
    print("OBJETO")

def main():
    """Função principal do jogo."""
    print("Pense em um animal, Fruta ou objeto!")
    time.sleep(3)

    opcao = str(input("Voce esta pesando em um ser vivo? ")).upper()

    if opcao == 'S':
        adivinhe_servivo()
    elif opcao == 'N':
        opcao = str(input("Voce esta pesando em uma fruta ?")).upper()
        if opcao == 'S':
            adivinhe_fruta()
        else:
            opcao = str(input("Então voce esta pensando em um objeto? ")).upper()
            if opcao == 'S':
                adivinhe_objeto()
            else:
                print("OPÇÃO INVALIDA!")
                jogar_novamente()

    

if __name__ == "__main__":
    main()
