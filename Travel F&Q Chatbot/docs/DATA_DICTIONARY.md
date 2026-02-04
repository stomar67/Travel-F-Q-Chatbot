# Data Dictionary 

## JSON Files Overview

| File | Size | Purpose |
|------|------|---------|
| destination.json | ~500 KB | Main destination info (visa, vaccination, currency, emergency, customs) |
| VisaChecker.json | ~200 KB | Visa requirements between country pairs |
| CurrencyExchange.json | ~50 KB | Exchange rates to INR |
| TravelInsaurance.json | ~30 KB | Insurance plans & coverage |

## destination.json Structure

```json
{
  "CountryName": {
    "visa": "string",
    "vaccination": "string",
    "currency": "string or {name, code}",
    "emergency": "string",
    "customs": "string",
    "aliases": ["alt1", "alt2"]
  }
}
```

**Fields**:
- **visa**: Visa requirements text
- **vaccination**: Vaccination requirements
- **currency**: Currency name & code (flexible format)
- **emergency**: Emergency contact numbers
- **customs**: Local customs & etiquette
- **aliases**: Alternative country names (optional)

## VisaChecker.json Structure

```json
{
  "SourceCountry": {
    "DestCountry": {
      "summary": "Brief visa info",
      "application_process": ["Step 1", "Step 2"]
    }
  }
}
```

**Fields**:
- **summary**: Visa requirements overview
- **application_process**: Steps to apply (array or string)

## CurrencyExchange.json Structure

```json
{
  "CODE": {
    "rate_to_INR": 1.5
  }
}
```

**Fields**:
- **CODE**: 3-letter currency code (ISO 4217)
- **rate_to_INR**: Exchange rate (1 unit = X rupees)

## TravelInsaurance.json Structure

```json
{
  "PlanName": {
    "price_range_inr": "₹5000 - ₹10000",
    "coverage": ["Medical up to ₹500K", "Lost baggage"]
  }
}
```

**Fields**:
- **PlanName**: Insurance plan name
- **price_range_inr**: Price range format
- **coverage**: Array of coverage items

## Data Examples

**destination.json entry**:
```json
{
  "France": {
    "visa": "Schengen visa required for most nationalities...",
    "vaccination": "No mandatory vaccinations...",
    "currency": {"name": "Euro", "code": "EUR"},
    "emergency": "Police: 17 | Ambulance: 15",
    "customs": "Use formal greetings, respect personal space...",
    "aliases": ["FR", "French Republic"]
  }
}
```

**VisaChecker.json entry**:
```json
{
  "India": {
    "France": {
      "summary": "Indian nationals need Schengen visa...",
      "application_process": [
        "Gather documents",
        "Complete DS-160",
        "Schedule interview",
        "Attend interview"
      ]
    }
  }
}
```

**CurrencyExchange.json entry**:
```json
{
  "EUR": {"rate_to_INR": 91.20},
  "USD": {"rate_to_INR": 83.45}
}
```

**TravelInsaurance.json entry**:
```json
{
  "Premium Protection": {
    "price_range_inr": "₹15,000 - ₹25,000",
    "coverage": [
      "Medical up to ₹500,000",
      "Flight delay compensation",
      "Trip cancellation 100%"
    ]
  }
}
```

## Data Validation Rules

**Required**: Country name, at least visa OR currency
**Optional**: aliases, application_process
**Format**: UTF-8 encoded JSON
**Currency Code**: 3 uppercase letters (ISO 4217)
**Exchange Rate**: Positive number, 2-4 decimals

## Data Quality Checklist

- [ ] All JSON files are valid
- [ ] UTF-8 encoding correct
- [ ] No missing commas/brackets
- [ ] Country names consistent
- [ ] Currency codes are ISO 4217 standard
- [ ] Exchange rates current
- [ ] No duplicate entries
- [ ] Price ranges properly formatted
- [ ] Coverage descriptions clear

---
For detailed field definitions and examples, see full DATA_DICTIONARY.md file.
