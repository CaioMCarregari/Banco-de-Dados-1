import psycopg2
from psycopg2 import OperationalError, Error
from tabulate import tabulate 
import datetime
from listar import *
from juncao import*

def criar_conexao():
    try: 
        conn = psycopg2.connect(
            dbname="app",   
            user="postgres",     
            password="udesc",      
            host="localhost",    
            port="5432"   
        )
        cur = conn.cursor()
        return conn, cur
    except OperationalError as e:
        print(f"Erro ao tentar se conectar ao PostgreSQL: {e}")
        return None, None
    
def inserir_motorista(conn, cur,cnh, nome):
    
    try:
        sql = "INSERT INTO motoristas (cnh, nome) VALUES (%s, %s);"
        cur.execute(sql, (cnh, nome,))
        conn.commit()
        print(f"Motorista '{nome}' com CNH '{cnh}' inserido com sucesso!")
    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir motorista {e}")

def inserir_caronas(conn, cur, origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo):
    try: 
        sql = """INSERT INTO carona (origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo) 
        VALUES (%s, %s, %s, %s, %s, %s);"""

        cur.execute(sql, (origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo))

        conn.commit()
        print(f"Viagem de '{origem}' a '{destino} salva com sucesso! \n")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir viagem {e}")

def inserir_veiculos(conn, cur, modelo, placa, ano, cor, capacidade_passageiro, id_motorista):
    try:
        sql = """INSERT INTO veiculos (modelo, placa, ano, cor, capacidade_passageiro, id_motorista) 
        VALUES (%s, %s, %s, %s, %s, %s);"""

        cur.execute(sql, (modelo, placa, ano, cor, capacidade_passageiro, id_motorista),) 

        conn.commit()
        print(f"O veiculo '{modelo}' com a '{placa}' foi adicionado com sucesso \n")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir o veiculo {e}")

def inserir_passageiros(conn, cur, cpf, nome):
    try:
        sql = "INSERT INTO passageiros (cpf, nome) VALUES (%s, %s);"

        cur.execute(sql, (cpf, nome,))

        conn.commit()
        print(f"O passageiro '{nome}' com o '{cpf}' foi adicionado com sucesso \n")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inseir o passageiro {e}")

def inserir_pedido(conn, cur, id_passageiro, id_carona, data_hora_pedido):
    try:
        sql = "INSERT INTO pedido (id_passageiro, id_carona, data_hora_pedido) VALUES (%s, %s, %s);"

        cur.execute(sql, (id_passageiro, id_carona, data_hora_pedido))

        conn.commit()
        print(f"O pedido da carona '{id_carona}' feito pelo passageiro'{id_passageiro}' foi adicionado com sucesso \n")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir o pedido {e}")

def inserir_pagamento(conn, cur, valor):
    try:
        sql = "INSERT INTO pagamento (valor) VALUES (%s);"

        cur.execute (sql, (valor,))

        conn.commit()
        print(f"O pagamento no valor de '{valor}' foi registado")

    except Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir o pagamento {e}")

def inserir_pagar(conn, cur, id_passageiro, id_pagamento, data_hora_pagamento):
    try:
        sql = "INSERT INTO pagar (id_passageiro, id_pagamento, data_hora_pagamento) VALUES (%s, %s, %s);"

        cur.execute(sql, (id_passageiro, id_pagamento, data_hora_pagamento))

        conn.commit()
        print("O pagamento foi registrado")

    except Error as e: 
        if conn: 
            conn.rollback()
        print(f"Erro ao gerar o pagamento {e}")

def inserir_recebe(conn, cur, id_motorista, id_pagamento, data_recebe):
    try:
        sql = "INSERT INTO recebe (id_motorista, id_pagamento, data_recebe) VALUES (%s, %s, %s);"

        cur.execute(sql, (id_motorista, id_pagamento, data_recebe))

        conn.commit()
        print("O deposito foi registrado")

    except Error as e: 
        if conn: 
            conn.rollback()
        print(f"Erro ao gerar o deposito {e}")

def verificar_id(id_motorista, carona, num):
    for i in range (len(carona)):
        if (id_motorista == carona[i][0]):
            return carona[i][num]
    
    return -1


