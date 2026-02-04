# Project Overview 

## What is This?

Travel Information Chatbot - A Streamlit web app that provides visa, currency, insurance, vaccination, emergency, and customs info for travelers.

## Features

```
🛂 Visa Requirements    💱 Currency Exchange
💉 Vaccination Info      🏥 Travel Insurance  
🚨 Emergency Contacts    🏛️ Local Customs
🗣️ 8 Language Support
```

## Quick Start

```bash
cd "Travel F&Q Chatbot"
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501`

## How It Works

```
User Input (Any Language)
    ↓
Translate to English
    ↓
Detect Intent (Visa? Currency? Etc.)
    ↓
Extract Country Name
    ↓
Fetch Relevant Data
    ↓
Translate to Selected Language
    ↓
Display Response
```

## Example Queries

- "What is visa for France?"
- "Currency exchange for Japan"
- "Insurance and vaccination for Thailand"
- "Emergency contacts in Germany"
- "Local customs in Italy"

Or in other languages:
- Hindi: "फ्रांस के लिए वीजा क्या है?"
- French: "Quel est le visa pour la France?"

## Project Structure

```
Travel F&Q Chatbot/
├── app.py                    # Main app (247 lines)
├── requirements.txt          # Dependencies
├── README.md                 # Main docs
├── data/                     # Data files
│   ├── destination.json
│   ├── VisaChecker.json
│   ├── CurrencyExchange.json
│   └── TravelInsaurance.json
└── docs/                     # Documentation
    ├── README_CONCISE.md
    ├── ARCHITECTURE_CONCISE.md
    ├── WORKFLOW_CONCISE.md
    ├── INSTALLATION_CONCISE.md
    ├── DATA_DICTIONARY_CONCISE.md
    ├── QUICK_REFERENCE.md
    └── PROJECT_OVERVIEW.md
```

## Key Components

| Component | Role |
|-----------|------|
| **UI** | Streamlit interface |
| **NLP** | Intent detection, entity extraction |
| **Logic** | Response generation |
| **Data** | JSON files (destination, visa, currency, insurance) |
| **Translation** | Google Translate API |

## System Layers

```
Presentation (Streamlit UI)
    ↓
Translation Layer
    ↓
NLP Layer
    ↓
Business Logic
    ↓
Data Access
    ↓
Storage (JSON Files)
```

## Intent Types

| Intent | Keywords |
|--------|----------|
| Visa | "visa" |
| Currency | "currency", "exchange", "rate" |
| Insurance | "insurance" |
| Vaccination | "vaccination", "vaccine" |
| Emergency | "emergency", "ambulance", "police" |
| Customs | "customs", "culture", "etiquette" |

## Data Files

| File | Size | Contains |
|------|------|----------|
| destination.json | ~500 KB | Country info |
| VisaChecker.json | ~200 KB | Visa rules |
| CurrencyExchange.json | ~50 KB | Exchange rates |
| TravelInsaurance.json | ~30 KB | Insurance plans |

## Languages Supported

English, Hindi, French, German, Spanish, Italian, Japanese, Thai

## Tech Stack

- **Framework**: Streamlit
- **Language**: Python 3.7+
- **Translation**: deep-translator
- **Data**: JSON
- **Caching**: Streamlit native

## Performance

- Data load: 50-100ms
- Intent detection: 1-2ms
- Total response: 150-600ms (with translation)

## Key Files in Code

- `app.py`: Main application with UI and logic
- `load_data()`: Load JSON files with caching
- `detect_intent()`: Find what user is asking
- `extract_country()`: Find destination
- `travel_bot()`: Main response generation

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Import errors | `pip install -r requirements.txt` |
| Data files missing | Check data/ folder |
| Translation not working | Check internet connection |
| Port in use | `streamlit run app.py --server.port 8502` |
| Country not recognized | Check spelling/use alias |

## Quick Links

- **Setup**: See INSTALLATION_CONCISE.md
- **How it works**: See WORKFLOW_CONCISE.md
- **System design**: See ARCHITECTURE_CONCISE.md
- **Data format**: See DATA_DICTIONARY_CONCISE.md
- **Quick reference**: See QUICK_REFERENCE.md

## Next Steps

1. Install: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`
3. Try queries in the web interface
4. Read docs for deeper understanding

---

**For more details, see documentation files in docs/ folder**
