from Identification import Identificar
import pandas as pd


#### Restrições
# Datas no formato: yyyy-mm-dd
# ultima_entrada <= data < proxima_entrada <= proxima_venda

# Inicializa identificação
RUPTURA = Identificar()

# Criando o dicionário com os dados de exemplo
dados = {
    'data': ['2026-06-01', '2026-06-02', '2026-06-03'],
    'codigo': [1, 2, 3],
    'ultima_entrada': ['2026-05-01', '2026-05-02', '2026-05-03'],
    'proxima_venda':  ['2026-06-11', '2026-06-12', '2026-06-13'],
    'proxima_entrada':  ['2026-06-08', '2026-07-09', '2026-06-12'],
}

# Convertendo para DataFrame do Pandas
df = pd.DataFrame(dados)

# Objeto de retorno
retorno = pd.DataFrame()

# Percorre os dados para cálculo
for index, line in df.iterrows():
    # Calcula e imprime o status
    analise = RUPTURA.calcular(line['data'], line['codigo'], line['ultima_entrada'], line['proxima_venda'], line['proxima_entrada'])
    print(f"Para a situação definida:")
    print(f"Data = {line['data']}")
    print(f"Código = {line['codigo']}")
    print(f"Última entrada = {line['ultima_entrada']}")
    print(f"Próxima venda = {line['proxima_venda']}")
    print(f"Próxima entrada = {line['proxima_entrada']}")
    print(f"Temos Ruptura = {analise['Ruptura']}\n")
    retorno = pd.concat([retorno, analise], ignore_index=True)

# Exibe objeto de retorno
print(retorno)


