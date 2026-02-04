# Travel Information Chatbot - Concise Documentation

## Quick Overview
Streamlit-based chatbot providing visa, currency, vaccination, insurance, emergency, and customs information for travel destinations.

## Quick Start
```bash
cd "Travel F&Q Chatbot"
pip install -r requirements.txt
streamlit run app.py
```
Access at `http://localhost:8501`

## Features
- 🛂 Visa requirements & application process
- 💱 Currency exchange rates (to INR)
- 💉 Vaccination requirements
- 🏥 Travel insurance plans
- 🚨 Emergency contacts
- 🏛️ Local customs & etiquette
- 🗣️ 8 language support (English, Hindi, French, German, Spanish, Italian, Japanese, Thai)

## Project Structure
```
Travel F&Q Chatbot/
├── app.py                  # Main application
├── requirements.txt        # Dependencies
├── README.md              # Main docs
├── data/                  # JSON data files
└── docs/                  # Documentation
    ├── ARCHITECTURE.md
    ├── WORKFLOW.md
    ├── INSTALLATION.md
    ├── QUICK_REFERENCE.md
    ├── DATA_DICTIONARY.md
    └── PROJECT_OVERVIEW.md
```

## Core Components

| Component | Details |
|-----------|---------|
| **UI** | Streamlit web interface with language selector & query input |
| **NLP** | Intent detection & country extraction from queries |
| **Data** | JSON files (destination, visa, currency, insurance) |
| **Translation** | Google Translate API for input/output |
| **Functions** | load_data(), detect_intent(), extract_country(), travel_bot() |

## Intent Types
| Intent | Keywords |
|--------|----------|
| visa | "visa" |
| currency | "currency", "exchange", "rate" |
| insurance | "insurance" |
| vaccination | "vaccination", "vaccine" |
| emergency | "emergency", "ambulance", "police" |
| customs | "customs", "culture", "etiquette" |

## Key Functions
- `load_data()` - Load JSON files with caching
- `detect_intent(query)` - Identify what user is asking
- `extract_country(query)` - Find destination country
- `translate_text(text, lang)` - Translate response
- `travel_bot(query)` - Main logic

## Installation
See `docs/INSTALLATION.md` for detailed setup

## Usage
1. Select language from dropdown
2. Enter travel question
3. Click Ask
4. View response in selected language

## Tech Stack
- **Framework**: Streamlit
- **Language**: Python 3.7+
- **Translation**: deep-translator (Google Translate)
- **Data**: JSON files

## Documentation
- **ARCHITECTURE.md** - System design
- **WORKFLOW.md** - Request processing
- **INSTALLATION.md** - Setup guide
- **QUICK_REFERENCE.md** - Quick lookup
- **DATA_DICTIONARY.md** - Data schemas
- **PROJECT_OVERVIEW.md** - Visual guide

## Example Queries
- "Visa for France?"
- "Currency exchange in Japan"
- "Travel insurance and vaccination for Thailand"
- "Emergency contacts in Germany"

## Performance
- Data load: 50-100ms
- Intent detection: 1-2ms
- Total response: 150-600ms (with translation)

## Troubleshooting
- **Import error**: `pip install -r requirements.txt`
- **Data files not found**: Check data/ folder exists
- **Translation not working**: Ensure internet connection
- **Port in use**: `streamlit run app.py --server.port 8502`

## License
MIT Open Source

---
For detailed documentation, see individual files in docs/ folder.
