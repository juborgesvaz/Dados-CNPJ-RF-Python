# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Bibliotecas 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import zipfile
import io
import datetime

# URL da página da RF para download das bases
url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
soup

downloads = soup.find_all('a', {'class':'external-link'})

# Diretório 
directory = os.getcwd()
# directory = "C:/Users/DELL/Documents/RF RIOT/"


# Tabela com as urls
urls, nomes = [], []
for x in soup.find_all('a', {'class':'external-link'}):
    urls.append(x['href'])
    nomes.append(x.get_text())
    
df_downloads = pd.DataFrame(
    {'nome': nomes,
     'url': urls})

df_downloads['arquivo'] = df_downloads['url'].str.rpartition('/', False).str[-1]

# Dowload dos arquivos

# Uso o 'for' abaixo quando for baixar todas as tabelas da RF
# for x in range(len(df_downloads)): 
for x in range(1):
    arq = df_downloads['arquivo'][x]
    url_arq = df_downloads['url'][x]
    req = requests.get(url_arq)
    open("\\Raw" + arq, 'wb').write(req.content)


# Definindo Layout das bases para carga no Banco de dados
layout_arqs = {'EMPRE': {'columns':
                          {'st_cnpj_base': str, 'st_razao_social': str, 'cd_natureza_juridica': str, 'cd_qualificacao': str,
                              'vl_capital_social': str, 'cd_porte_empresa': str, 'st_ente_federativo': str},
                          'table_name_db': 'tb_empresa'},
                'ESTABELE': {'columns':
                             {'st_cnpj_base': str, 'st_cnpj_ordem': str, 'st_cnpj_dv': str, 'cd_matriz_filial': str, 'st_nome_fantasia': str, 'cd_situacao_cadastral': str,
                              'dt_situacao_cadastral': str, 'cd_motivo_situacao_cadastral': str, 'st_cidade_exterior': str, 'cd_pais': str, 'dt_inicio_atividade': str,
                              'cd_cnae_principal': str, 'cd_cnae_secundario': str, 'st_tipo_logradouro': str, 'st_logradouro': str, 'st_numero': str, 'st_complemento': str,
                              'st_bairro': str, 'st_cep': str, 'st_uf': str, 'cd_municipio': str, 'st_ddd1': str, 'st_telefone1': str, 'st_ddd2': str, 'st_telefone2': str,
                              'st_ddd_fax': str, 'st_fax': str, 'st_email': str, 'st_situacao_especial': str, 'dt_situacao_especial': str
                              }, 'table_name_db': 'tb_estabelecimento'},
                'SIMPLES': {'columns':
                            {'st_cnpj_base': str, 'st_opcao_simples': str, 'dt_opcao_simples': str, 'dt_exclusao_simples': str,
                             'st_opcao_mei': str, 'dt_opcao_mei': str, 'dt_exclusao_mei': str
                             }, 'table_name_db': 'tb_dados_simples'},
                'SOCIO': {'columns':
                           {'st_cnpj_base': str, 'cd_tipo': str, 'st_nome': str, 'st_cpf_cnpj': str, 'cd_qualificacao': str, 'dt_entrada': str,
                            'cd_pais': str, 'st_representante': str, 'st_nome_representante': str, 'cd_qualificacao_representante': str, 'cd_faixa_etaria': str},
                          'table_name_db': 'tb_socio'},
                'PAIS': {'columns': {'cd_pais': str, 'st_pais': str}, 'table_name_db': 'tb_pais'},
                'MUNIC': {'columns': {'cd_municipio': str, 'st_municipio': str}, 'table_name_db': 'tb_municipio'},
                'QUALS': {'columns': {'cd_qualificacao': str, 'st_qualificacao': str}, 'table_name_db': 'tb_qualificacao_socio'},
                'NATJU': {'columns': {'cd_natureza_juridica': str, 'st_natureza_juridica': str}, 'table_name_db': 'tb_natureza_juridica'},
                'MOTI': {'columns': {'cd_motivo_situacao_cadastral': str, 'st_motivo_situacao_cadastral': str}, 'table_name_db': 'tb_motivo_situacao_cadastral'},
                'CNAE': {'columns': {'cd_cnae': str, 'st_cnae': str}, 'table_name_db': 'tb_cnae'}
                }


    
# Listar arquivos do diretório
files = os.listdir(directory+"\\Raw")

file = "K3241.K03200Y0.D20108.EMPRECSV.zip"
arq = "K3241.K03200Y0.D20108.EMPRECSV.zip"



# Descompactando Arquivo Zip

# Uso o 'for' abaixo quando for descompactar todas as tabelas da RF
# for x in range(len(df_downloads)): 
for x in range(1):
    arq = df_downloads['arquivo'][x]

    # Seleciono o modelo de layout
    modelo = arq.replace('.zip', '').split('.')[-1].replace('CSV', '') if arq.find('SIMPLES') < 0 else 'SIMPLES'
    cols_names = list(layout_arqs[modelo]['columns'].keys())
    
    with zipfile.ZipFile(directory + "\\Raw" + arq, 'r') as zip:
        d = zip.read(zip.namelist()[0])
        df = pd.read_csv(io.BytesIO(d), delimiter=';', header=None, chunksize=65000, iterator=True, dtype=str, encoding="ISO-8859-1")
        df = pd.concat(df, ignore_index=True)
    
    df.to_csv('\\Standardized'+arq.replace('.zip', '')+'.csv', index=False, header=None, sep=';')
    
    # Insiro o layout 
    df = df.set_axis(cols_names, axis=1, inplace=False)
    
    df.to_csv('\\Conformed'+arq.replace('.zip', '')+'.csv', index=False, header=None, sep=';')
    
# Cron Job   
with open('dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))

