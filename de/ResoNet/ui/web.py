"""
ResonanzNet Web-UI – Das lokale Portal ins Feld
Systemisch: Ermöglicht Meinungseintrag, Ansicht, Synchronisation und Gruppenzugehörigkeit via Webbrowser.
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash
import json
from pathlib import Path
from datetime import datetime

DATA_PATH = Path("../data/opinions.json")
CONFIG_PATH = Path("../setup/config.json")

app = Flask(__name__)
app.secret_key = "resonanzfeld"  # für Flash-Nachrichten

TEMPLATE = """
<!doctype html>
<title>ResonanzNet Feld-UI</title>
<h1>ResonanzNet: Das Feld der Stimmen</h1>
<p><b>Knoten:</b> {{ node_name }}</p>
<p><b>Themenfelder:</b> {{ topics|join(", ") }}</p>
<hr>
<h2>Neue Meinung eintragen</h2>
<form method="post" action="{{ url_for('add_opinion') }}">
    <label>Thema:
        <select name="topic">
        {% for t in topics %}
            <option value="{{ t }}">{{ t }}</option>
        {% endfor %}
        </select>
    </label><br>
    <label>Meinung:<br>
        <textarea name="opinion" rows="3" cols="50" required></textarea>
    </label><br>
    <button type="submit">Absenden</button>
</form>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>{% for msg in messages %}<li>{{ msg }}</li>{% endfor %}</ul>
  {% endif %}
{% endwith %}
<hr>
<h2>Meinungen im Feld</h2>
<table border="1" cellpadding="4">
  <tr>
    <th>Zeitpunkt</th>
    <th>Thema</th>
    <th>Meinung</th>
    <th>Autor</th>
  </tr>
  {% for op in opinions %}
  <tr>
    <td>{{ op.timestamp }}</td>
    <td>{{ op.topic }}</td>
    <td>{{ op.opinion }}</td>
    <td>{{ op.author }}</td>
  </tr>
  {% endfor %}
</table>
<hr>
<form method="post" action="{{ url_for('sync') }}">
    <button type="submit">Mit Feld synchronisieren (Platzhalter)</button>
</form>
"""

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"node_name": "raspy.local", "topics": ["Allgemein"]}

def load_opinions():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_opinions(opinions):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(opinions, f, ensure_ascii=False, indent=2)

@app.route("/", methods=["GET"])
def index():
    config = load_config()
    opinions = load_opinions()
    opinions_sorted = sorted(opinions, key=lambda o: o.get("timestamp", ""), reverse=True)
    return render_template_string(
        TEMPLATE,
        node_name=config.get("node_name", "raspy.local"),
        topics=config.get("topics", ["Allgemein"]),
        opinions=opinions_sorted
    )

@app.route("/add", methods=["POST"])
def add_opinion():
    config = load_config()
    opinions = load_opinions()
    author = config.get("node_name", "raspy.local")
    topic = request.form.get("topic", "Allgemein")
    text = request.form.get("opinion", "").strip()
    if not text:
        flash("Meinung darf nicht leer sein.")
        return redirect(url_for("index"))
    opinion = {
        "author": author,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "topic": topic,
        "opinion": text,
        "signature": ""
    }
    opinions.append(opinion)
    save_opinions(opinions)
    flash("Meinung eingetragen!")
    return redirect(url_for("index"))

@app.route("/sync", methods=["POST"])
def sync():
    # Platzhalter: Hier könnte sync_with_peers() eingebunden werden
    flash("Synchronisation mit Feld (Platzhalter – keine echte P2P-Sync).")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)