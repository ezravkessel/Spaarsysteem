"# Spaarsysteem" 

"# Teamleden"
- Ezra
- Luna
- Vasco

Een spaarsysteem gemaakt met Python (Flask), HTML, CSS en JavaScript.

Wat heb je nodig?
Python (3.10 of nieuwer)
Git
Installeren en starten (Windows)

Open een terminal en voer deze commando's één voor één uit:

bash
git clone https://github.com/ezravkessel/Spaarsysteem.git
cd Spaarsysteem
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Open daarna in je browser: http://127.0.0.1:5000

Stoppen kan met Ctrl+C in de terminal.

Installeren en starten (Mac / Linux)
bash
git clone https://github.com/ezravkessel/Spaarsysteem.git
cd Spaarsysteem
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
Projectstructuur
Spaarsysteem/
├── app.py              # Flask-applicatie (Python)
├── requirements.txt    # Benodigde pakketten
├── templates/          # HTML-bestanden
│   └── index.html
└── static/             # CSS en JavaScript
    ├── css/style.css
    └── js/script.js
Let op
Activeer de virtuele omgeving (venv) elke keer als je een nieuwe terminal opent.
Installeer je een nieuw pakket? Voer dan pip freeze > requirements.txt uit en commit het bestand.