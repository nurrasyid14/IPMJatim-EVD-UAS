def top_n_by_cluster(df, n=3):
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
