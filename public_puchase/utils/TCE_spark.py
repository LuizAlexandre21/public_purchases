# Pacotes 
import requests 
import tempfile
import zipfile
import csv 
import os 
import sys
import logging

# Configurando o logging 
# Configurando apresentação do log em terminal 
if sys.stdout.isatty():
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
else:
    LOG_FORMAT = "%(name)s - %(levelname)s - %(message)s"

# Configurando os parametros do log
logging.basicConfig(level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper()), format=LOG_FORMAT, datefmt="%Y-%m-%dT%H:%M:%S")

# Criando a classe logger - engine odd
logger = logging.getLogger("TCE_data")

# Lista com os endereços 
Links = [
    'https://drive.google.com/u/0/uc?id=1OfxA4FGzR4zOy8KIdPl8cAK5ojsJv-vV&export=download&confirm=t',
    'https://drive.google.com/u/0/uc?id=1FEGbEIhE3WQrkd3iy20b5fBi2xwbakXL&export=download&confirm=t',
    'https://drive.google.com/u/0/uc?id=1KT1N3KrLlfpm_UBRbASk4IBZsS-ij2Q5&export=download&confirm=t',
    'https://drive.google.com/u/0/uc?id=1NGpVRqo9xbvEUSzR9KWOOf4V6GeBc5a7&export=download&confirm=t',
    ]   
logging.info(f"Existem atualmente {len(Links)} Endereços")

# Lista com os Anos 
Ano = [2016,2017,2018,2019]
logging.info(f"Existem atualmente dados para os seguintes anos: {Ano}")

# Criando a classe de dados 
class TCE_data:
    # Exportando os resultados 
    licitação =[] 
    item = []

    # Definindo a função construtora 
    def __init__(self):

        # Fazendo downloads dos arquivos 
        for doc in Links:

            # Download dos documentos contidos no google drive
            r = requests.get(doc)
            
            # Verificando o status code da requisição 

            match r.status_code:
                case 200:
                    logging.info("Download concluido com sucesso")
                case _: 
                    logging.error("Download apresentou algum erro")
 
            # Salvando arquivos 
            temp = self.storage(r) 

            # Extraindo os dados dos arquivos comprimidos 
            tempo = zipfile.ZipFile(temp, 'r')
            logging.info("Arquivos extraidos com sucesso")

            # Salvando os dataframes 
            items, licitacao = self.save(tempo)
            
            # Concatenando os dataframes
            # Items 
            item.append(pd.concat(items))

            # Licitação 
            licitacao.append(pd.concat(licitacao))



    # Função para amarzenamento de arquivos em local temporario 
    def storage(self,contents):

        # Criando arquivo temporario 
        temp = tempfile.NamedTemporaryFile().name +'.zip'
        logging.info(f"O arquivo temporario criado foi {temp}")

        # Salvando os arquivos nos locais temporarios 
        try:
            with open(temp,'wb') as f:
                f.write(contents.content)
            logging.info("O arquivo foi salvo com sucesso")       
        
        except:
            logging.error("O arquivo apresentou problemas para ser salvo")


        return temp

    # Função para salvar arquivos comprimidos

    def save(self,ziper):
        # Listas de output
        item, licitação = [],[]
        
        # Arquivos contidos na compressão 
        lista = ziper.filelist

        # Extração dos arquivos de licitações e items
        for arch in lista:

            # Switch Case Structure
            match arch.filename: 

                # Filtrando os arquivos de items 
                case 'item.csv':
                    
                    # Extraindo os arquivos de item 
                    try:
                        ziper.extract('item.csv')
                        logging.info('Arquivo extraido com sucesso')
                    except:
                        logging.error('A extração apresentou problemas')

                    # Salvando os arquivos 
                    item.append(pd.read_csv('item.csv'))

                    # Removendo os arquivos 
                    os.remove('item.csv')

                # Filtrando os arquivos de licitação 
                case 'licitacao.csv': 

                    # Extraindo os arquivos de item 
                    try:
                        ziper.extract('licitacao.csv')
                        logging.info('Arquivo extraido com sucesso')
                    except:
                        logging.error('A extração apresentou problemas')
                    
                    # Salvando os arquivos 
                    licitação.append(pd.read_csv('licitacao.csv'))

                    # Removendo os arquivos 
                    os.remove('licitacao.csv')
            
        return item,licitação

 