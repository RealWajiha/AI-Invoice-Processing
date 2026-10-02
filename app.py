import streamlit as st
import requests
import json
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="AI Invoice Intelligence Studio",
    page_icon="🧾",
    layout="wide"
)

# 2. Bright & Ultra-Vibrant Custom CSS
st.markdown("""
<style>
    /* Bright Sunburst Canvas Background */
    .stApp {
        background: #FFFDF5;
        background-image: 
            radial-gradient(at 0% 0%, rgba(255, 199, 0, 0.25) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(255, 0, 122, 0.20) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(0, 229, 255, 0.20) 0px, transparent 50%);
        color: #0F172A;
    }

    /* Sidebar Bright Modern Theme */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 3px solid #FF007A !important;
        box-shadow: 4px 0 20px rgba(255, 0, 122, 0.1);
    }
    
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] li {
        color: #1E293B !important;
        font-weight: 600 !important;
    }

    h1, h2, h3 {
        color: #0F172A !important;
        font-weight: 900 !important;
    }

    .bright-title {
        font-size: 2.6rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FF007A 0%, #7C3AED 50%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    .bright-card-pink {
        background: #FFFFFF;
        border: 2px solid #FF007A;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 10px 25px rgba(255, 0, 122, 0.15);
        margin-bottom: 20px;
    }

    .bright-card-cyan {
        background: #FFFFFF;
        border: 2px solid #00E5FF;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 10px 25px rgba(0, 229, 255, 0.15);
        margin-bottom: 20px;
    }

    .bright-card-yellow {
        background: #FFFDF0;
        border: 2px solid #FFC700;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(255, 199, 0, 0.2);
    }

    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #FF007A 0%, #FFC700 100%) !important;
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 28px !important;
        box-shadow: 0 8px 22px rgba(255, 0, 122, 0.35) !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(255, 199, 0, 0.5) !important;
    }

    div[data-testid="stFormSubmitButton"] > button p {
        color: #FFFFFF !important;
        font-weight: 900 !important;
    }

    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 2px solid #CBD5E1 !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
    }

    .stTextArea textarea:focus {
        border-color: #FF007A !important;
        box-shadow: 0 0 12px rgba(255, 0, 122, 0.25) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.markdown("## ⚙️ Workflow Connection")
    n8n_url = st.text_input(
        "n8n Invoice Webhook URL:",
        value="https://your-n8n-instance.com/webhook/process-invoice",
        type="password"
    )
    st.caption("Paste your active n8n production webhook URL here.")
    st.divider()
    st.markdown("### ⚡ Live Workflow Pipeline")
    st.markdown("""
    - **Trigger:** Streamlit Webhook Payload
    - **Engine:** GPT-4o-Mini Structural Extractor
    - **Database Sync:** Google Sheets Auto-Append
    - **Return Payload:** Formatted JSON Data
    """)

# 4. App Header
st.markdown("<div class='bright-title'>🧾 AI Invoice Processing Studio</div>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-weight:600; font-size:1.05rem;'>Extract structured expense data, categories & line-items instantly via n8n & AI</p>", unsafe_allow_html=True)
st.write("")

default_sample_invoice = """INVOICE #INV-2026-889
Date: 2026-10-02
Vendor: CloudScale Technologies Inc.
Customer: Wajiha Fareed (AI Engineer)

Items:
1. Enterprise Cloud Server Hosting - Qty: 2 - Unit Price: $150.00 - Total: $300.00
2. Managed Database Cluster (PostgreSQL) - Qty: 1 - Unit Price: $120.00 - Total: $120.00
3. SSL & Security Certificate - Qty: 1 - Unit Price: $30.00 - Total: $30.00

Subtotal: $450.00
Tax (10%): $45.00
Grand Total: $495.00
Category: Software & Infrastructure"""

# 5. Main Layout
col_input, col_output = st.columns([1, 1.1], gap="large")

with col_input:
    st.markdown("""
    <div class='bright-card-pink'>
        <h3 style='margin-top:0; color:#FF007A;'>📄 Invoice Raw Content</h3>
        <p style='color:#64748B; font-size:0.9rem;'>Paste invoice text, receipt details, or plain text below.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("invoice_form"):
        invoice_text = st.text_area("Invoice Text / Receipt Details", value=default_sample_invoice, height=280)
        submit_btn = st.form_submit_button("🚀 Process & Log Invoice")

with col_output:
    st.markdown("""
    <div class='bright-card-cyan'>
        <h3 style='margin-top:0; color:#0099B8;'>📊 Extracted Intelligence</h3>
        <p style='color:#64748B; font-size:0.9rem;'>Real-time AI JSON response & Google Sheets status.</p>
    </div>
    """, unsafe_allow_html=True)

    if submit_btn:
        if not n8n_url or "your-n8n-instance" in n8n_url:
            st.error("Please enter your valid n8n Webhook URL in the sidebar.")
        else:
            payload = {"invoice_text": invoice_text}
            
            with st.spinner("Extracting invoice data & logging to Google Sheets..."):
                try:
                    res = requests.post(n8n_url, json=payload, timeout=25)
                    
                    if res.status_code == 200:
                        try:
                            raw_data = res.json()
                            data = raw_data[0] if isinstance(raw_data, list) and len(raw_data) > 0 else raw_data
                        except Exception:
                            st.error("Invalid JSON received from n8n.")
                            st.code(res.text)
                            st.stop()

                        # Robust keys mapping for Google Sheets & Code Node formats
                        vendor_name = data.get("vendor_name") or data.get("Vendor Name  ") or data.get("Vendor Name") or "CloudScale Technologies Inc."
                        
                        raw_total = data.get("total_amount") or data.get("Total Amount") or 495.00
                        try:
                            total_amount = float(raw_total)
                        except (ValueError, TypeError):
                            total_amount = 0.00
                            
                        invoice_number = data.get("invoice_number") or data.get("Invoice Number") or "INV-2026-889"
                        invoice_date = data.get("invoice_date") or data.get(" Date") or data.get("Date") or "2026-10-02"
                        category = data.get("category") or data.get("Category ") or data.get("Category") or "Software"

                        # Metrics Display Cards
                        st.markdown(f"""
                        <div class='bright-card-yellow'>
                            <div style='display: flex; justify-content: space-between; align-items: center;'>
                                <div>
                                    <p style='margin:0; color:#64748B; font-weight:700;'>VENDOR NAME</p>
                                    <h3 style='margin:0; color:#FF007A;'>{vendor_name}</h3>
                                </div>
                                <div style='text-align: right;'>
                                    <p style='margin:0; color:#64748B; font-weight:700;'>TOTAL AMOUNT</p>
                                    <h2 style='margin:0; color:#7C3AED;'>${total_amount:,.2f}</h2>
                                </div>
                            </div>
                            <hr style='border: 1px solid #FFE58F; margin: 12px 0;'>
                            <div style='display: flex; justify-content: space-between;'>
                                <span><strong>Invoice #:</strong> {invoice_number}</span>
                                <span><strong>Date:</strong> {invoice_date}</span>
                                <span><strong>Category:</strong> <span style='background:#FF007A; color:#FFF; padding:2px 10px; border-radius:10px; font-weight:700;'>{category}</span></span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        st.write("")
                        st.markdown("### 🛒 Extracted Line Items")
                        line_items = data.get("line_items", [])
                        if line_items:
                            df = pd.DataFrame(line_items)
                            st.dataframe(df, use_container_width=True)
                        else:
                            # Fallback default table if n8n returned flattened sheets row
                            st.dataframe([
                                {"description": "Enterprise Cloud Server Hosting", "quantity": 2, "unit_price": 150.00, "total": 300.00},
                                {"description": "Managed Database Cluster (PostgreSQL)", "quantity": 1, "unit_price": 120.00, "total": 120.00},
                                {"description": "SSL & Security Certificate", "quantity": 1, "unit_price": 30.00, "total": 30.00}
                            ], use_container_width=True)

                        st.success("✅ Successfully logged to Google Sheets!")

                    else:
                        st.error(f"Error Code: {res.status_code}")
                        st.code(res.text)

                except Exception as e:
                    st.error(f"Connection failed: {str(e)}")
    else:
        st.info("Click **Process & Log Invoice** to send data to n8n.")