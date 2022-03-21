# Analise das licitações do TCE-RS - Amostral

Este projeto apresenta uma análise dos dados acerca das licitações, quais foram obtidas junto ao portal de dados abertos do TCE-RS. O exercício empírico foi executado por meio dos dados acerca das licitações e de items, disponibilizados nos arquivos *licitacao.csv* e *item.csv* 
------ 

## 1. Pre requisitos
### 1.1 Poetry 
Poetry ajuda você a declarar, gerenciar e instalar dependências de projetos Python, garantindo que você tenha a pilha certa em todos os lugares.
Poetry traz ao Python o tipo de ferramenta de gerenciamento de projetos “tudo em um” que Go e Rust apreciam há muito tempo. Permitir que os projetos tenham dependências determinísticas com versões específicas de pacotes para que sejam construídos consistentemente em diferentes locais. O Poetry também facilita a criação, empacotamento e publicação de projetos e bibliotecas no PyPI para que outros possam compartilhar os frutos de seus trabalhos em Python.
O objetivo da **public_purchases** é obter uma analise simples dos dados obtidos juntos ao TCE-RS.


### 1.2 Instalando o Poetry
# Como executar a aplicação 
- Linux 
```sh 
curl -sSL \
https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```
- Windows 
```sh 
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```
## 2. Arquivos
## Para executar dentro do contêiner:
### Requisitos:

- **pyproject.toml** - É o formato de arquivo especificado do PEP 518 que contém os requisitos do sistema de compilação dos projetos Python.
- **utils** - Arquivos contendo funções auxiliares para o projeto 
  - **TCE_data.py** - Arquivo contendo a classe para construção do dataframe acerca das tabelas items e licitaçõe
- **Analise_Amostral** - Analise dos dados do TCE-RS, para o ano de 2016  
  - **functions.py** - Arquivo contendo funções para o auxilio da construção da analise dos dados 
  - **Analise das licitações do TCE-RS - Amostral.ipynb** - Notebook contendo a analise dos dados

## To run without the container:
### Requirements:
- Poetry

## 3. Starting Project - Local
### 3.1 Cloning the repository
```sh 
https://github.com/LuizAlexandre21/public_puchases.git
```

### 3.2 Installing project dependencies
```sh
sudo poetry install 
```

### 3.3 Running the project
#### 3.3.1 
```sh
poetry run jupyter notebook public_puchase/Analise_Amostral/Analiseas_licitações\ do_TCE-RS\ -\ Amostral.ipynb 
```
