from inserir import *
from listar import *
from tabulate import tabulate 
from remover import *
from juncao import *
from subconsultas import*

if __name__ == "__main__":
    conn, cur = criar_conexao()

    if conn:
 
        while True:

            opcao = int(input("Escolha uma das opcoes: \n 1 - Inserir uma tupla em uma tabela \n 2 - Remover uma tupla de uma tabela\n 3 - imprimir uma tabela\n 4 - mostrar juncao\n 5 - subconsultas\n 6 - sair\n"))

            match opcao:
                case 1:
                    menu_inserir(conn, cur)

                case 2:
                    menu_remover(conn, cur)

                case 3:
                    menu_listar(cur)

                case 4:
                    menu_juncao(cur)

                case 5:
                    menu_subconsultas(cur)
                
                case 6:
                    print(f"Programa encerrado\n")
                    break
                
                case _:
                    print(f"Opção inválida\n")