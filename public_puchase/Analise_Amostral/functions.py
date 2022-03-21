# Pacotes 
import pandas as pd 
import json
import logging
import re
import unicodedata
from multidict import MultiDict
from operator import itemgetter
from spacy.lang.pt.stop_words import STOP_WORDS as stop_words
# Tamanho de um dataframe 
def data_describe(dataframe):

    # Calculando o espaço do dataframe 
    space_ram = round(sum(dataframe.memory_usage())/(1024)**2,2)

    # Calculando o tamanho de linhas do dataframe 
    lines_count = int(len(dataframe))

    # Calculando a quantidade de colunas 
    columns_count = int(len(dataframe.columns))

    # Numero de items nulos

    return list((space_ram,lines_count,columns_count))

# Removendo emojis do texto
def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        "]+",
        flags=re.UNICODE
    )
    
    return emoji_pattern.sub(r'', text)

# Modificando a capitalização dos textos
def lower_text(text):
    return text.lower()

# Removendo caracteres especiais 
def remove_special_chars(text):
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("utf-8")
    
    return text

# Removendo pontuações
def punctuation(text):
    text = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', text)

    return text

# Removendo espaços desnecessário
def space_remove(text):
    text = text.replace("  ","")
    try:
        if text[-1] == " ":
            return text[:-1]
    except:
        print("text null")
    return text 

# Limpeza de stop words
def sanitize(sentence):
    if sentence.isspace():
        return " "
    else:
        lst =[]
        for token in sentence.split():
            if token.lower() not in stop_words:
                lst.append(token)

    return " ".join(lst)


