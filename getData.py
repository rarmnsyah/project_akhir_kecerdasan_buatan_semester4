import pandas as pd
import numpy as np
import os

def get_data(nameFile, nrows):
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, 'test1', 'job-recommendation', 'splitjobs', 'splitjobs')
    df = pd.read_csv(os.path.join(path, 'jobs1.tsv'), sep='\t',  nrows=nrows)
    df.to_csv(f'{nameFile}.csv')

# get_data('newdf', 1000)

path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv('newdf.csv')
print(df.head())

