import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Oracle Cost Charts Only", page_icon="📊", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>☁️ Oracle Cloud Cost Charts 💹</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load default data
df = pd.read_csv("default_cost_data.csv")
df["Resource_ID"] = df["Resource_ID"].astype(str)
df["Resource_Num"] = df["Resource_ID"].str.extract(r"(\d+)").astype(int)
df = df.sort_values(by="Resource_Num").drop(columns="Resource_Num")
underutilized = df[df["CPU_Utilization(%)"] < 30]

# Color palettes
bar_colors = ['#f6f2ff', '#e8d9fc', '#dbbffc', '#cfa6f9', '#c28cf7', '#b572f5', '#a959f3', '#9c3ff1', '#9015ef', '#7b00d4']
pie_colors = ['#fff0f3', '#ffd3db', '#ffb6c2', '#ff99aa', '#ff7c91', '#ff5f79', '#ff4260', '#ff2548', '#ff082f', '#e60017']
scatter_colors = ['#FFA07A', '#20B2AA', '#9370DB', '#3CB371', '#F08080', '#00BFFF', '#CD5C5C', '#4682B4', '#E9967A', '#7FFFD4']

# Charts
bar_fig = px.bar(df, x="Resource_Type", y="Cost_($)", color="Resource_Type",
                 color_discrete_sequence=bar_colors,
                 title="Cloud Cost Breakdown by Resource Type",
                 hover_data=["Resource_ID", "CPU_Utilization(%)", "Usage_Hours"])
bar_fig.update_layout(height=350, margin=dict(t=40, b=20))

pie_df = df.groupby("Resource_Type")["Cost_($)"].sum().reset_index()
pie_fig = px.pie(pie_df, names="Resource_Type", values="Cost_($)",
                 color_discrete_sequence=pie_colors,
                 title="Cloud Cost Distribution by Resource Type")
pie_fig.update_traces(textinfo="percent+label", pull=0.03)
pie_fig.update_layout(height=350, margin=dict(t=40, b=20))

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

scatter_fig = px.scatter(df, x="CPU_Utilization(%)", y="Cost_($)", size="Cost_($)",
                         color="Resource_Type", title="CPU Utilization vs. Cost Analysis",
                         hover_data=["Resource_ID", "Usage_Hours"],
                         color_discrete_sequence=scatter_colors)
scatter_fig.add_vline(x=30, line_dash="dash", line_color="red",
                      annotation_text="Underutilized Threshold (30%)", annotation_position="top left")
scatter_fig.update_layout(height=350, margin=dict(t=40, b=20))

# Layout
st.markdown("## 📊 Oracle Cloud Visuals")
col1, col2 = st.columns(2)
with col1: st.plotly_chart(bar_fig, use_container_width=True)
with col2: st.plotly_chart(pie_fig, use_container_width=True)
col3, col4 = st.columns(2)
with col3: st.plotly_chart(line_fig, use_container_width=True)
with col4: st.plotly_chart(scatter_fig, use_container_width=True)

# Underutilized Resources
st.markdown("### 🚀 Underutilized Resources (CPU < 30%)")
if not underutilized.empty:
    st.dataframe(underutilized, use_container_width=True, height=underutilized.shape[0]*35 + 35)
else:
    st.success("✅ No underutilized resources found.")
