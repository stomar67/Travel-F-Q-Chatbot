# Architecture - Travel Information Chatbot

## System Layers

```
Streamlit UI (Input/Display)
    ↓
Translation Layer (Google Translate)
    ↓
NLP Layer (Intent Detection, Entity Extraction)
    ↓
Business Logic (travel_bot() function)
    ↓
Data Layer (load_data() with caching)
    ↓
JSON Files (destination, visa, currency, insurance)
```

## Components

| Layer | Responsibility |
|-------|-----------------|
| **UI** | Web interface with language selector & query input |
| **Translation** | Input translation to English, output to target language |
| **NLP** | Intent detection via keywords, country extraction |
| **Logic** | Response generation for each intent |
| **Data Access** | Load JSON files with @st.cache_data |
| **Storage** | 4 JSON files with travel data |

## Data Flow

```
User Input → Language Detection → Translate to English 
    → Intent Detection → Country Extraction 
    → Fetch Data → Format Response 
    → Translate to Selected Language → Display
```

## Intent Handlers

| Intent | Sources | Output |
|--------|---------|--------|
| visa | visa_rules + destinations | Summary + process steps |
| currency | currency_rates + destinations | Exchange rate to INR |
| insurance | insurance | Plan list with coverage |
| vaccination | destinations | Requirements |
| emergency | destinations | Contact numbers |
| customs | destinations | Cultural info |

## Design Patterns
- **Caching**: @st.cache_data for performance
- **Factory**: Multiple data sources with consistent interface
- **Strategy**: Different handlers per intent
- **Facade**: travel_bot() as simple interface

## Performance
- Data caching: One disk read per session
- Intent detection: O(n) keyword matching
- Currency conversion: Direct lookup
- Translation: 100-500ms (external API)

## Files
- `app.py` (247 lines) - Main application
- `destination.json` (~500 KB) - Core data
- `VisaChecker.json` (~200 KB) - Visa rules
- `CurrencyExchange.json` (~50 KB) - Exchange rates
- `TravelInsaurance.json` (~30 KB) - Insurance plans

## Error Handling
- Empty input: Warning message
- Missing country: Error message
- Missing data: Default to "N/A"
- Translation error: Return English text
- Missing translator: Skip translation gracefully

## Scalability Notes
- Current: File-based (suitable for <1000 destinations)
- 10x growth: Add database (PostgreSQL)
- 100x growth: Microservices + distributed DB
- Global: Regional databases + CDN

---
For detailed architecture, see full ARCHITECTURE.md file.
