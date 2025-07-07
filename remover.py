from psycopg2 import Error
from juncao import *
from listar import *
from inserir import*

def remover_carona(conn, cur, id_carona):
    try:
        sql = "DELETE FROM carona WHERE id_carona = %s;" 
        cur.execute (sql, (id_carona,))
        conn.commit()
        print(f"Carona com o '{id_carona}' removido com sucesso!")
        
    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover carona {e}")

def remover_motoristas(conn, cur, id_motorista):
    try:
        sql = "DELETE FROM motoristas WHERE id_motorista = %s;"
        cur.execute(sql, (id_motorista,))
        conn.commit()
        print(f"Motorista com ID {id_motorista} removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover motorista: {e}")

def remover_pagamento(conn, cur, id_pagamento):
    try:
        sql = "DELETE FROM pagamento WHERE id_pagamento = %s;"
        cur.execute(sql, (id_pagamento,))
        conn.commit()
        print(f"O pagamento com ID {id_pagamento} removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover pagamento: {e}")

def remover_pagar(conn, cur, id_passageiro, id_pagamento):
    try:
        sql = "DELETE FROM pagar WHERE id_passageiro = %s AND id_pagamento = %s;"
        cur.execute(sql, (id_passageiro, id_pagamento))
        conn.commit()
        print(f"O registro de pagamento foi removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover o registro de pagamento: {e}")

def remover_passageiro(conn, cur, id_passageiro):
    try:
        sql = "DELETE FROM passageiros WHERE id_passageiro = %s;"
        cur.execute(sql, (id_passageiro,))
        conn.commit()
        print(f"Passageiro com ID {id_passageiro} removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover passageiro: {e}")

def remover_pedido(conn, cur, id_passageiro, id_carona):
    try:
        sql = "DELETE FROM pedido WHERE id_passageiro = %s AND id_carona = %s;"
        cur.execute(sql, (id_passageiro, id_carona))
        conn.commit()
        print(f"O pedido do passageiro {id_passageiro} para a carona {id_carona} foi removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover o pedido: {e}")

def remover_recebe(conn, cur, id_motorista, id_pagamento):
    try:
        sql = "DELETE FROM recebe WHERE id_motorista = %s AND id_pagamento = %s;"
        cur.execute(sql, (id_motorista, id_pagamento))
        conn.commit()
        print(f"O registro de recebimento do motorista {id_motorista} foi removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover o registro de recebimento: {e}")

def remover_veiculo(conn, cur, id_veiculo):
    try:
        sql = "DELETE FROM veiculos WHERE id_veiculo = %s;"
        cur.execute(sql, (id_veiculo,))
        conn.commit()
        print(f"Veiculo com ID {id_veiculo} removido com sucesso!")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao remover veiculo: {e}")

