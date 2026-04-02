# Local ML Web App

This Flask app loads your saved `LinearRegression` model and serves a local web interface.

## Model inputs
The uploaded model expects these 5 features in this exact order:

1. Engine volume
2. Mileage
3. Cylinders
4. Prod. year
5. Levy

## Files
- `app.py` - Flask server
- `model.pkl` - your saved model
- `templates/index.html` - frontend form
- `requirements.txt` - dependencies

## Run locally

### 1) Create and activate a virtual environment (recommended)

Windows:
```bash
py -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Start the local server
```bash
python app.py
```

### 4) Open in your browser
```text
http://127.0.0.1:5000
```

## Notes
- The model is a scikit-learn `LinearRegression`.
- If you retrain the model, replace `model.pkl` with the new file.
- If feature order changes, update `FEATURES` in `app.py`.
