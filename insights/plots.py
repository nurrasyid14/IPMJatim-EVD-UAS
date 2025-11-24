import plotly.express as px
import pandas as pd

def horizontal_bar(df: pd.DataFrame, title: str, x_col: str, y_col: str, top: bool = True):
    """
    Creates a horizontal bar chart with automatic color scaling.
    
    Parameters:
        df : pd.DataFrame
            Data to plot
        title : str
            Chart title
        x_col : str
            Column name for values (x-axis)
        y_col : str
            Column name for categories (y-axis)
        top : bool
            If True, use blue gradient (higher = darker)
            If False, use red gradient (lower = darker)
    
    Returns:
        plotly.graph_objects.Figure
    """
    if top:
        color_scale = 'Blues'
    else:
        color_scale = 'Reds_r'  # reversed red so lower = darker
    
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        orientation='h',
        color=x_col,
        color_continuous_scale=color_scale,
        text=x_col
    )
    
    fig.update_layout(
        title_text=title,
        yaxis={'categoryorder': 'total ascending'},
        coloraxis_colorbar=dict(title=x_col)
    )
    
    return fig


def pie_chart(series: pd.Series, title: str):
    """
    Creates a pie chart from a pandas Series.
    
    Parameters:
        series : pd.Series
            Indexed by category, values are counts
        title : str
            Chart title
    
    Returns:
        plotly.graph_objects.Figure
    """
    fig = px.pie(
        names=series.index,
        values=series.values,
        title=title,
        hole=0.3
    )
    return fig


def pca_3d(df: pd.DataFrame):
    """
    Creates a 3D PCA projection using Indeks Kesehatan, Pendidikan, Ekonomi as x,y,z.
    Colors by Cluster.
    
    Parameters:
        df : pd.DataFrame
            Must contain 'Indeks Kesehatan', 'Indeks Pendidikan', 'Indeks Ekonomi', 'Cluster', 'City'
    
    Returns:
        plotly.graph_objects.Figure
    """
    required_cols = ['Indeks Kesehatan', 'Indeks Pendidikan', 'Indeks Ekonomi', 'Cluster', 'City']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain column '{col}' for PCA 3D plot.")
    
    fig = px.scatter_3d(
        df,
        x='Indeks Kesehatan',
        y='Indeks Pendidikan',
        z='Indeks Ekonomi',
        color=df['Cluster'].astype(str),
        hover_name='City',
        title="3D PCA Projection of Cities"
    )
    
    return fig
