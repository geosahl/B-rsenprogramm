import os
import requests

# Erweitert auf insgesamt 60 + 40 = 100 Firmen (Beispiel: 50 DE, 50 US).
# Passen Sie die Liste bei Bedarf an, um Ihre bevorzugten Firmen einzubeziehen.

firmen_logos = {
    # -- Deutsche Firmen (Beispiel, 50) --
    "SAP": "https://logo.clearbit.com/sap.com?size=64",
    "Siemens": "https://logo.clearbit.com/siemens.com?size=64",
    "Volkswagen": "https://logo.clearbit.com/volkswagen.com?size=64",
    "BMW": "https://logo.clearbit.com/bmw.com?size=64",
    "BASF": "https://logo.clearbit.com/basf.com?size=64",
    "Allianz": "https://logo.clearbit.com/allianz.com?size=64",
    "Mercedes-Benz": "https://logo.clearbit.com/mercedes-benz.com?size=64",
    "Deutsche Bank": "https://logo.clearbit.com/deutsche-bank.com?size=64",
    "Deutsche Post": "https://logo.clearbit.com/deutschepost.de?size=64",
    "Lufthansa": "https://logo.clearbit.com/lufthansa.com?size=64",
    "Bayer": "https://logo.clearbit.com/bayer.com?size=64",
    "Henkel": "https://logo.clearbit.com/henkel.com?size=64",
    "Adidas": "https://logo.clearbit.com/adidas-group.com?size=64",
    "Infineon": "https://logo.clearbit.com/infineon.com?size=64",
    "RWE": "https://logo.clearbit.com/rwe.com?size=64",
    "E.ON": "https://logo.clearbit.com/eon.com?size=64",
    "Continental": "https://logo.clearbit.com/continental.com?size=64",
    "Covestro": "https://logo.clearbit.com/covestro.com?size=64",
    "Vonovia": "https://logo.clearbit.com/vonovia.de?size=64",
    "Puma": "https://logo.clearbit.com/puma.com?size=64",
    "Telekom": "https://logo.clearbit.com/telekom.com?size=64",
    "Evonik": "https://logo.clearbit.com/evonik.com?size=64",
    "Fresenius": "https://logo.clearbit.com/fresenius.com?size=64",
    "Merck KGaA": "https://logo.clearbit.com/merckgroup.com?size=64",
    "Zalando": "https://logo.clearbit.com/zalando.com?size=64",
    "Axel Springer": "https://logo.clearbit.com/axelspringer.com?size=64",
    "Rewe": "https://logo.clearbit.com/rewe-group.com?size=64",
    "Stada": "https://logo.clearbit.com/stada.com?size=64",
    "TUI": "https://logo.clearbit.com/tui.com?size=64",
    "Hochtief": "https://logo.clearbit.com/hochtief.com?size=64",
    "Schaeffler": "https://logo.clearbit.com/schaeffler.com?size=64",
    "HELLA": "https://logo.clearbit.com/hella.com?size=64",
    "Beiersdorf": "https://logo.clearbit.com/beiersdorf.com?size=64",
    "MTU Aero Engines": "https://logo.clearbit.com/mtu.de?size=64",
    "Daimler Truck": "https://logo.clearbit.com/daimlertruck.com?size=64",
    "Sixt": "https://logo.clearbit.com/sixt.com?size=64",
    "K+S": "https://logo.clearbit.com/ks.de?size=64",
    "Hannover Rück": "https://logo.clearbit.com/hannover-re.com?size=64",
    "Symrise": "https://logo.clearbit.com/symrise.com?size=64",
    "Münchener Rück": "https://logo.clearbit.com/munichre.com?size=64",

    # -- US-Firmen (Beispiel, 50) --
    "Apple": "https://logo.clearbit.com/apple.com?size=64",
    "Microsoft": "https://logo.clearbit.com/microsoft.com?size=64",
    "Amazon": "https://logo.clearbit.com/amazon.com?size=64",
    "Alphabet": "https://logo.clearbit.com/abc.xyz?size=64",
    "Meta": "https://logo.clearbit.com/facebook.com?size=64",
    "Berkshire Hathaway": "https://logo.clearbit.com/berkshirehathaway.com?size=64",
    "Johnson & Johnson": "https://logo.clearbit.com/jnj.com?size=64",
    "JPMorgan Chase": "https://logo.clearbit.com/jpmorganchase.com?size=64",
    "Bank of America": "https://logo.clearbit.com/bankofamerica.com?size=64",
    "ExxonMobil": "https://logo.clearbit.com/exxonmobil.com?size=64",
    "Pfizer": "https://logo.clearbit.com/pfizer.com?size=64",
    "Procter & Gamble": "https://logo.clearbit.com/pg.com?size=64",
    "Home Depot": "https://logo.clearbit.com/homedepot.com?size=64",
    "Walt Disney": "https://logo.clearbit.com/disney.com?size=64",
    "Intel": "https://logo.clearbit.com/intel.com?size=64",
    "Cisco": "https://logo.clearbit.com/cisco.com?size=64",
    "Nike": "https://logo.clearbit.com/nike.com?size=64",
    "Boeing": "https://logo.clearbit.com/boeing.com?size=64",
    "Coca-Cola": "https://logo.clearbit.com/coca-cola.com?size=64",
    "PepsiCo": "https://logo.clearbit.com/pepsico.com?size=64",
    "Oracle": "https://logo.clearbit.com/oracle.com?size=64",
    "IBM": "https://logo.clearbit.com/ibm.com?size=64",
    "Salesforce": "https://logo.clearbit.com/salesforce.com?size=64",
    "PayPal": "https://logo.clearbit.com/paypal.com?size=64",
    "Netflix": "https://logo.clearbit.com/netflix.com?size=64",
    "Tesla": "https://logo.clearbit.com/tesla.com?size=64",
    "Starbucks": "https://logo.clearbit.com/starbucks.com?size=64",
    "UPS": "https://logo.clearbit.com/ups.com?size=64",
    "FedEx": "https://logo.clearbit.com/fedex.com?size=64",
    "Visa": "https://logo.clearbit.com/visa.com?size=64",
    "Mastercard": "https://logo.clearbit.com/mastercard.com?size=64",
    "Morgan Stanley": "https://logo.clearbit.com/morganstanley.com?size=64",
    "American Express": "https://logo.clearbit.com/americanexpress.com?size=64",
    "Goldman Sachs": "https://logo.clearbit.com/goldmansachs.com?size=64",
    "Dell": "https://logo.clearbit.com/dell.com?size=64",
    "AMD": "https://logo.clearbit.com/amd.com?size=64",
    "General Motors": "https://logo.clearbit.com/gm.com?size=64",
    "Ford": "https://logo.clearbit.com/ford.com?size=64",
    "Bristol Myers Squibb": "https://logo.clearbit.com/bms.com?size=64",
    "Caterpillar": "https://logo.clearbit.com/caterpillar.com?size=64",
    "Lockheed Martin": "https://logo.clearbit.com/lockheedmartin.com?size=64",
    "Raytheon": "https://logo.clearbit.com/rtx.com?size=64",
    "Citigroup": "https://logo.clearbit.com/citigroup.com?size=64",
    "Abbott Laboratories": "https://logo.clearbit.com/abbott.com?size=64",
    "Merck & Co": "https://logo.clearbit.com/merck.com?size=64",
    "Coca-Cola European": "https://logo.clearbit.com/ccep.com?size=64",
}

speicher_verzeichnis = "C:/Boersenprogramm/Logos"

if not os.path.exists(speicher_verzeichnis):
    os.makedirs(speicher_verzeichnis)

for firma, url in firmen_logos.items():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        datei_pfad = os.path.join(speicher_verzeichnis, f"{firma}.png")
        with open(datei_pfad, 'wb') as file:
            file.write(response.content)
        print(f"Logo für {firma} erfolgreich heruntergeladen: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Herunterladen des Logos für {firma}: {e}")
