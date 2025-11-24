import pandas as pd

def load_and_preprocess(csv_path):
    df = pd.read_excel(csv_path)
    
    # Keep only necessary columns
    df = df[['City', 'Indeks Kesehatan', 'Indeks Pendidikan', 'Indeks Ekonomi', 'Cluster']]
    
    # Compute accumulative index
    df['Indeks Accumulative'] = df[['Indeks Kesehatan', 'Indeks Pendidikan', 'Indeks Ekonomi']].mean(axis=1)
    
    return df
