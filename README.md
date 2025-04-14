# ☁️ Oracle Cloud Cost Optimization Dashboard 💸

[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parasnath-tech/oracle-cloud-cost-dashboard)

🔗 **Live Demo**: [oracle-cloud-cost-dashboard.streamlit.app](https://oracle-cloud-cost-dashboard.streamlit.app/)

---

## 📘 About This Project

This interactive dashboard helps track, analyze, and optimize Oracle Cloud Infrastructure (OCI) usage costs.  
Built using **Python**, **Streamlit**, and **Plotly**, it integrates real usage data to generate actionable insights and cost-saving opportunities.

---

## 📊 Features

- 🔍 **Cost Breakdown by Resource Type**
- 📈 **Monthly Spending Trends**
- 📉 **Usage vs. Cost Analysis**
- 🚀 **Underutilized Resource Detection (CPU < 30%)**
- 📤 **Downloadable Filtered Dataset**
- 🎛️ **Real-Time Filtering by Resource Type**
- 📋 **Tabular View with Insights**
- ☁️ **Hosted on Streamlit Cloud**

---

## 🧪 Tech Stack

- **Language**: Python
- **Framework**: Streamlit
- **Visualization**: Plotly Express
- **Libraries**:
  - `streamlit`
  - `pandas`
  - `plotly.express`

---

## 📁 Sample Dataset (CSV Format)

| Resource_ID | Resource_Type | Usage_Hours | Cost_($) | CPU_Utilization(%) | Instance_Count | Instance_Type |
|-------------|----------------|-------------|----------|---------------------|----------------|----------------|
| R123        | Compute        | 120         | 50       | 18                  | 1              | VM.Standard2.1 |

_You can upload your own CSV in the same format using the dashboard interface._

---

## 🔍 Dashboard Sections

### 📈 Visual Insights

- **Bar Chart**: Cost breakdown by resource type
- **Pie Chart**: Cost distribution by category
- **Line Chart**: Usage hours vs. cost trends
- **Scatter Plot**: CPU Utilization vs. Cost (highlights underutilization)

### 🚀 Underutilized Resources

- Automatically flags any instance with **CPU Utilization < 30%**

### 📤 Data Download

- Download filtered datasets based on applied dashboard filters.

### 📋 Complete Data Table

- Scrollable, interactive table showing full cost breakdown.

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/parasnath-tech/oracle-cloud-cost-dashboard.git
cd oracle-cloud-cost-dashboard
pip install -r requirements.txt
streamlit run app.py
``````

🤝 Contribution
Open to feedback, suggestions, or pull requests. Just fork the repo and contribute!

---

🧠 Creator
Built with ❤️ by Paras Nath
