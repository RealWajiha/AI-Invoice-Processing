# AI-Invoice-Processing
# Demo Link
https://wajiha-ai-invoice-processing.streamlit.app/
An AI-powered invoice extraction and expense logging engine built with n8n, OpenAI (GPT-4o-Mini), Google Sheets, and a vibrant Streamlit dashboard.
# 🧾 AI Invoice Processing Studio

An automated, end-to-end invoice data extraction and expense management system powered by **n8n**, **OpenAI (GPT-4o-Mini)**, **Google Sheets API**, and an interactive **Streamlit** frontend.

![Python](https://img.shields.io/badge/Python-3.10+-FF007A?style=for-the-badge&logo=python&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-Automation-FF4500?style=for-the-badge&logo=n8n&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--Mini-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## ⚡ Key Features

- 📄 **Raw Invoice Parsing:** Extract vendor names, invoice numbers, totals, tax amounts, and categories from plain text or receipts.
- 🛒 **Line Item Breakdown:** Structured breakdown of individual items, quantities, and pricing.
- 📊 **Google Sheets Auto-Sync:** Automated appending of processed expenses directly to Google Sheets database.
- 🎨 **Vibrant UI Dashboard:** Custom-built bright pop theme in Streamlit for seamless user input and real-time AI JSON metrics visualization.
- 🔄 **n8n Webhook Architecture:** Asynchronous production workflow triggered via Webhook payloads.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit, Custom CSS
- **Workflow Automation:** n8n Cloud / Self-hosted
- **AI Model:** OpenAI (`gpt-4o-mini` with Structured Outputs)
- **Database/Logging:** Google Sheets API

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone [https://github.com/RealWajiha/AI-Invoice-Processing-Studio.git](https://github.com/RealWajiha/AI-Invoice-Processing-Studio.git)
cd AI-Invoice-Processing-Studio
