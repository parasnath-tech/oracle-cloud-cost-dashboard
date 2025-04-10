import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Oracle Cloud Cost Optimizer",
    page_icon="https://photos.app.goo.gl/TdV5yxCzW8VSSwwm6",
    layout="wide"
)
st.image("https://logodix.com/logo/692804.png", width=400)

# Custom title
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>(💸Oracle Cloud Cost Optimization Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("📊 Real-time cost insights for Oracle Cloud Infrastructure")

with col2:
    st.image("https://www.tecnovait.com/wp-content/uploads/2023/11/oracle-servicio-cloud-en.png", width=80)


# Sidebar setup
#st.sidebar.title("📊 Project Navigator")
#st.sidebar.info("""
#Built by [Paras Nath](https://github.com/parasnath-tech)  
#This dashboard helps you monitor and optimize Oracle Cloud costs.
#""")
with st.expander("📘 About This Project", expanded=True):
    st.markdown("""
    This interactive dashboard helps track, analyze, and optimize Oracle Cloud Infrastructure (OCI) usage costs.  
    It’s built using **Python, Streamlit, and Plotly**, and integrates real usage data to generate insights and cost-saving opportunities.

    **Key Features:**
    - Cost breakdowns by service
    - Monthly spending trends
    - Recommendations for optimization
    - Easy-to-use filters and visuals
    """)
st.markdown("""
<a href="https://github.com/parasnath-tech/oracle-cloud-cost-dashboard" target="_blank">
    <img src="https://img.shields.io/badge/View%20on%20GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>
""", unsafe_allow_html=True)


# 🌗 Theme check
theme_base = st.get_option("theme.base")
is_dark = theme_base == "dark"

# 🎨 Custom Palettes
bar_colors = ['#f6f2ff', '#e8d9fc', '#dbbffc', '#cfa6f9', '#c28cf7', '#b572f5', '#a959f3', '#9c3ff1', '#9015ef', '#7b00d4']
pie_colors = ['#fff0f3', '#ffd3db', '#ffb6c2', '#ff99aa', '#ff7c91', '#ff5f79', '#ff4260', '#ff2548', '#ff082f', '#e60017']
# Scatter (Designer palette with contrast)
scatter_colors = [
    '#FFA07A', '#20B2AA', '#9370DB', '#3CB371', '#F08080',
    '#00BFFF', '#CD5C5C', '#4682B4', '#E9967A', '#7FFFD4']

# 🌟 Title
st.title("☁️ Oracle Cloud Cost Optimization Dashboard")
st.markdown("This dashboard presents cost-saving insights using resource-level metrics from Oracle Cloud.")

# 📂 File Upload
uploaded_file = st.file_uploader("📁 Upload your Oracle Cloud Cost CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df["Resource_ID"] = df["Resource_ID"].astype(str)

    # ✅ Sort properly by numeric part of Resource_ID
    df["Resource_Num"] = df["Resource_ID"].str.extract(r"(\d+)").astype(int)
    df = df.sort_values(by="Resource_Num").drop(columns="Resource_Num")

    underutilized = df[df["CPU_Utilization(%)"] < 30]

    # 🎛️ Dropdown
    resource_types = df["Resource_Type"].unique()
    selected_type = st.selectbox("🔍 Filter by Resource Type", options=["All"] + list(resource_types))

    if selected_type != "All":
        df = df[df["Resource_Type"] == selected_type]
        underutilized = underutilized[underutilized["Resource_Type"] == selected_type]

    # 📊 Bar Chart
    bar_fig = px.bar(df, x="Resource_Type", y="Cost_($)", color="Resource_Type",
                     color_discrete_sequence=bar_colors,
                     title="Cloud Cost Breakdown by Resource Type",
                     hover_data=["Resource_ID", "CPU_Utilization(%)", "Usage_Hours"])
    bar_fig.update_layout(height=350, margin=dict(t=40, b=20))

    # 📊 Pie Chart
    pie_df = df.groupby("Resource_Type")["Cost_($)"].sum().reset_index()
    pie_fig = px.pie(pie_df, names="Resource_Type", values="Cost_($)",
                     color_discrete_sequence=pie_colors,
                     title="Cloud Cost Distribution by Resource Type")
    pie_fig.update_traces(textinfo="percent+label", pull=0.03)
    pie_fig.update_layout(height=350, margin=dict(t=40, b=20))

    # 📊 Line Chart
    df_sorted = df.sort_values(by="Usage_Hours")
    line_fig = px.line(df_sorted, x="Usage_Hours", y="Cost_($)", markers=True,
                       title="Usage Hours vs. Cost Trend",
                       hover_data=["Resource_ID", "CPU_Utilization(%)"])
    line_fig.update_traces(marker=dict(size=8),
                           line=dict(color='royalblue'),
                           text=df_sorted["Resource_ID"],
                           textposition="top center",
                           mode="lines+markers+text")
    line_fig.update_layout(height=350, margin=dict(t=40, b=20),
                           xaxis_title="Usage Hours", yaxis_title="Cost ($)")

    # 📊 Scatter Plot
    scatter_fig = px.scatter(df, x="CPU_Utilization(%)", y="Cost_($)", size="Cost_($)",
                             color="Resource_Type", title="CPU Utilization vs. Cost Analysis",
                             hover_data=["Resource_ID", "Usage_Hours"],
                             color_discrete_sequence=scatter_colors)
    scatter_fig.add_vline(x=30, line_dash="dash", line_color="red",
                          annotation_text="Underutilized Threshold (30%)", annotation_position="top left")
    scatter_fig.update_layout(height=350, margin=dict(t=40, b=20))

    # 📈 Grid Layout
    st.markdown("## 📈 Visual Insights")
    col1, col2 = st.columns(2)
    with col1: st.plotly_chart(bar_fig, use_container_width=True)
    with col2: st.plotly_chart(pie_fig, use_container_width=True)
    col3, col4 = st.columns(2)
    with col3: st.plotly_chart(line_fig, use_container_width=True)
    with col4: st.plotly_chart(scatter_fig, use_container_width=True)

    # 📤 Download
    st.markdown("### 📤 Download Filtered Data")
    st.download_button("⬇️ Download Current View", data=df.to_csv(index=False),
                       file_name="filtered_cloud_cost.csv", mime="text/csv")

    # 📋 Full Table
    st.markdown("### 📊 Full Cost Breakdown Table")
    st.dataframe(df, use_container_width=True, height=300)

    # 🚀 Underutilized Table
    st.markdown("### 🚀 Underutilized Resources (CPU < 30%)")
    if not underutilized.empty:
        st.dataframe(underutilized, use_container_width=True, height=underutilized.shape[0]*35 + 35)
    else:
        st.success("✅ No underutilized resources found.")
else:
    st.warning("📂 Please upload your Oracle Cloud CSV file to view the dashboard.")
