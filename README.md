Beschreibung des Börsenprogramms

Zweck des Programms

Das Programm sammelt und bewertet Informationen sowie Nachrichten zu Aktien und generiert darauf basierend Kaufempfehlungen. Es nutzt zwei APIs:

Financial Modeling Prep (https://site.financialmodelingprep.com/) für Finanzkennzahlen.

GDELT Project (https://www.gdeltproject.org/) für Nachrichtenanalyse.

Die Daten werden in einer CSV-Datei gespeichert, die zur weiteren Analyse in Excel verwendet werden kann.

Seiten des Programms

1. Hauptseite

Auf der Hauptseite werden die fünf besten Firmen angezeigt, inklusive:

Firmenname

Kurschart

KGV (Kurs-Gewinn-Verhältnis)

Dividende

Ex-Dividenden-Datum

Gesamtbewertung

Zusätzlich gibt es Buttons, um auf weitere Seiten zu gelangen:

"Firmen aufnehmen" (Weiterleitung zur zweiten Seite)

"Firma analysieren" (Weiterleitung zur dritten Seite)

"CSV-Datei anzeigen" (Weiterleitung zur vierten Seite)

2. Firmen aufnehmen

Diese Seite zeigt eine Liste von bereits gespeicherten Firmen mit Daten.
Zusätzlich gibt es:

Ein Eingabefeld zur Eingabe weiterer Firmen.

Eine Funktion, um das Börsenkürzel automatisch zu ermitteln.

Einen "Hinzufügen"-Button, um neue Firmen zur Datenbank hinzuzufügen.

3. Firma analysieren

Diese Seite enthält eine sortierbare Tabelle mit den gespeicherten Firmen. Spalten:

Kleiner Chart

KGV

Dividende

Ex-Dividenden-Datum

Bewertung

Nutzer können die Tabelle nach verschiedenen Kriterien sortieren.

4. CSV-Datei anzeigen

Auf dieser Seite wird der Inhalt der CSV-Datei dargestellt. Alle gespeicherten Informationen werden in Tabellenform angezeigt, sodass sie zur Weiterverarbeitung in Excel exportiert werden können.

Zusammenfassung

Das Börsenprogramm dient der Sammlung, Bewertung und Darstellung von Aktieninformationen. Es ermöglicht die Analyse der besten Aktien, das Hinzufügen neuer Unternehmen sowie die Verwaltung und Sortierung von Finanzdaten. Die CSV-Speicherung stellt sicher, dass alle relevanten Informationen einfach weiterverwendet werden können.

boersenprogramm/
│── main.py               # Startpunkt der Anwendung (GUI oder CLI)
│── config.py             # API-Keys und Konfigurationsvariablen
│── data_handler.py       # Laden und Speichern von CSV-Daten
│── api_fetcher.py        # Abruf von Finanz- und Nachrichten-Daten über APIs
│── analysis.py           # Bewertung und Verarbeitung der Daten
│── ui/                   # UI-Module (z.B. Flask, Streamlit oder Tkinter)
│   ├── main_page.py      # Hauptseite mit Top 5 Firmen
│   ├── add_company.py    # Firmenaufnahme
│   ├── analysis_page.py  # Tabellenansicht zur Analyse
│   ├── csv_viewer.py     # CSV-Datei-Anzeige
│── assets/               # Statische Dateien (z.B. Icons, CSS)
│── tests/                # Unit-Tests für die Module
