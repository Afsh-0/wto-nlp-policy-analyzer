# WTO NLP Policy Analyzer

An end-to-end Natural Language Processing (NLP) system that analyzes World Trade Organization (WTO) policy documents and classifies them into meaningful policy categories such as tariffs, imports, exports, investment, and regulations.

## Overview

Global trade policies are complex and lengthy, making manual analysis time-consuming.
This project builds an automated pipeline that:

* Extracts text from WTO policy reports (PDF)
* Cleans and processes the text

## Features

**PDF Text Extraction** – Reads WTO reports directly
**Text Preprocessing** – Cleans and normalizes raw text
**Chunking** – Splits large documents into smaller segments
**Policy Classification** – Categorizes text into:

  * Tariff
  * Import
  * Export
  * Investment
  * Policy

## Project Structure

```
WTO_NLP_Policy_Analyzer/
│
├── data/                  
├── src/                
│   ├── extract.py     
│   ├── preprocess.py     
│   ├── insights.py        
│   ├── nlp_pipeline.py          
│   └── visulaization.py                       
├── main.py               
├── requirements.txt     
└── README.md              


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/wto-nlp-policy-analyzer.git
cd wto-nlp-policy-analyzer
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the full pipeline:

```bash
python main.py
```
