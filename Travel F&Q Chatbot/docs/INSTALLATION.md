# Installation & Setup Guide

## Requirements
- Python 3.7+
- pip (Python package manager)
- 500 MB disk space
- Internet (for translation feature)

## Installation (Quick)

```bash
cd "Travel F&Q Chatbot"
pip install -r requirements.txt
streamlit run app.py
```

Browser opens to `http://localhost:8501`

## Installation (Step by Step)

### 1. Clone/Download Project
```bash
cd path/to/Travel F&Q Chatbot
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv travel_env
travel_env\Scripts\activate

# macOS/Linux
python3 -m venv travel_env
source travel_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
streamlit --version
python -c "from deep_translator import GoogleTranslator; print('OK')"
```

## Run Application
```bash
streamlit run app.py
```

Then:
1. Select language from dropdown
2. Type your travel question
3. Click "Ask"
4. View response

## Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: streamlit` | `pip install streamlit` |
| `ModuleNotFoundError: deep_translator` | `pip install deep-translator` |
| `FileNotFoundError: destination.json` | Verify data/ folder exists |
| Port 8501 in use | `streamlit run app.py --server.port 8502` |
| Translation not working | Check internet connection |

## Advanced Setup

### Custom Port
```bash
streamlit run app.py --server.port 9000
```

### Disable Translation
Edit `app.py`, set `_HAS_DEEP_TRANSLATOR = False`

### Add Data Files
1. Update JSON files in data/ folder
2. Follow existing format
3. Restart application

## Uninstall
```bash
pip uninstall streamlit deep-translator
deactivate
rm -rf travel_env
```

## Troubleshooting

**Q: "No module named 'streamlit'"**
A: Run `pip install streamlit`

**Q: "Data files not found"**
A: Ensure `data/` folder has all 4 JSON files

**Q: "Translation not working"**
A: Check internet + try again, or use English queries

**Q: "Country not recognized"**
A: Check spelling or use alias (e.g., "USA" for United States)

**Q: "App runs slowly"**
A: First run slower due to data loading. Subsequent runs cached.

---
For detailed setup, see full INSTALLATION.md file.