def menu_remover(conn, cur):
    opca2 = int(input("Escolha uma das opcoes: \n 1 - carona\n 2 - motoristas\n 3 - pagamento\n 4 - pagar\n 5 - passageiros\n 6 - pedido\n 7 - recebe\n 8 - veiculos \n"))
    
    match opca2:
        case 1: 
            #CARONA
            print("selecione uma das caronas abaixo: \n")
            carona = listar_caronas(cur)

            if not carona:
                print("Nao ha carona registrada. \n")
                return

            cabecalho = ["ID_CARONA", "ORIGEM", "DESTINO", "DISTANCIA_KM", "DURACAO_MINUTOS", "ID_MOTORISTA", "ID_VEICULO"]
            imprimir(cabecalho, carona)

            id = -1
            while(id == -1):
                id_carona = int(input("Digite o id da carona escolhida\n"))
                id = verificar_id(id_carona, carona, 0)
                if (id == -1):
                    print("O id do carona nao existe\n")

            remover_carona(conn, cur, id_carona)

        case 2:
            #MOTORISTAS
            print("Selecione um dos motoristas abaixo para a carona: \n")
            motoristas = listar_motoristas(cur)

            if not motoristas:
                print("Nao ha motoristas registrados. \n")
                return

            cabecalho = ["ID", "CNH", "Nome"]
            imprimir(cabecalho, motoristas)
            id_motorista = int(input("Digite o id do motorista escolhido: \n"))

            id = -1
            while(id == -1):
                id_motorista = int(input("Digite o id do motorista escolhido: \n"))
                id = verificar_id(id_motorista, motoristas, 0)
                if (id == -1):
                    print("O id do motorista nao existe\n")

            remover_motoristas(conn, cur, id_motorista)

        case 3:
            #PAGAMENTO
            print("Selecione um dos pagamentos abaixo: \n")
            pagamento = listar_pagamento(cur)

            if not pagamento:
                print("Nao ha pagamento registrados. \n")
                return

            cabecalho = ["ID_PAGAMENTO", "VALOR"]
            imprimir(cabecalho, pagamento)

            id = -1
            while(id == -1):
                id_pagamento = int(input("Digite o id do pagamento escolhido: \n"))
                id = verificar_id(id_pagamento, pagamento, 0)
                if (id == -1):
                    print("O id do pagamento nao existe\n")

            remover_pagamento(conn, cur, id_pagamento)

        case 4:
            #PAGAR
            print("Selecione O ID_PASSAGEIRO e o ID_PAGAMENTO da tupla a ser deletada: \n")
            pagar = juncao_pagar(cur)

            if not pagar:
                print("Nao ha pagar registrados. \n")
                return

            cabecalho = ["ID_PASSAGEIRO", "NOME", "ID_PAGAMENTO", "VALOR","DATA_HORA_PAGAR"]
            imprimir(cabecalho, pagar)
            id_passageiro = int(input("Digite o id do passageiro escolhido: \n"))
            id_pagamento = int(input("Digite o id do pagamento escolhido: \n"))

            remover_pagar(conn, cur, id_passageiro, id_pagamento)

        case 5:
            #PASSAGEIROS
            print("Selecione um passageiro listado abaixo: \n")
            passageiro =  listar_passageiros(cur)

            if not passageiro:
                print("Nao ha passageiro registrados. \n")
                return

            cabecalho = ["ID_PASSAGEIRO", "CPF", "NOME"]
            imprimir(cabecalho, passageiro)
            id_passageiro = int(input("Digite o id do passageiro escolhido"))

            id = -1
            while(id == -1):
                id_passageiro = int(input("Digite o id do passageiro escolhido: \n"))
                id = verificar_id(id_passageiro, passageiro, 0)
                if (id == -1):
                    print("O id do passageiro nao existe\n")

            remover_passageiro(conn, cur, id_passageiro)
        
        case 6:
            #PEDIDO
            print("Selecione O ID_PASSAGEIRO e o ID_CARONA da tupla a ser deletada: \n")
            pedido = juncao_registros_pedido(cur)

            if not pedido:
                print("Nao ha pedidos registrados. \n")
                return

            cabecalho = ["ID_PASSAGEIRO", "NOME_PASSAGEIRO", "ID_CARONA", "ORIGEM", "DESTINO", "DATA_HORA_PEDIDO"]
            imprimir(cabecalho, pedido)
            id_passageiro = int(input("Digite o id do passageiro escolhido: \n"))
            id_carona = int(input("Digite o id da carona escolhida: \n"))

            remover_pedido(conn, cur, id_passageiro, id_carona)

        case 7:
            #RECEBE
            print("Selecione O ID_MOTORISTA e o ID_PAGAMENTO da tupla a ser deletada: \n")
            recebe = juncao_recebe(cur)

            if not recebe:
                print("Nao ha registros de rebimento. \n")
                return

            cabecalho = ["ID_MOTORISTA", "NOME", "ID_PAGAMENTO", "VALOR","DATA_RECEBE"]
            imprimir(cabecalho, recebe)
            id_motorista = int(input("Digite o id do motorista escolhido: \n"))
            id_pagamento = int(input("Digite o id do pagamento escolhido: \n"))

            remover_recebe(conn, cur, id_motorista, id_pagamento)

        case 8:
            #VEICULOS
            print("Selecione um dos veiculos abaixo para a carona: \n")
            veiculos = listar_veiculos(cur)
            
            if not veiculos:
                print("Nao ha veiculos registrados. \n")
                return

            cabecalho = ["id_veiculo", "modelo", "placa", "ano", "cor", "capacidade_passageiro"]
            imprimir(cabecalho, veiculos)
            id_veiculo = int(input("Digite o id do veiculo escolhido: \n"))

            id = -1
            while(id == -1):
                id_veiculo = int(input("Digite o id do veiculo escolhido: \n"))
                id = verificar_id(id_veiculo, veiculos, 0)
                if (id == -1):
                    print("O id do veiculo nao existe\n")

            remover_veiculo(conn, cur, id_veiculo)

        case _: print("opcao invalida\n")
