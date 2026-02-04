# Workflow - Travel Information Chatbot

## User Journey
```
Select Language → Enter Query → Click Ask → View Response
```

## Request Processing Flow

```
1. VALIDATION
   └─ Check if query is empty

2. TRANSLATION (if needed)
   └─ Convert user input to English

3. INTENT DETECTION
   └─ Search for keywords: visa, currency, insurance, etc.
   └─ Result: List of intents

4. COUNTRY EXTRACTION
   └─ Match country name, aliases, or partial tokens
   └─ Result: Country name or None

5. VALIDATION
   └─ Check if country exists in database

6. RESPONSE GENERATION
   └─ For each intent, fetch relevant data
   └─ Format and combine responses

7. TRANSLATION (if needed)
   └─ Convert response to selected language

8. DISPLAY
   └─ Show in success box
```

## Intent Detection
| Intent | Keyword Check |
|--------|---------------|
| visa | "visa" |
| currency | "currency" OR "exchange" OR "rate" |
| insurance | "insurance" |
| vaccination | "vaccination" OR "vaccine" |
| emergency | "emergency" OR "ambulance" OR "police" |
| customs | "customs" OR "culture" |

## Country Extraction
1. Check exact country name match
2. Check aliases (e.g., "UK" → "United Kingdom")
3. Try partial token matching
4. Return first match or None

## Example: "Visa for France?"

```
Input: "Visa for France?"
↓
Validation: ✓ Not empty
↓
Translation: ✓ Already English
↓
Intent Detection: Found "visa"
intents = ["visa"]
↓
Country Extraction: Found "France"
country = "France"
↓
Validation: ✓ France exists
↓
Response Generation:
- Fetch visa_rules["India"]["France"]
- Fetch destinations["France"]["visa"]
- Format with application process
↓
Translation: ✓ English (no translation)
↓
Display: Visa information for France
```

## Example: "बीमा और वीजा के लिए थाईलैंड" (Hindi: Insurance & Visa for Thailand)

```
Input: "बीमा और वीजा के लिए थाईलैंड"
↓
Translation: → "Insurance and visa for Thailand"
↓
Intent Detection: Found ["insurance", "visa"]
↓
Country Extraction: Found "Thailand"
↓
Response Generation:
- Fetch insurance plans
- Fetch visa info for Thailand
- Combine responses
↓
Translation: → Hindi
↓
Display: Response in Hindi
```

## Response Generation Details

**Visa**: summary + process steps + detailed info

**Currency**: "1 CODE ≈ ₹RATE" lookup from exchange rates

**Insurance**: List all plans with coverage items

**Vaccination**: Direct fetch from destination data

**Emergency**: Contact info from destination data

**Customs**: Cultural info from destination data

## Error Scenarios

| Scenario | Result |
|----------|--------|
| Empty input | "Please enter a question." |
| No country mentioned | "Please mention a destination country." |
| Missing data field | Show "N/A" |
| Translation fails | Return English |
| No specific intent | Show help menu |

---
For detailed workflows with diagrams, see full WORKFLOW.md file.
