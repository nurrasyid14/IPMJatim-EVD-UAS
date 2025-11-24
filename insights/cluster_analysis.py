def top_n_by_cluster(df, n=3):
    clusters = df['Cluster'].unique()
    result = {}
    
    for cluster in sorted(clusters, reverse=True):  # Cluster 3 first, then 2, then 1
        cluster_df = df[df['Cluster'] == cluster]
        
        result[cluster] = {
            'Indeks Ekonomi': cluster_df.nlargest(n, 'Indeks Ekonomi')[['City', 'Indeks Ekonomi']],
            'Indeks Pendidikan': cluster_df.nlargest(n, 'Indeks Pendidikan')[['City', 'Indeks Pendidikan']],
            'Cluster': cluster_df.nlargest(n, 'Cluster')[['City', 'Cluster']],
            'Accumulative': cluster_df.nlargest(n, 'Indeks Accumulative')[['City', 'Indeks Accumulative']]
        }
    return result

def bottom_n_concern(df, n=5):
    return df.nsmallest(n, 'Indeks Accumulative')[['City', 'Indeks Accumulative']]
    
def cluster_distribution(df):
    return df['Cluster'].value_counts()
