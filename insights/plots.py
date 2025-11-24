import plotly.express as px

# 1. Sideways Bar Plot
def horizontal_bar(df, title, x_col, y_col):
    fig = px.bar(df, x=x_col, y=y_col, orientation='h', color=x_col, text=x_col)
    fig.update_layout(title_text=title, yaxis={'categoryorder':'total ascending'})
    return fig

# 2. Pie chart of cluster distribution
def pie_chart(series, title):
    fig = px.pie(values=series.values, names=series.index, title=title)
    return fig

# 3. 3D PCA Projection
from sklearn.decomposition import PCA

def pca_3d(df):
    pca = PCA(n_components=3)
    features = df[['Indeks Kesehatan', 'Indeks Pendidikan', 'Indeks Ekonomi']]
    components = pca.fit_transform(features)
    
    df_pca = df.copy()
    df_pca['PC1'] = components[:,0]
    df_pca['PC2'] = components[:,1]
    df_pca['PC3'] = components[:,2]
    
    fig = px.scatter_3d(
        df_pca, x='PC1', y='PC2', z='PC3', color='Cluster',
        hover_data=['City'],
        title='3D PCA Projection of Cities'
    )
    fig.update_layout(scene=dict(
        xaxis_title='PC1 (Index Health)',
        yaxis_title='PC2 (Index Education)',
        zaxis_title='PC3 (Index Economy)'
    ))
    return fig
