from psycopg2 import Error
from listar import *

def juncao_carona(cur):
    """
    Lista todas as caronas com detalhes do motorista (nome) e do veiculo (modelo e placa)
    usando INNER JOIN.
    """
    try:
        sql = """
            SELECT
                c.id_carona,
                c.origem,
                c.destino,
                m.nome AS nome_motorista,
                v.modelo AS modelo_veiculo,
                v.placa AS placa_veiculo,
                c.distancia_km
            FROM
                carona AS c
            INNER JOIN
                motoristas AS m ON c.id_motorista = m.id_motorista
            INNER JOIN
                veiculos AS v ON c.id_veiculo = v.id_veiculo
            ORDER BY
                c.id_carona;
        """
        cur.execute(sql)
        caronas_detalhadas = cur.fetchall()
        return caronas_detalhadas
    except Error as e:
        print(f"Erro ao listar caronas com detalhes: {e}")
        return []
    

def juncao_veiculos_com_motoristas(cur):
    try:
        sql = """
            SELECT
                m.id_motorista,
                m.nome AS nome_proprietario,
                v.id_veiculo,
                v.modelo,
                v.placa,
                v.ano,
                v.cor
            FROM
                veiculos AS v
            JOIN
                motoristas AS m ON v.id_motorista = m.id_motorista
            ORDER BY
                m.nome, v.modelo;
        """
        cur.execute(sql)
        veiculos_com_motoristas = cur.fetchall()
        return veiculos_com_motoristas
    except Error as e:
        print(f"Erro ao listar veículos com motoristas: {e}")
        return []

def juncao_pagar(cur):
    try:
        sql = """
            SELECT
                p.id_passageiro,
                ps.nome,
                p.id_pagamento,
                pg.valor,
                p.data_hora_pagamento
            FROM
                pagar AS p
            JOIN
                passageiros AS ps ON p.id_passageiro = ps.id_passageiro
            JOIN
                pagamento AS pg ON p.id_pagamento = pg.id_pagamento
            ORDER BY
                p.data_hora_pagamento DESC;
        """
        cur.execute(sql)
        pagar = cur.fetchall()
        return pagar
    except Error as e:
        print(f"Erro ao listar registros de 'pagar': {e}")
        return []
    
def juncao_registros_pedido(cur):
    try:
        sql = """
            SELECT
                ped.id_passageiro,
                pas.nome AS nome_passageiro,
                ped.id_carona,
                car.origem,
                car.destino,
                ped.data_hora_pedido
            FROM
                pedido AS ped
            JOIN
                passageiros AS pas ON ped.id_passageiro = pas.id_passageiro
            JOIN
                carona AS car ON ped.id_carona = car.id_carona
            ORDER BY
                ped.data_hora_pedido DESC;
        """
        cur.execute(sql)
        registros = cur.fetchall()
        return registros
    except Error as e:
        print(f"Erro ao listar registros de 'pedido': {e}")
        return []
    
def juncao_recebe(cur):
    try:
        sql = """
            SELECT
                r.id_motorista,
                m.nome AS nome_motorista,
                r.id_pagamento,
                p.valor,
                r.data_recebe
            FROM
                recebe AS r
            JOIN
                motoristas AS m ON r.id_motorista = m.id_motorista
            JOIN
                pagamento AS p ON r.id_pagamento = p.id_pagamento
            ORDER BY
                r.data_recebe DESC;
        """
        cur.execute(sql)
        registros = cur.fetchall()
        return registros
    except Error as e:
        print(f"Erro ao listar registros de 'recebe': {e}")
        return []
    
def menu_juncao (cur):
    opcao2 = int(input("Escolha uma das opcoes:\n 1 - carona,motoristas e veiculos\n 2 - passageiro e pagamento\n 3 - motorista e pagamento\n 4 - passageiro e carona\n 5 - voltar\n"))

    match opcao2:
        case 1:
            carona = juncao_carona(cur)

            if not carona:
                print("Nao ha caronas registradas. \n")
                return
            
            cabecalho = ["ID_CARONA", "ORIGEM", "DESTINO", "NOME_MOTORISTA", "MODELO_VEICULO", "PLACA_VEICULO", "DISTANCIA_KM"] 
            imprimir (cabecalho, carona)

        case 2: 
            pagar = juncao_pagar(cur)

            if not pagar:
                print("Nao ha pagar registrados. \n")
                return

            cabecalho = ["ID_PASSAGEIRO", "NOME", "ID_PAGAMENTO", "VALOR","DATA_HORA_PAGAR"]
            imprimir(cabecalho, pagar)

        case 3:
            recebe = juncao_recebe(cur)

            if not recebe:
                print("Nao ha registros de rebimento. \n")
                return

            cabecalho = ["ID_MOTORISTA", "NOME", "ID_PAGAMENTO", "VALOR","DATA_RECEBE"]
            imprimir(cabecalho, recebe)

        case 4:
            pedido = juncao_registros_pedido(cur)

            if not pedido:
                print("Nao ha pedidos registrados. \n")
                return

            cabecalho = ["ID_PASSAGEIRO", "NOME_PASSAGEIRO", "ID_CARONA", "ORIGEM", "DESTINO", "DATA_HORA_PEDIDO"]
            imprimir(cabecalho, pedido)

        case 5:
            print("Voltar\n")
            return
        
        case _:
            print("opção inválida\n")
