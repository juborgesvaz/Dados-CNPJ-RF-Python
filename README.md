# Base CNPJ Receita Federal - Python

Processamento via Python dos [dados de empresa, estabelecimento e sócio da base pública de CNPJs da Receita Federal](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj) e disponibiliza em um banco de dados estruturados para consumo.

O novo layout do dados abertos do CNPJ  está disponível [aqui](https://www.gov.br/receitafederal/pt-br/assuntos/orientacaotributaria/cadastros/consultas/arquivos/NOVOLAYOUTDOSDADOSABERTOSDOCNPJ.pdf).


## Antes de executar
O arquivo de dados disponibilizado pela RF vem quebrado e é muito grande. O script implementa o fluxo utilizando apenas 1 parte devido ao tamanho da base e limitação de recursos para processamento.

No local onde salvar o 'script.py', criar três pastas: 'Raw', 'Standardized' e 'Conformed'.


## Scheduler para execução periódica


## Dados Raw
Pasta onde salvo os dados baixados no seu formato original.

## Dados Standardized
Pasta onde transformo os arquivos em um formato mais fácil para leitura.

## Dados Conformed
Pasta onde salvo os dados processados para disponibilização na aplicação.
(Padronização do tipo do dado, nome de coluna, melhoria do conteúdo).
