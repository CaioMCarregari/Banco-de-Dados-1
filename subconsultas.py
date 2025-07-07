from psycopg2 import Error
from tabulate import tabulate 
from listar import *

def carona_maior_distancia(cur):
    try:
        sql = """
            SELECT
                c.id_carona,
                c.origem,
                c.destino,
                c.distancia_km,
                m.nome AS nome_motorista
            FROM
                carona AS c
            JOIN
                motoristas AS m ON c.id_motorista = m.id_motorista
            WHERE
                c.distancia_km = (SELECT MAX(distancia_km) FROM carona);
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao executar consulta com subquery: {e}")
        return []
    
def carona_menor_distancia(cur):
    try:
        sql = """
            SELECT
                c.id_carona,
                c.origem,
                c.destino,
                c.distancia_km,
                m.nome AS nome_motorista
            FROM
                carona AS c
            JOIN
                motoristas AS m ON c.id_motorista = m.id_motorista
            WHERE
                c.distancia_km = (SELECT MIN(distancia_km) FROM carona);
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao executar consulta com subquery: {e}")
        return []

def passageiro_maior_pagamento(cur):
    try:
        sql = """
            SELECT
                p.id_passageiro,
                p.nome,
                p.cpf,
                pag.valor AS valor_pago
            FROM
                passageiros AS p
            JOIN
                pagar AS pa ON p.id_passageiro = pa.id_passageiro
            JOIN
                pagamento AS pag ON pa.id_pagamento = pag.id_pagamento
            WHERE
                pag.valor = (SELECT MAX(valor) FROM pagamento);
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao gerar relatório de maior pagamento: {e}")
        return []
    
def passageiro_menor_pagamento(cur):
    try:
        sql = """
            SELECT
                p.id_passageiro,
                p.nome,
                p.cpf,
                pag.valor AS valor_pago
            FROM
                passageiros AS p
            JOIN
                pagar AS pa ON p.id_passageiro = pa.id_passageiro
            JOIN
                pagamento AS pag ON pa.id_pagamento = pag.id_pagamento
            WHERE
                pag.valor = (SELECT MIN(valor) FROM pagamento);
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao gerar relatório de maior pagamento: {e}")
        return []

def motorista_com_mais_caronas(cur):
    try:
        sql = """
            SELECT
                m.id_motorista,
                m.nome,
                COUNT(c.id_carona) AS numero_de_caronas
            FROM
                motoristas AS m
            JOIN
                carona AS c ON m.id_motorista = c.id_motorista
            GROUP BY
                m.id_motorista, m.nome
            HAVING
                COUNT(c.id_carona) = (
                    SELECT MAX(contagem)
                    FROM (
                        SELECT COUNT(id_carona) AS contagem
                        FROM carona
                        GROUP BY id_motorista
                    ) AS contagens_por_motorista
                );
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao gerar relatório de motorista com mais caronas: {e}")
        return []

def passageiro_com_mais_viagens(cur):
    try:
        sql = """
            SELECT
                p.id_passageiro,
                p.nome,
                p.cpf,
                COUNT(ped.id_carona) AS numero_de_viagens
            FROM
                passageiros AS p
            JOIN
                pedido AS ped ON p.id_passageiro = ped.id_passageiro
            GROUP BY
                p.id_passageiro, p.nome, p.cpf
            HAVING
                COUNT(ped.id_carona) = (
                    SELECT MAX(contagem)
                    FROM (
                        SELECT COUNT(*) AS contagem
                        FROM pedido
                        GROUP BY id_passageiro
                    ) AS contagens_por_passageiro
                );
        """
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Error as e:
        print(f"Erro ao gerar relatório de passageiro com mais viagens: {e}")
        return []

def calcular_valor_total_recebido(cur):
    try:
        sql = "SELECT SUM(valor) FROM pagamento;"
        
        cur.execute(sql)
        resultado = cur.fetchone()
        
        if resultado and resultado[0] is not None:
            valor_total = resultado[0]
            return valor_total
        else:
            return 0
            
    except Error as e:
        print(f"Erro ao calcular o valor total: {e}")
        return None
    
def menu_subconsultas(cur):
    opcao2 = int(input("Escola uma das opcoes: \n 1 - Carona com maior distancia \n 2 - Carona com menor distancia\n 3 - passageiro que fez o maior pagamento\n 4 - passageiro que fez o menor pagamento\n 5 - Motoristacom mais carona\n 6 - Passageiro com mais viagens\n 7 - Receita total do app\n"))

    match opcao2:
        case 1:
            print("\n--- Relatorio: Carona(s) de Maior Distancia ---\n")

            maior_carona = carona_maior_distancia(cur)
            
            if not maior_carona:
                print("Ainda nao ha caronas")
                return

            cabecalho = ["ID Carona", "Origem", "Destino", "Distancia (km)", "Nome do Motorista"]
            
            imprimir(cabecalho, maior_carona)

        case 2:
            print("\n--- Relatorio: Carona de Menor Distancia ---\n")

            menor_carona = carona_menor_distancia(cur)
            
            if not menor_carona:
                print("Ainda nao ha caronas")
                return

            cabecalho = ["ID Carona", "Origem", "Destino", "Distancia (km)", "Nome do Motorista"]
            
            imprimir(cabecalho, menor_carona)
            

        case 3:
            print("\n--- Relatorio: Passageiro com o Maior Pagamento ---\n")

            maior_pagamento = passageiro_maior_pagamento(cur)
            
            if not maior_pagamento:
                print("Ainda nao ha pagamentos.")
                return

            cabecalho = ["ID Passageiro", "Nome", "CPF", "Valor Maximo Pago"]
            imprimir(cabecalho, maior_pagamento)

        case 4:
            print("\n--- Relatorio: Passageiro com o Menor Pagamento ---\n")

            menor_pagamento = passageiro_menor_pagamento(cur)
            
            if not menor_pagamento:
                print("Ainda nao ha pagamentos.")
                return

            cabecalho = ["ID Passageiro", "Nome", "CPF", "Menor_valor Pago"]
            imprimir(cabecalho, menor_pagamento)

        case 5:
            print("\n--- Relatório: Motorista(s) com Mais Caronas Realizadas ---")
    
            mais_caronas = motorista_com_mais_caronas(cur)
            
            if not mais_caronas:
                print("Ainda nao ha caronas")
                return

            cabecalho = ["ID Motorista", "Nome do Motorista", "Nº de Caronas"]
            imprimir(cabecalho, mais_caronas)

        case 6:
            print("\n--- Relatório: Passageiro(s) com Mais Viagens Realizadas ---")

            mais_viagens = passageiro_com_mais_viagens(cur)
            
            if not mais_viagens:
                print("Ainda nao ha viagens")
                return

            cabecalho = ["ID Passageiro", "Nome do Passageiro", "CPF", "Nº de Viagens"]
            imprimir(cabecalho, mais_viagens)

        case 7: 
            print("\n--- Relatorio: Faturamento Total da Empresa ---")

            valor_total = calcular_valor_total_recebido(cur)
            
            if valor_total is not None:
                print(f"\nO valor total recebido pela empresa foi de: R$ {valor_total:.2f}")
            else:
                print("Nao foi possivel calcular o faturamento devido a um erro.")
        
        case _: print("opcao invalida")
