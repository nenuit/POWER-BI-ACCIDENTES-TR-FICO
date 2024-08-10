import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
    <style>
    .report-container {
        width: 100vw; /* Ensure full width */
        height: 100vh; /* Full viewport height */
        border: none; /* Optional: Removes the border */
        overflow: hidden; /* Optional: Removes scrollbars */
    }
    iframe {
        width: 100%;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("POWER BI Accidentes de Tráfico")
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDk5NmMzYjgtZTY0OC00ZjYyLTlhYmItNmY3YTQ4YTQwNzM5IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
components.html(f'<iframe class="report-container" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>')
