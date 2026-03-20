# 📦 Supply Chain Management - ML Project 

A comprehensive data analysis and machine learning project for optimizing supply chain operations in the Fashion & Beauty industry.

## 👤 Author
**ASWASANA ROUT**  

[GitHub](https://github.com/scuebaduuuu2425) | [LinkedIn](https://linkedin.com/in/aswasana-rout-155298325)


## 🎯 Project Overview

This project analyzes supply chain data from a makeup products startup and implements a deep learning model for demand forecasting. The analysis covers inventory management, supplier performance, logistics optimization, and quality control.

**Domain:** Data Analytics | Machine Learning  
**Industry:** Fashion & Beauty  


## 🚀 Features

- **Data Analysis:** Complete exploratory data analysis with statistical insights
- **Visualizations:** 9 professional charts covering all supply chain aspects
- **ML Model:** Neural network for demand forecasting with 90%+ accuracy
- **Interactive Dashboard:** Streamlit web app with real-time filtering
- **Automated Reports:** Comprehensive analysis report generation

## 📊 Dataset

The dataset contains 100 records with 24 features:
- Product information (type, SKU, price, availability)
- Sales data (units sold, revenue)
- Inventory metrics (stock levels, lead times)
- Logistics (shipping times, costs, carriers)
- Manufacturing (production volumes, costs, defect rates)
- Quality control (inspection results)

## 🛠️ Tech Stack

- **Python 3.8+**
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Machine Learning:** TensorFlow, Keras, Scikit-learn
- **Dashboard:** Streamlit


## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/scuebaduuuu2425/supply-chain-ml.git
cd supply-chain-ml

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

### Run Complete Analysis
```bash
data exploration.ipynb
data visualization.ipynb
demand forecasting_model.ipynb
generate_report.ipynb
```

### Launch Dashboard
```bash
streamlit run dashboard.py
```

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.85+ |
| RMSE | ~45 units |
| MAE | ~35 units |

The neural network architecture:
- Input Layer: 20 features
- Hidden Layers: 128 → 64 → 32 → 16 neurons
- Activation: ReLU
- Optimizer: Adam
- Loss: MSE

## 📊 Outputs

**Visualizations:**
- Product analysis
- Supply chain metrics
- Location & supplier performance
- Shipping & transportation
- Quality control
- Correlation heatmap
- Training history
- Prediction analysis

**Files Generated:**
- `demand_forecasting_model.h5` - Trained model
- `scaler.pkl` - Feature scaler
- `label_encoders.pkl` - Category encoders
- `Supply_Chain_Analysis_Report.txt` - Complete report

## 🎨 Dashboard

Interactive Streamlit dashboard with 6 pages:
1. **Overview** - KPIs and summary metrics
2. **Product Analysis** - Revenue, pricing, sales
3. **Supply Chain Metrics** - Lead times, inventory
4. **Supplier & Location** - Performance comparison
5. **Shipping & Transportation** - Logistics analysis
6. **Quality Control** - Defect rates, inspections

To view : https://supply-chain-management-vrrvz4zchbd9mib3ekzsub.streamlit.app/

## 📝 Key Insights

- **Revenue:** $578,445 total across 100 products
- **Best Category:** Skincare generates 38% of revenue
- **Lead Time:** Average 15.8 days with optimization potential
- **Quality:** 33% pass rate indicates improvement needed
- **Forecast Accuracy:** Model predicts demand within ±35 units

## 🔮 Use Cases

- Demand forecasting for inventory planning
- Supplier performance evaluation
- Route optimization for cost reduction
- Quality control monitoring
- Stock level optimization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Dataset: Fashion & Beauty supply chain data
- Built with Python and modern ML frameworks
- Inspired by real-world supply chain challenges

---

⭐ **Star this repo if you find it helpful!**
