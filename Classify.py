import pandas as pd
from snownlp import sentiment
from snownlp import SnowNLP
import xlsxwriter

def type_class(text):
    if text > 0.65:
        text = '积极'
    elif text >= 0.4 and text <= 0.65:
        text = '中性'
    else:
        text = '消极'
    return text

path = r"C:\\Users\\Administratior\\Desktop\\ncm\\ncmhotcomments.xlsx"   

df = pd.read_excel(path)

df['score'] = df['content'].apply(lambda x: SnowNLP(x).sentiments)
df['type'] = df['score'].apply(lambda x: type_class(x))
df.to_excel(r"C:\\Users\\Administratior\\Desktop\\ncm\\ncmhotcomments.xlsx", sheet_name="01", index=False, header=True, engine='xlsxwriter')