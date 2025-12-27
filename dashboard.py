import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Supply Chain Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1e3a8a;
        font-weight: 700;
    }
    h2 {
        color: #2563eb;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('supply_chain_data.csv')
    return df

df = load_data()

# Sidebar
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["Overview", "Product Analysis", "Supply Chain Metrics", 
     "Supplier & Location", "Shipping & Transportation", "Quality Control"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")

# Filters
selected_product_type = st.sidebar.multiselect(
    "Product Type:",
    options=df['Product type'].unique(),
    default=df['Product type'].unique()
)

selected_location = st.sidebar.multiselect(
    "Location:",
    options=df['Location'].unique(),
    default=df['Location'].unique()
)

# Filter data
df_filtered = df[
    (df['Product type'].isin(selected_product_type)) &
    (df['Location'].isin(selected_location))
]

# Main content
st.title("📦 Supply Chain Management Dashboard")
st.markdown("**Real-time insights into supply chain operations**")
st.markdown("---")

if page == "Overview":
    st.header("📈 Overview & Key Metrics")
    
    # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_revenue = df_filtered['Revenue generated'].sum()
        st.metric("Total Revenue", f"${total_revenue:,.0f}")
    
    with col2:
        total_products_sold = df_filtered['Number of products sold'].sum()
        st.metric("Products Sold", f"{total_products_sold:,}")
    
    with col3:
        avg_price = df_filtered['Price'].mean()
        st.metric("Avg Price", f"${avg_price:.2f}")
    
    with col4:
        avg_lead_time = df_filtered['Lead times'].mean()
        st.metric("Avg Lead Time", f"{avg_lead_time:.1f} days")
    
    with col5:
        total_stock = df_filtered['Stock levels'].sum()
        st.metric("Total Stock", f"{total_stock:,}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue by product type
        revenue_by_product = df_filtered.groupby('Product type')['Revenue generated'].sum().reset_index()
        fig1 = px.bar(
            revenue_by_product,
            x='Product type',
            y='Revenue generated',
            title='Revenue by Product Type',
            color='Product type',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig1.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Products sold by location
        products_by_location = df_filtered.groupby('Location')['Number of products sold'].sum().reset_index()
        fig2 = px.pie(
            products_by_location,
            values='Number of products sold',
            names='Location',
            title='Products Sold by Location',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Distribution charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig3 = px.histogram(
            df_filtered,
            x='Stock levels',
            nbins=30,
            title='Stock Levels Distribution',
            color_discrete_sequence=['#3b82f6']
        )
        fig3.update_layout(height=350)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        fig4 = px.histogram(
            df_filtered,
            x='Lead times',
            nbins=30,
            title='Lead Times Distribution',
            color_discrete_sequence=['#10b981']
        )
        fig4.update_layout(height=350)
        st.plotly_chart(fig4, use_container_width=True)

elif page == "Product Analysis":
    st.header("🛍️ Product Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Average price by product type
        avg_price_product = df_filtered.groupby('Product type')['Price'].mean().reset_index()
        fig = px.bar(
            avg_price_product,
            x='Product type',
            y='Price',
            title='Average Price by Product Type',
            color='Product type',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Availability by product type
        avg_availability = df_filtered.groupby('Product type')['Availability'].mean().reset_index()
        fig = px.bar(
            avg_availability,
            x='Product type',
            y='Availability',
            title='Average Availability by Product Type',
            color='Product type',
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Price vs Revenue scatter
    fig = px.scatter(
        df_filtered,
        x='Price',
        y='Revenue generated',
        color='Product type',
        size='Number of products sold',
        title='Price vs Revenue (size = products sold)',
        hover_data=['SKU']
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Top products table
    st.subheader("Top 10 Products by Revenue")
    top_products = df_filtered.nlargest(10, 'Revenue generated')[
        ['SKU', 'Product type', 'Price', 'Number of products sold', 'Revenue generated']
    ]
    st.dataframe(top_products, use_container_width=True)

elif page == "Supply Chain Metrics":
    st.header("⚙️ Supply Chain Metrics")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_order_qty = df_filtered['Order quantities'].mean()
        st.metric("Avg Order Quantity", f"{avg_order_qty:.0f}")
    
    with col2:
        avg_ship_time = df_filtered['Shipping times'].mean()
        st.metric("Avg Shipping Time", f"{avg_ship_time:.1f} days")
    
    with col3:
        avg_ship_cost = df_filtered['Shipping costs'].mean()
        st.metric("Avg Shipping Cost", f"${avg_ship_cost:.2f}")
    
    with col4:
        avg_mfg_lead = df_filtered['Manufacturing lead time'].mean()
        st.metric("Avg Mfg Lead Time", f"{avg_mfg_lead:.1f} days")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.box(
            df_filtered,
            x='Product type',
            y='Lead times',
            title='Lead Times by Product Type',
            color='Product type'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(
            df_filtered,
            x='Product type',
            y='Order quantities',
            title='Order Quantities by Product Type',
            color='Product type'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap
    numeric_cols = ['Price', 'Stock levels', 'Lead times', 'Order quantities', 
                   'Shipping times', 'Production volumes', 'Manufacturing costs']
    corr_matrix = df_filtered[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0
    ))
    fig.update_layout(title='Correlation Heatmap', height=500)
    st.plotly_chart(fig, use_container_width=True)

elif page == "Supplier & Location":
    st.header("🏭 Supplier & Location Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue by supplier
        revenue_supplier = df_filtered.groupby('Supplier name')['Revenue generated'].sum().reset_index()
        fig = px.bar(
            revenue_supplier,
            x='Supplier name',
            y='Revenue generated',
            title='Revenue by Supplier',
            color='Supplier name'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Production by location
        prod_location = df_filtered.groupby('Location')['Production volumes'].sum().reset_index()
        fig = px.bar(
            prod_location,
            x='Location',
            y='Production volumes',
            title='Production Volumes by Location',
            color='Location'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Manufacturing costs by supplier
    fig = px.box(
        df_filtered,
        x='Supplier name',
        y='Manufacturing costs',
        title='Manufacturing Costs Distribution by Supplier',
        color='Supplier name'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Location performance table
    st.subheader("Location Performance Summary")
    location_summary = df_filtered.groupby('Location').agg({
        'Revenue generated': 'sum',
        'Number of products sold': 'sum',
        'Production volumes': 'sum',
        'Manufacturing costs': 'mean',
        'Lead times': 'mean'
    }).round(2)
    st.dataframe(location_summary, use_container_width=True)

elif page == "Shipping & Transportation":
    st.header("🚚 Shipping & Transportation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carrier distribution
        carrier_dist = df_filtered['Shipping carriers'].value_counts().reset_index()
        carrier_dist.columns = ['Carrier', 'Count']
        fig = px.pie(
            carrier_dist,
            values='Count',
            names='Carrier',
            title='Shipping Carrier Distribution'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Transportation mode
        transport_dist = df_filtered['Transportation modes'].value_counts().reset_index()
        transport_dist.columns = ['Mode', 'Count']
        fig = px.pie(
            transport_dist,
            values='Count',
            names='Mode',
            title='Transportation Mode Distribution'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Shipping costs by carrier
    fig = px.box(
        df_filtered,
        x='Shipping carriers',
        y='Shipping costs',
        title='Shipping Costs by Carrier',
        color='Shipping carriers'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Routes analysis
    col1, col2 = st.columns(2)
    
    with col1:
        route_counts = df_filtered['Routes'].value_counts().reset_index()
        route_counts.columns = ['Route', 'Count']
        fig = px.bar(
            route_counts,
            x='Route',
            y='Count',
            title='Route Distribution',
            color='Route'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        avg_cost_route = df_filtered.groupby('Routes')['Costs'].mean().reset_index()
        fig = px.bar(
            avg_cost_route,
            x='Routes',
            y='Costs',
            title='Average Transportation Cost by Route',
            color='Routes'
        )
        st.plotly_chart(fig, use_container_width=True)

elif page == "Quality Control":
    st.header("✅ Quality Control")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pass_rate = (df_filtered['Inspection results'] == 'Pass').sum() / len(df_filtered) * 100
        st.metric("Pass Rate", f"{pass_rate:.1f}%")
    
    with col2:
        avg_defect = df_filtered['Defect rates'].mean()
        st.metric("Avg Defect Rate", f"{avg_defect:.2f}%")
    
    with col3:
        pending_count = (df_filtered['Inspection results'] == 'Pending').sum()
        st.metric("Pending Inspections", f"{pending_count}")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        inspection_dist = df_filtered['Inspection results'].value_counts().reset_index()
        inspection_dist.columns = ['Result', 'Count']
        fig = px.pie(
            inspection_dist,
            values='Count',
            names='Result',
            title='Inspection Results Distribution',
            color='Result',
            color_discrete_map={'Pass': '#10b981', 'Fail': '#ef4444', 'Pending': '#f59e0b'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.histogram(
            df_filtered,
            x='Defect rates',
            nbins=30,
            title='Defect Rates Distribution',
            color_discrete_sequence=['#ef4444']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Defect rates by product type
    fig = px.box(
        df_filtered,
        x='Product type',
        y='Defect rates',
        title='Defect Rates by Product Type',
        color='Product type'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Quality summary table
    st.subheader("Quality Summary by Product Type")
    quality_summary = df_filtered.groupby('Product type').agg({
        'Defect rates': ['mean', 'min', 'max'],
        'Inspection results': lambda x: (x == 'Pass').sum() / len(x) * 100
    }).round(2)
    quality_summary.columns = ['Avg Defect Rate', 'Min Defect Rate', 'Max Defect Rate', 'Pass Rate (%)']
    st.dataframe(quality_summary, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Supply Chain Management Dashboard** | Built with Streamlit & Plotly")
st.markdown(f"**Data Points:** {len(df_filtered)} | **Last Updated:** 2025")