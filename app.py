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
st.title("Dashboard IPM Jatim 2024")

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
# Top Charts Layout (2x2)
# -----------------------
top_acc_df = top_n_accumulative(filtered_df, n=10)
top_ekonomi_df = top_n_by_index(filtered_df, 'Indeks Ekonomi', n=5)
top_pendidikan_df = top_n_by_index(filtered_df, 'Indeks Pendidikan', n=5)
top_kesehatan_df = top_n_by_index(filtered_df, 'Indeks Kesehatan', n=5)

# First row: Top Accumulative | Top Ekonomi
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(
        horizontal_bar(
            top_acc_df,
            title="Top 10 Kota dengan Indeks Terbaik",
            x_col='Indeks Accumulative',
            y_col='City',
            top=True
        ),
        use_container_width=True
    )
with col2:
    st.plotly_chart(
        horizontal_bar(
            top_ekonomi_df,
            title="Top 5 Kota - Indeks Ekonomi",
            x_col='Indeks Ekonomi',
            y_col='City',
            top=True
        ),
        use_container_width=True
    )

# Second row: Top Pendidikan | Top Kesehatan
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(
        horizontal_bar(
            top_pendidikan_df,
            title="Top 5 Kota - Indeks Pendidikan",
            x_col='Indeks Pendidikan',
            y_col='City',
            top=True
        ),
        use_container_width=True
    )
with col4:
    st.plotly_chart(
        horizontal_bar(
            top_kesehatan_df,
            title="Top 5 Kota - Indeks Kesehatan",
            x_col='Indeks Kesehatan',
            y_col='City',
            top=True
        ),
        use_container_width=True
    )

# -----------------------
# Bottom 5 Concern (Red Gradient)
# -----------------------
bottom_df = bottom_n_concern(filtered_df, n=5)
st.header("5 Kab/Kota yang perlu dikembangkan")
st.plotly_chart(
    horizontal_bar(
        bottom_df,
        title="Bottom 5 Cities - Accumulative Index",
        x_col='Indeks Accumulative',
        y_col='City',
        top=False  # Red gradient
    ),
    use_container_width=True
)

# -----------------------
# Cluster Distribution Pie Chart
# -----------------------
st.header("Distribusi Anggota Cluster")
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
