from tabulate import tabulate 
from psycopg2 import Error

def listar_motoristas(cur):
    try:
        cur.execute("SELECT id_motorista, cnh, nome FROM motoristas ORDER BY id_motorista;")
        motoristas = cur.fetchall() 
        return motoristas
    
    except Error as e:
        print(f"Erro ao listar motoristas: {e}")
        return []
    
def listar_veiculos(cur):
    try:
        cur.execute("SELECT id_veiculo, modelo, placa, ano, cor, capacidade_passageiro, id_motorista FROM veiculos;")
        veiculos = cur.fetchall()
        return veiculos
    
    except Error as e:
        print(f"Erro ao listar veiculos: {e}")
        return []
    
def listar_caronas(cur):
    try:
        cur.execute("SELECT id_carona, origem, destino, distancia_km, duracao_minutos, id_motorista, id_veiculo FROM carona")
        carona = cur.fetchall()
        return carona
    
    except Error as e:
        print(f"Erro ao listar a carona: {e}")
        return [] 
    
def listar_pagar (cur):
    try:
        cur.execute("SELECT id_passageiro, id_pagamento, data_hora_pagamento FROM pagar")
        pagar = cur.fetchall()
        return pagar
    
    except Error as e:
        print(f"Erro ao listar o pagamento: {e}")
        return [] 

    
def listar_passageiros(cur):
    try:
        cur.execute("SELECT id_passageiro, cpf, nome FROM passageiros")
        passageiros = cur.fetchall()
        return passageiros
    
    except Error as e:
        print(f"Erro ao listar o passageiro: {e}")
        return []    

def listar_pedido(cur):
    try:
        cur.execute("SELECT id_passageiro, id_carona, data_hora_pedido FROM pedido") 
        carona =  cur.fetchall()
        return carona
    
    except Error as e:
        print(f"Erro ao listar o pedido: {e}")
        return [] 
    
def listar_pagamento(cur):
    try:
        cur.execute("SELECT id_pagamento, valor FROM pagamento")
        pagamento = cur.fetchall()
        return pagamento
    
    except Error as e:
        print(f"Erro ao listar o pedido: {e}")
        return [] 
    
def listar_recebe(cur):
    try:
        cur.execute("SELECT id_motorista, id_pagamento, data_recebe FROM recebe")
        recebe =cur.fetchall()
        return recebe
    
    except Error as e:
        print(f"Erro ao listar o deposito: {e}")
        return [] 
    
def imprimir (cabecalho, tabela):
    if tabela:
        print(tabulate(tabela, headers = cabecalho, tablefmt = "psql"))
    else:
        print(f"Nenhum '{tabela}' encontrado no anco de dados.")

def listar_pagamentos_disponiveis(cur):
    """
    Lista apenas os pagamentos que ainda não foram associados na tabela 'pagar'.
    """
    try:
        sql = """
            SELECT
                p.id_pagamento,
                p.valor
            FROM
                pagamento AS p
            LEFT JOIN
                pagar AS pg ON p.id_pagamento = pg.id_pagamento
            WHERE
                pg.id_pagamento IS NULL
            ORDER BY
                p.id_pagamento;
        """
        cur.execute(sql)
        pagamentos_disponiveis = cur.fetchall()
        return pagamentos_disponiveis
    
    except Error as e:
        print(f"Erro ao listar pagamentos disponíveis: {e}")
        return []
    
def listar_recebe_disponiveis(cur):
    """
    Lista apenas os pagamentos que ainda não foram associados na tabela 'pagar'.
    """
    try:
        sql = """
            SELECT
                p.id_pagamento,
                p.valor
            FROM
                pagamento AS p
            LEFT JOIN
                recebe AS r ON p.id_pagamento = r.id_pagamento
            WHERE
                r.id_pagamento IS NULL
            ORDER BY
                p.id_pagamento;
        """
        cur.execute(sql)
        pagamentos_disponiveis = cur.fetchall()
        return pagamentos_disponiveis
    
    except Error as e:
        print(f"Erro ao listar pagamentos disponíveis: {e}")
        return []
    
    
def menu_listar(cur):
    opcao2 = int(input("Escolha uma das opcoes: \n 1 - carona\n 2 - motoristas\n 3 - pagamento\n 4 - pagar\n 5 - passageiros\n 6 - pedido\n 7 - recebe\n 8 - veiculos\n 9 - voltar\n"))
                
    match opcao2:
        case 1:
            carona = listar_caronas(cur)

            if not carona:
                print("Nao ha carona registrada. \n")
                return

            cabecalho = ["ID_CARONA", "ORIGEM", "DESTINO", "DISTANCIA_KM", "DURACAO_MINUTOS", "ID_MOTORISTA", "ID_VEICULO"]
            imprimir(cabecalho, carona)

        case 2:
            motoristas = listar_motoristas(cur)

            if not motoristas:
                print("Nao ha motoristas registrados. \n")
                return

            cabecalho = ["ID", "CNH", "Nome"]
            imprimir(cabecalho, motoristas)

        case 3:
            pagamento = listar_pagamento(cur)

            if not pagamento:
                print("Nao ha pagamento registrados. \n")
                return
            
            cabecalho = ["ID_PAGAMENTO", "VALOR"]
            imprimir(cabecalho, pagamento)

        case 4:
            pagar = listar_pagar(cur)

            if not pagar:
                print("Nao ha pagar registrados. \n")
                return
            
            cabecalho = ["ID_PASSAGEIRO", "ID_PAGAMENTO", "DATA_HORA_PAGAR"]
            imprimir(cabecalho, pagar)

        case 5:
            passageiro =  listar_passageiros(cur)

            if not passageiro:
                print("Nao ha passageiro registrados. \n")
                return
            
            cabecalho = ["ID_PASSAGEIRO", "CPF", "NOME"]
            imprimir(cabecalho, passageiro)

        case 6:
            pedido = listar_pedido(cur)

            if not pedido:
                print("Nao ha pedidos registrados. \n")
                return
            
            cabecalho = ["ID_PASSAGEIRO", "ID_CARONA", "DATA_HORA_PEDIDO"]
            imprimir(cabecalho, pedido)

        case 7:
            recebe = listar_recebe(cur)

            if not recebe:
                print("Nao ha registros de rebimento. \n")
                return
            
            cabecalho = ["ID_MOTORISTA", "ID_PAGAMENTO", "DATA_RECEB"]
            imprimir(cabecalho, recebe)

        case 8:
            veiculos = listar_veiculos(cur)

            if not veiculos:
                print("Nao ha veiculos registrados. \n")
                return
            
            cabecalho = ["id_veiculo", "modelo", "placa", "ano", "cor", "capacidade_passageiro", "id_motorista"]
            imprimir(cabecalho, veiculos)

        case 9:
            print("Voltar\n")
            return
        
        case _:
            print("opção inválida\n")