import pandas as pd

def top_n_by_cluster(df: pd.DataFrame, n: int = 5) -> dict:
    """
    Returns top n cities by each index metric for each cluster.
    
    Output format:
    {
        cluster_number: {
            'Indeks Ekonomi': DataFrame,
            'Indeks Pendidikan': DataFrame,
            'Cluster': DataFrame,
            'Indeks Accumulative': DataFrame
        },
        ...
    }
    """
    clusters = df['Cluster'].unique()
    result = {}

    for cluster in sorted(clusters, reverse=True):
        cluster_df = df[df['Cluster'] == cluster]

        result[cluster] = {
            'Indeks Ekonomi': cluster_df.nlargest(n, 'Indeks Ekonomi')[['City', 'Indeks Ekonomi']],
            'Indeks Pendidikan': cluster_df.nlargest(n, 'Indeks Pendidikan')[['City', 'Indeks Pendidikan']],
            'Cluster': cluster_df.nlargest(n, 'Cluster')[['City', 'Cluster']],
            'Indeks Accumulative': cluster_df.nlargest(n, 'Indeks Accumulative')[['City', 'Indeks Accumulative']]
        }

    return result


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
