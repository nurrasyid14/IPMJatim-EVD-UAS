import streamlit as st
from data_handler import load_and_preprocess
from insights import (
    top_n_accumulative,
    top_n_by_index,
    bottom_n_concern,
    cluster_distribution,
    horizontal_bar,
    pie_chart,
    pca_3d
)

# -----------------------
# Streamlit Settings
# -----------------------
st.set_page_config(page_title="Dashboard IPM Jatim 2024", layout="wide")
st.title("City Index Dashboard")

# -----------------------
# Load Data
# -----------------------
df = load_and_preprocess("data_handler/IPM Jatim 2024.xlsx")

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.header("Filters")
clusters = sorted(df['Cluster'].unique())
cluster_filter = st.sidebar.multiselect(
    "Select clusters to show",
    options=clusters,
    default=clusters
)
filtered_df = df[df['Cluster'].isin(cluster_filter)]

# -----------------------
# Top 10 Accumulative Index
# -----------------------
top_acc_df = top_n_accumulative(filtered_df, n=10)
st.plotly_chart(
    horizontal_bar(
        top_acc_df,
        title="Top 10 Kota dengan Indeks Terbaik",
        x_col='Indeks Accumulative',
        y_col='City',
        top=True  # Blue gradient
    ),
    use_container_width=True
)

# -----------------------
# Top 5 by Individual Indexes
# -----------------------
for col in ['Indeks Ekonomi', 'Indeks Pendidikan', 'Indeks Kesehatan']:
    top_index_df = top_n_by_index(filtered_df, col, n=5)
    st.plotly_chart(
        horizontal_bar(
            top_index_df,
            title=f"Top 5 {col}",
            x_col=col,
            y_col='City',
            top=True  # Blue gradient
        ),
        use_container_width=True
    )

# -----------------------
# Bottom 5 Concern
# -----------------------
bottom_df = bottom_n_concern(filtered_df, n=5)
st.plotly_chart(
    horizontal_bar(
        bottom_df,
        title="5 Kab/Kota yang perlu dikembangkan",
        x_col='Indeks Accumulative',
        y_col='City',
        top=False  # Red gradient
    ),
    use_container_width=True
)

# -----------------------
# Cluster Distribution Pie Chart
# -----------------------
st.header("Cluster Members Distribution")
distribution = cluster_distribution(filtered_df)
st.plotly_chart(
    pie_chart(distribution, title="Anggota Cluster"),
    use_container_width=True
)

# -----------------------
# 3D PCA Projection
# -----------------------
st.header("Visualisasi Cluster Indeks Kab/Kota")
st.plotly_chart(
    pca_3d(filtered_df),
    use_container_width=True
)
