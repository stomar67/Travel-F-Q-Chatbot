# Quick Reference Guide - Travel Information Chatbot

## Project Overview at a Glance

**Travel Information Chatbot** is a Python-based web application that provides comprehensive travel information including visa requirements, currency exchange, insurance, vaccination, emergency contacts, and local customs for travelers.

| Aspect | Details |
|--------|---------|
| **Type** | Streamlit Web Application |
| **Language** | Python 3.7+ |
| **Purpose** | Travel Information Assistant |
| **Users** | Travel Planning & Information Seekers |
| **Status** | Active |

## Quick Start (2 Minutes)

### Installation
```bash
cd "Travel F&Q Chatbot"
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

### Access
Open browser to `http://localhost:8501`

## File Structure

```
Travel F&Q Chatbot/
├── app.py                          # Main application (247 lines)
├── requirements.txt                # Dependencies
├── README.md                       # Main project documentation
├── data/
│   ├── destination.json            # 500+ KB
│   ├── VisaChecker.json           # 200+ KB
│   ├── CurrencyExchange.json       # 50+ KB
│   └── TravelInsaurance.json       # 30+ KB
└── docs/
    ├── ARCHITECTURE.md             # System design
    ├── WORKFLOW.md                 # Process flows
    ├── INSTALLATION.md             # Setup guide
    ├── QUICK_REFERENCE.md          # This file
    ├── DATA_DICTIONARY.md          # Data schemas
    ├── DOCUMENTATION_INDEX.md      # Navigation guide
    └── PROJECT_OVERVIEW.md         # Visual guide
```

## Key Components

### 1. User Interface (Streamlit)
- Language selector (8 languages)
- Query input field
- Response display
- Clean, responsive design

### 2. NLP Engine
- Intent detection (6 types)
- Country extraction
- Multi-intent support

### 3. Response Generator
- Visa information
- Currency conversion
- Insurance plans
- Vaccination requirements
- Emergency contacts
- Local customs

### 4. Translation System
- Input → English conversion
- Output → Selected language conversion
- Google Translate API powered

## Dependencies

```
streamlit          # Web framework
deep-translator    # Translation library
json               # Built-in data format
```

## Core Functions

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `load_data()` | Load JSON files | None | (destinations, visa_rules, currency_rates, insurance) |
| `detect_intent()` | Find query intent | query (str) | intents (list) |
| `extract_country()` | Find destination | query (str) | country (str/None) |
| `translate_text()` | Translate response | text (str), lang (str) | translated (str) |
| `translate_to_english()` | Convert input | text (str) | english_text (str) |
| `travel_bot()` | Main logic | query (str) | response (str) |

## Intent Types & Keywords

| Intent | Keywords | Type |
|--------|----------|------|
| **visa** | visa | Document |
| **currency** | currency, exchange, rate | Finance |
| **insurance** | insurance | Finance |
| **vaccination** | vaccination, vaccine | Health |
| **emergency** | emergency, ambulance, police | Safety |
| **customs** | customs, culture, etiquette | Culture |
| **general** | (default) | Help |

## Supported Languages

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇫🇷 French
- 🇩🇪 German
- 🇪🇸 Spanish
- 🇮🇹 Italian
- 🇯🇵 Japanese
- 🇹🇭 Thai

## Example Queries

### Basic Queries
```
"Visa for France?"
"Currency in Japan"
"Insurance plans"
"Vaccination for Thailand"
```

### Advanced Queries
```
"Visa and insurance for Germany"
"Currency exchange and customs in Italy"
"Vaccination, emergency contacts, and insurance for Spain"
```

### Multi-Language Queries
```
Hindi:      "फ्रांस के लिए वीजा की आवश्यकता है?"
French:     "Quel est le visa pour la France?"
Spanish:    "¿Cuál es la visa para Francia?"
Japanese:   "フランスのビザはどうですか？"
```

## Common Issues & Solutions

### ❌ Streamlit Not Installed
```bash
pip install streamlit
```

### ❌ Translation Not Working
```bash
pip install deep-translator
```

### ❌ Data Files Not Found
Check `data/` folder has 4 JSON files

### ❌ Country Not Recognized
- Check spelling
- Try country alias (e.g., "USA" for United States)
- Verify country exists in `destination.json`

### ❌ Port 8501 Already in Use
```bash
streamlit run app.py --server.port 8502
```

## Response Times

| Operation | Time |
|-----------|------|
| Data Load | 50-100ms |
| Intent Detection | 1-2ms |
| Country Extraction | 1-2ms |
| Response Generation | 5-10ms |
| Translation | 100-500ms |
| **Total** | **150-600ms** |

## Data Storage Formats

### destination.json Structure
```json
{
  "CountryName": {
    "visa": "string",
    "vaccination": "string",
    "currency": {"name": "", "code": ""},
    "emergency": "string",
    "customs": "string",
    "aliases": ["alt1", "alt2"]
  }
}
```

### VisaChecker.json Structure
```json
{
  "SourceCountry": {
    "DestCountry": {
      "summary": "text",
      "application_process": ["step1", "step2"]
    }
  }
}
```

### CurrencyExchange.json Structure
```json
{
  "CODE": {
    "rate_to_INR": 1.5
  }
}
```

### TravelInsaurance.json Structure
```json
{
  "PlanName": {
    "price_range_inr": "₹5000 - ₹10000",
    "coverage": ["item1", "item2"]
  }
}
```

## Caching

- Uses `@st.cache_data` decorator
- Data cached after first load
- No disk I/O on subsequent accesses
- Session-based caching

## Performance Tips

1. **Faster Responses**: Use English queries (skip translation)
2. **Multiple Requests**: Keep app running (cached data)
3. **Slow Network**: Translation may take longer
4. **Large Queries**: Multiple intents = slightly slower

## Development Commands

```bash
# Check Python version
python --version

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 9000

# Check installation
pip list | grep -E "streamlit|deep"
```

## Browser Compatibility

- ✅ Chrome (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Focus input | Tab |
| Submit query | Enter |
| Reload app | R |
| Show settings | Shift+E |
| Keyboard help | Shift+H |

## Configuration Files

### Streamlit Config Location
```
Windows: C:\Users\<username>\.streamlit\config.toml
macOS:   ~/.streamlit/config.toml
Linux:   ~/.streamlit/config.toml
```

### Default Config
```toml
[server]
port = 8501
headless = false
runOnSave = true
```

## Security Notes

- No user data stored
- No authentication required
- Public API calls to Google Translate
- Suitable for public deployment
- Add rate limiting for production

## Future Enhancements

- [ ] Database integration
- [ ] User accounts & history
- [ ] Flight booking API
- [ ] Hotel recommendations
- [ ] Weather information
- [ ] Voice input/output
- [ ] Mobile app
- [ ] Advanced NLP (transformers)

## Support Resources

| Resource | Location |
|----------|----------|
| **README** | README.md |
| **Architecture** | ARCHITECTURE.md |
| **Workflow** | WORKFLOW.md |
| **Installation** | INSTALLATION.md |
| **This Guide** | QUICK_REFERENCE.md |

## Contact & Contribution

- **Author**: Sneha Tomar
- **Status**: Active Development
- **License**: MIT (Open Source)
- **Contributing**: Issues & PRs welcome

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial release |

## Useful Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Deep Translator Docs](https://py-translator.readthedocs.io/)
- [Python 3 Documentation](https://docs.python.org/3/)

---

**Quick Reference Guide v1.0** | Last Updated: February 2026