def menu_inserir (conn, cur):
     
    opca2 = int(input("Escolha uma das opcoes: \n 1 - carona\n 2 - motoristas\n 3 - pagamento\n 4 - pagar\n 5 - passageiros\n 6 - pedido\n 7 - recebe\n 8 - veiculos\n 9 - voltar\n"))
    
    match opca2:
        case 1:
            #CARONA
            origem = input("Digite a origem: \n")
            destino = input("Digite o destino: \n")
            distancia_km = float(input("Digite a distancia em km: \n"))
            duracao_minutos = int(input("Digite a duracao da viagem em mintos: \n"))
            carona =  juncao_veiculos_com_motoristas(cur)

            if not carona:  
                print("Nenhum motorista disponivel no momento.")

            else:
                print("Selecione um dos motoristas abaixo para a carona: \n")
                cabecalho = ["ID_MOTORISTA", "NOME_MOTORISTA", "ID_VEICULO", "MODELO", "PLACA", "ANO", "COR"]
                imprimir(cabecalho, carona)
                
                
                id_veiculo = -1
                while(id_veiculo == -1):
                    id_motorista = int(input("Digite o id do Motorista: \n"))
                    print("\n")
                    id_veiculo = int(verificar_id(id_motorista, carona, 2))
                    if (id_veiculo == -1):
                        print("Id do motorista nao valido\n")

                inserir_caronas(conn, cur, origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo)

        case 2:
            #MOTORISTAS
            cnh = input ("Digite a cnh do motorista (11 digitos): \n")

            nome = input("Digite o nome do motorista: \n")

            inserir_motorista(conn, cur, cnh, nome)

        case 3:
            #PAGAMENTO
            valor = float(input("Digite o valor da carona: \n"))
            inserir_pagamento(conn, cur, valor)

        case 4:
            #PAGAR
            passageiro =  listar_passageiros(cur)

            if not passageiro:
                print("Nao ha passageiros listados\n")
                return
            
            print("Selecione um passageiro listado abaixo: \n")
            cabecalho = ["ID_PASSAGEIRO", "CPF", "NOME"]
            imprimir(cabecalho, passageiro)
            
            id = -1
            while(id == -1):
                id_passageiro = int(input("Digite o id do passageiro escolhido\n"))
                id = verificar_id(id_passageiro, passageiro, 0)
                if (id == -1):
                    print("O id do passageiro nao existe\n")

            pagamento = listar_pagamentos_disponiveis(cur)

            if not pagamento:
                print("Nao ha pagamentos disponiveis listado\n")
                return
            
            print("Selecione um dos pagamentos abaixo: \n")
            cabecalho = ["ID_PAGAMENTO", "VALOR"]
            imprimir(cabecalho, pagamento)

            id = -1
            while(id == -1):
                id_pagamento = int(input("Digite o id do pagamento escolhido: \n"))
                id = verificar_id(id_pagamento, pagamento, 0)
                
                if (id == -1):
                    print("O id do pagamento nao existe\n")

            data_hora_pagamento = datetime.datetime.now()
            inserir_pagar(conn, cur, id_passageiro, id_pagamento, data_hora_pagamento)

        case 5:
            #PASSAGEIROS
            cpf = input ("Digite o cpf do passageiro a ser adicionado: \n")

            nome = input("Digite o nome do passageiro: \n")

            inserir_passageiros(conn, cur, cpf, nome)

        case 6:
            #PEDIDO
            passageiro =  listar_passageiros(cur)

            if not passageiro:
                print("Nao ha passageiros listados\n")
                return
            
            print("Selecione um passageiro listado abaixo: \n")
            cabecalho = ["ID_PASSAGEIRO", "CPF", "NOME"]
            imprimir(cabecalho, passageiro)
            
            id = -1 
            while(id == -1):
                id_passageiro = int(input("Digite o id do passageiro escolhido: \n"))
                id = verificar_id(id_passageiro, passageiro, 0)
                if(id == -1):
                    print("O id do passageiro esta incorreto\n")

            carona = listar_caronas(cur)
            
            if not carona:
                print("Nao ha caronas listada\n")
                return
            
            print("selecione uma das caronas abaixo: \n")
            cabecalho = ["ID_CARONA", "ORIGEM", "DESTINO", "DISTANCIA_KM", "DURACAO_MINUTOS", "ID_MOTORISTA", "ID_VEICULO"]
            imprimir(cabecalho, carona)
            
            id = -1
            while(id == -1):
                id_carona = int(input("Digite o id da caorna escolhida: \n"))
                id = verificar_id(id_carona, carona, 2)
                if(id == -1):
                    print("O id do passageiro esta incorreto\n")

            
            data_hora_pedido = datetime.datetime.now()
            inserir_pedido(conn, cur, id_passageiro, id_carona, data_hora_pedido)

        case 7:
            #RECEBE
            motoristas = listar_motoristas(cur)
            
            if not motoristas:
                print("nao ha motoristas listados\n")
                return
            
            print("Selecione um dos motoristas abaixo para a carona: \n")
            cabecalho = ["ID", "CNH", "Nome"]
            imprimir(cabecalho, motoristas)

            id = -1
            while(id == -1):
                id_motorista = int(input("Digite o id do motorista escolhido: \n"))
                id = verificar_id(id_motorista, motoristas, 0)
                if(id == -1):
                    print("O id do motorista esta incorreto\n")

            pagamento = listar_recebe_disponiveis(cur)

            if not pagamento:
                print("Nao ha recebimentos disponiveis\n")
                return
            
            print("Selecione um dos pagamentos abaixo: \n")
            cabecalho = ["ID_PAGAMENTO", "VALOR"]
            imprimir(cabecalho, pagamento)

            id = -1
            while(id == -1):
                id_pagamento = int(input("Digite o id do pagamento escolhido: \n"))
                id = verificar_id(id_pagamento, pagamento, 0)
                if(id == -1):
                    print("O id do pagamento esta incorreto\n")
            
            data_hora_recebe = datetime.datetime.now()

            inserir_recebe(conn, cur, id_motorista, id_pagamento, data_hora_recebe)

        case 8: 
            #VEICULOS
            modelo = input("Digite o modelo do carro: \n")
            placa = input("Digite a placa do carro: \n")
            ano = int(input("Digite o ano do carro: \n"))
            cor = input("Digite a cor do carro: \n")
            capacidade_passageiro = int(input("Quantos passageiros cabem: \n"))
            
            print("Selecione um dos motoristas abaixo para a carona: \n")
            motoristas = listar_motoristas(cur)

            if not motoristas:
                print("Nao ha motoristas registrados. \n")
                return

            cabecalho = ["ID", "CNH", "Nome"]
            imprimir(cabecalho, motoristas)
            id_motorista = int(input("Digite o id do motorista escolhido: \n"))

            inserir_veiculos(conn, cur, modelo, placa, ano, cor, capacidade_passageiro, id_motorista)

        case 9:
            print("Voltar\n")
            return
        
        case _:
            print("opção inválida\n")
