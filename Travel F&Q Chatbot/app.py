import streamlit as st
import json

# Try to import deep_translator; show a helpful message in the UI if missing
try:
    from deep_translator import GoogleTranslator
    _HAS_DEEP_TRANSLATOR = True
except ModuleNotFoundError:
    GoogleTranslator = None
    _HAS_DEEP_TRANSLATOR = False

# ------------------ LOAD DATA ------------------ #

@st.cache_data
def load_data():
    with open("C:\\Users\\SNEHA TOMAR\\Desktop\\Ds_Ml_code\\Travel F&Q Chatbot\\data\\destination.json", "r", encoding="utf-8") as f:
        destinations = json.load(f)

    with open("C:\\Users\\SNEHA TOMAR\\Desktop\\Ds_Ml_code\\Travel F&Q Chatbot\\data\\VisaChecker.json", "r", encoding="utf-8") as f:
        visa_rules = json.load(f)

    with open("C:\\Users\\SNEHA TOMAR\\Desktop\\Ds_Ml_code\\Travel F&Q Chatbot\\data\\CurrencyExchange.json", "r", encoding="utf-8") as f:
        currency_rates = json.load(f)

    with open("C:\\Users\\SNEHA TOMAR\\Desktop\\Ds_Ml_code\\Travel F&Q Chatbot\\data\\TravelInsaurance.json", "r", encoding="utf-8") as f:
        insurance = json.load(f)

    return destinations, visa_rules, currency_rates, insurance


destinations, visa_rules, currency_rates, insurance = load_data()

# ------------------ NLP HELPERS ------------------ #

def detect_intent(query):
    """Detect ALL intents present in the query (supports combined questions)."""
    q = query.lower()
    intents = []
    
    # Check for specific intents with multiple keyword variations
    if "visa" in q:
        intents.append("visa")
    if "currency" in q or "exchange" in q or "rate" in q:
        intents.append("currency")
    if "insurance" in q:
        intents.append("insurance")
    if "vaccination" in q or "vaccine" in q or "immunization" in q or "inoculation" in q:
        intents.append("vaccination")
    if "emergency" in q or "emergence" in q or "ambulance" in q or "police" in q or "helpline" in q or "urgent" in q:
        intents.append("emergency")
    if "custom" in q or "customs" in q or "tradition" in q or "culture" in q or "etiquette" in q or "rule" in q or "law" in q:
        intents.append("customs")
    
    return intents if intents else ["general"]


def extract_country(query):
    q = query.lower()
    # First check aliases if present
    for country, info in destinations.items():
        names = [country.lower()]
        if isinstance(info, dict) and "aliases" in info and isinstance(info["aliases"], list):
            names.extend([a.lower() for a in info["aliases"] if isinstance(a, str)])
        for name in set(names):
            if name and name in q:
                return country

    # fallback: check tokens (matches multi-word country mentions)
    tokens = q.split()
    for country in destinations.keys():
        for t in tokens:
            if t and t == country.lower()[:len(t)]:
                return country

    return None


def translate_text(text, lang):
    if lang == "English":
        return text
    # map friendly language names to Google language codes
    LANG_CODE = {
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Italian": "it",
        "Japanese": "ja",
        "Thai": "th",
    }

    if not _HAS_DEEP_TRANSLATOR:
        return text

    target = LANG_CODE.get(lang, "en")
    try:
        return GoogleTranslator(source="auto", target=target).translate(text)
    except Exception:
        return text


def translate_to_english(text):
    """Translate arbitrary user input to English for intent/country extraction."""
    if not _HAS_DEEP_TRANSLATOR:
        return text
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except Exception:
        return text

# ------------------ CHATBOT CORE ------------------ #

def travel_bot(query, user_country="India"):
    intents = detect_intent(query)
    country = extract_country(query)

    if not country:
        return "Please mention a destination country."

    responses = {}

    # Handle each intent
    for intent in intents:
        if intent == "visa":
            # visa_rules entries may be either a short string or a dict with
            # 'summary' and 'application_process'. Support both formats.
            raw = visa_rules.get(user_country, {}).get(country)
            summary_text = None
            process = None
            if isinstance(raw, dict):
                summary_text = raw.get("summary")
                process = raw.get("application_process")
            else:
                summary_text = raw

            detailed = destinations.get(country, {}).get("visa")

            parts = []
            if summary_text:
                parts.append(str(summary_text))

            if detailed:
                parts.append(f"Details: {detailed}")

            if process:
                # process may be a string or list
                if isinstance(process, list):
                    steps = "\n".join([f"- {s}" for s in process])
                    parts.append("Application process:\n" + steps)
                else:
                    parts.append("Application process: " + str(process))

            responses["Visa"] = "\n\n".join(parts) if parts else "Visa info not available."

        elif intent == "vaccination":
            responses["Vaccination"] = destinations[country].get("vaccination", "N/A")

        elif intent == "currency":
            # Support structured currency or old string format
            cur = destinations[country].get("currency")
            currency_code = None
            if isinstance(cur, dict):
                currency_code = cur.get("code")
            elif isinstance(cur, str):
                # parse like 'Japanese Yen (JPY)' or 'Japanese Yen (JPY).'
                try:
                    currency_code = cur.split("(")[-1].replace(")", "").strip().rstrip('.')
                except Exception:
                    currency_code = None

            if currency_code:
                currency_code = currency_code.upper()
                rate_info = currency_rates.get(currency_code, {})
                responses["Currency"] = f"1 {currency_code} ≈ ₹{rate_info.get('rate_to_INR', 'N/A')}"
            else:
                responses["Currency"] = "Currency info not available."

        elif intent == "insurance":
            response = ""
            for plan, details in insurance.items():
                response += f"\n{plan} Plan:\n"
                response += f"Price: {details['price_range_inr']}\n"
                response += "Coverage:\n"
                for c in details["coverage"]:
                    response += f"- {c}\n"
            responses["Insurance"] = response

        elif intent == "emergency":
            responses["Emergency"] = destinations[country].get("emergency", "N/A")

        elif intent == "customs":
            responses["Customs"] = destinations[country].get("customs", "N/A")

    # If general intent is the only one, show menu
    if intents == ["general"]:
        return (
            f"Please ask about a specific topic:\n"
            f"• Visa requirements\n"
            f"• Vaccination requirements\n"
            f"• Currency exchange\n"
            f"• Local customs\n"
            f"• Emergency contacts\n"
            f"• Travel insurance"
        )

    # Combine all responses
    if responses:
        return "\n\n".join([f"{key}: {value}" for key, value in responses.items()])
    
    return "Visa info not available."

# ------------------ STREAMLIT UI ------------------ #

st.set_page_config(page_title="Travel FAQ Chatbot", page_icon="🌍")

st.title("🌍 Travel Information Chatbot")
st.subheader("Visa • Vaccination • Currency • Insurance • Emergency Info")

language = st.selectbox(
    "Select Response Language",
    ["English", "Hindi", "French", "German", "Spanish", "Italian", "Japanese", "Thai"]
)

user_query = st.text_input("Ask your travel question:")

if st.button("Ask"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Translate user input to English for intent detection and country extraction
        processed_query = user_query
        if _HAS_DEEP_TRANSLATOR:
            try:
                processed_query = translate_to_english(user_query)
            except Exception:
                processed_query = user_query

        answer = travel_bot(processed_query)

        # Translate the answer to the user's selected language
        translated_answer = translate_text(answer, language)
        st.success(translated_answer)

st.markdown("---")
st.caption("Powered by Streamlit | Travel FAQ Bot Project")
