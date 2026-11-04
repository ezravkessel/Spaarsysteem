"# Spaarsysteem" 

"# Teamleden"
- Ezra
- Luna
- Vasco

Een spaarsysteem gemaakt met Python (Flask), HTML, CSS en JavaScript.

# Spaarsysteem

Een spaarsysteem gemaakt met Python (Flask), HTML, CSS en JavaScript.

## Wat heb je nodig?

- [Python](https://www.python.org/downloads/) (3.10 of nieuwer)
- [Git](https://git-scm.com/downloads)

## Installeren en starten (Windows)

Open een terminal en voer deze commando's één voor één uit:

```bash
git clone https://github.com/ezravkessel/Spaarsysteem.git
cd Spaarsysteem
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m flask --app app run --port 5050
```

Open daarna in je browser: <http://127.0.0.1:5050>

Stoppen kan met `Ctrl+C` in de terminal.

## Installeren en starten (Mac / Linux)

```bash
git clone https://github.com/ezravkessel/Spaarsysteem.git
cd Spaarsysteem
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m flask --app app run --port 5050

## Gebruikersdatabase instellen

Sparo gebruikt SQLite om gebruikersaccounts op te slaan. Wachtwoorden worden beveiligd opgeslagen als een hash.

De database (`sparo.db`) wordt niet meegestuurd via GitHub. Iedereen moet deze daarom één keer zelf aanmaken.

### Database aanmaken

Open een terminal in de projectmap en voer uit:

**Windows:**
```powershell
python database.py
```

**Mac / Linux:**
```bash
python3 database.py
```

Als het gelukt is, verschijnt:

`Database succesvol aangemaakt!`

Het bestand `sparo.db` wordt automatisch aangemaakt.

### Een testgebruiker toevoegen

Start Python in de projectmap:

```powershell
python
```

Voer daarna deze regels één voor één uit:

```python
from database import add_user
add_user("test@sparo.nl", "Test123!voorbeeld")
exit()
```

Gebruik alleen testgegevens. Het wachtwoord wordt automatisch gehasht voordat het wordt opgeslagen.

**Let op:** een e-mailadres kan maar één keer in de database voorkomen. Voeg hetzelfde testaccount dus niet opnieuw toe.

### SECRET_KEY instellen

Sparo gebruikt een `SECRET_KEY` om inlogsessies te beveiligen. Deze sleutel mag niet in GitHub worden opgeslagen.

**Windows (PowerShell):**
```powershell
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
```

**Mac / Linux:**
```bash
export SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
```

Stel de sleutel in voordat je Flask start. Gebruik hiervoor dezelfde terminal.

### Sparo starten

**Windows:**
```powershell
python -m flask --app app run --port 5050
```

**Mac / Linux:**
```bash
python3 -m flask --app app run --port 5050
```

Open daarna:

http://127.0.0.1:5050/login

Log in met je aangemaakte testaccount.

Na het inloggen kun je via `/profiel` controleren of je sessie werkt en uitloggen.

**Belangrijk:** als je een nieuwe terminal opent, moet je de `SECRET_KEY` opnieuw instellen.










```

## Projectstructuur

```
Spaarsysteem/
├── app.py              # Flask-applicatie (Python)
├── requirements.txt    # Benodigde pakketten
├── templates/          # HTML-bestanden
│   └── index.html
└── static/             # CSS en JavaScript
    ├── css/style.css
    └── js/script.js
```

## Let op

- Activeer de virtuele omgeving (`venv`) elke keer als je een nieuwe terminal opent.
- Installeer je een nieuw pakket? Voer dan `pip freeze > requirements.txt` uit en commit het bestand.
