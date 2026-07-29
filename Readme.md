# Algoritmo para Identificação de Ruptura de Estoque

Algoritmo desenvolvido como parte da Artigo: "Identificação retrospectiva de rupturas de estoque no varejo alimentar: um modelo baseado em dados transacionais e seus ganhos para a gestão**"

O arquivo (```Identification.py```) faz a identificação prévia dos dados (rotulagem) com base em dados passados e futuros. 
Desenvolvido apenas a partir de regras de negócio estabelecidas.


## Identification.py
Idenfificação da ruputura baseada nos dados passados.  
Verifica se um item esteve em estado de ruptura em um determinado período baseado em seu reinício de vendas ou prazo de reposição (0 = Não e 1 = Sim).  
Variáveis de entrada (data atual, código do produto, data da última entrada, data da próxima venda e data da próxima entrada) no formato "yyyy-mm-dd"

Teste através do arquivo ```ExecutarIdentificacao.py```



