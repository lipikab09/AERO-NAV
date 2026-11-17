import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="AERO-NAV AI Dashboard", layout="wide")
st.title("🚁 AERO-NAV AI Command Center")

col1, col2, col3 = st.columns(3)
col1.metric("SLAM Status", "Active", "Locked")
col2.metric("GPS Signal", "DENIED", "0 Sats")
col3.metric("Epistemic Uncertainty", "0.14", "Normal")

t = np.linspace(0, 20, 200)
fig = go.Figure(data=[go.Scatter3d(x=np.sin(t)*10, y=np.cos(t)*10, z=t*0.5, mode='lines+markers')])
st.plotly_chart(fig, use_container_width=True)
