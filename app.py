import streamlit as st
from dataset_handler import load_and_preprocess
from insights import top_n_by_cluster, bottom_n_concern, cluster_distribution
from insights import horizontal_bar, pie_chart, pca_3d

# -----------------------
# Streamlit Settings
# -----------------------
st.set_page_config(page_title="City Index Dashboard", layout="wide")
st.title("City Index Dashboard")

# -----------------------
# Load Data
# -----------------------
df = load_and_preprocess("data/dataset.csv")

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
# Top 3 by Cluster (Blue Gradient)
# -----------------------
st.header("Top 3 Indices by Cluster")
top_data = top_n_by_cluster(filtered_df)

for cluster, metrics in sorted(top_data.items(), reverse=True):
    st.subheader(f"Cluster {cluster}")
    
    # Side-by-side layout for all metrics
    cols = st.columns(len(metrics))
    for i, (metric_name, metric_df) in enumerate(metrics.items()):
        with cols[i]:
            st.plotly_chart(
                horizontal_bar(
                    metric_df,
                    title=f"Top 3 {metric_name}",
                    x_col=metric_name,
                    y_col='City',
                    color_scale='Blues'
                ),
                use_container_width=True
            )

# -----------------------
# Bottom 5 Concern (Red Gradient)
# -----------------------
st.header("Bottom 5 Concern (Lowest Accumulative Index)")
bottom_df = bottom_n_concern(filtered_df)
st.plotly_chart(
    horizontal_bar(
        bottom_df,
        title="Bottom 5 Cities",
        x_col='Indeks Accumulative',
        y_col='City',
        color_scale='Reds_r'  # reversed red so lowest values are darkest
    ),
    use_container_width=True
)

# -----------------------
# Cluster Distribution Pie Chart
# -----------------------
st.header("Cluster Members Distribution")
distribution = cluster_distribution(filtered_df)
st.plotly_chart(
    pie_chart(distribution, title="Cluster Members"),
    use_container_width=True
)

# -----------------------
# 3D PCA Projection
# -----------------------
st.header("3D PCA Projection of Cities")
st.plotly_chart(
    pca_3d(filtered_df),
    use_container_width=True
)
