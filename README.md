# Base CNPJ Receita Federal - Python

Processamento via Python dos [dados de empresa, estabelecimento e sócio da base pública de CNPJs da Receita Federal](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj) e disponibiliza em um banco de dados estruturados para consumo.

O novo layout do dados abertos do CNPJ  está disponível [aqui](https://www.gov.br/receitafederal/pt-br/assuntos/orientacaotributaria/cadastros/consultas/arquivos/NOVOLAYOUTDOSDADOSABERTOSDOCNPJ.pdf).


## Antes de executar
O arquivo de dados disponibilizado pela RF vem quebrado e é muito grande. O script implementa o fluxo utilizando apenas 1 parte devido ao tamanho da base e limitação de recursos para processamento.


## Scheduler para execução periódica
