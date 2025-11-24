import pandas as pd

def top_n_accumulative(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Returns top n cities by Accumulative Index.
    """
    return df.nlargest(n, 'Indeks Accumulative')[['City', 'Indeks Accumulative']]

def top_n_by_index(df: pd.DataFrame, index_col: str, n: int = 5) -> pd.DataFrame:
    """
    Returns top n cities by a specific index (Indeks Ekonomi, Pendidikan, Kesehatan)
    """
    return df.nlargest(n, index_col)[['City', index_col]]

def bottom_n_concern(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Returns bottom n cities with the lowest accumulative index.
    """
    return df.nsmallest(n, 'Indeks Accumulative')[['City', 'Indeks Accumulative']]

def cluster_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Returns the count of cities per cluster.
    """
    return df['Cluster'].value_counts().sort_index()
