import streamlit as st
import requests

st.set_page_config(page_title="Berufsorientierung Saarland", layout="centered")

st.title("💬 Berufsorientierungs-Chatbot Saarland")
st.write("Willkommen! Ich helfe dir bei beruflicher Neuorientierung im Saarland – z. B. nach Jobverlust oder in einer Umbruchphase.")

# Schritt 1: Grunddaten
st.header("1️⃣ Deine Situation")
wohnort = st.text_input("In welchem Ort wohnst du?")
beruf = st.text_input("Was ist dein aktueller oder letzter Beruf?")
situation = st.selectbox("Wie ist deine aktuelle Situation?", ["Ich habe meinen Job verloren", "Ich bin von Jobverlust bedroht", "Ich möchte mich beruflich verändern"])

# Schritt 2: Interessen
st.header("2️⃣ Deine Interessen")
interessen = st.multiselect(
    "Welche Bereiche interessieren dich besonders?",
    ["IT & Digitalisierung", "Gesundheit & Soziales", "Umwelt & Nachhaltigkeit", "Handwerk & Technik", "Bildung & Pädagogik", "Kaufmännisch & Verwaltung"]
)

# Schritt 3: Weiterbildung
st.header("3️⃣ Weiterbildung")
weiterbildung = st.selectbox("Hast du Interesse an einer Weiterbildung oder Umschulung?", ["Ja", "Nein", "Vielleicht"])

# Schritt 4: Beratung
st.header("4️⃣ Beratung")
beratung = st.selectbox("Möchtest du persönliche Beratung in Anspruch nehmen?", ["Ja", "Nein", "Vielleicht später"])

# Schritt 5: Ergebnisse anzeigen
if st.button("🔍 Auswertung & Empfehlungen anzeigen"):
    st.subheader("📋 Deine Angaben")
    st.write(f"**Wohnort:** {wohnort}")
    st.write(f"**Beruf:** {beruf}")
    st.write(f"**Situation:** {situation}")
    st.write(f"**Interessen:** {', '.join(interessen)}")
    st.write(f"**Weiterbildung:** {weiterbildung}")
    st.write(f"**Beratung:** {beratung}")

    st.subheader("🎓 Weiterbildungsempfehlungen")
    for interesse in interessen:
        if interesse == "IT & Digitalisierung":
            st.markdown("- Umschulung zum Fachinformatiker, IT-Support, Datenanalyse")
        elif interesse == "Gesundheit & Soziales":
            st.markdown("- Weiterbildung zur Betreuungskraft, Pflegeberater/in")
        elif interesse == "Umwelt & Nachhaltigkeit":
            st.markdown("- Kurse zu erneuerbaren Energien, Recycling, Umwelttechnik")
        elif interesse == "Handwerk & Technik":
            st.markdown("- Umschulung in SHK, Elektro, Fahrzeugtechnik")
        elif interesse == "Bildung & Pädagogik":
            st.markdown("- Weiterbildung zum Erzieher/in, Bildungscoach")
        elif interesse == "Kaufmännisch & Verwaltung":
            st.markdown("- Fortbildung in Buchhaltung, Projektorganisation")

    st.markdown("🔗 [Weiterbildungsportal Saarland](https://weiterbildungsportal.saarland/)")
    st.markdown("🔗 [KURSNET der Agentur für Arbeit](https://kursnet-finden.arbeitsagentur.de/kurs/)")
    st.markdown("🔗 [IHK Saarland](https://www.saarland.ihk.de/)")
    st.markdown("🔗 [HWK Saarland](https://www.hwk-saarland.de/)")

    st.subheader("💼 Aktuelle Jobangebote im Saarland")

    # API-Abfrage für Jobangebote
    api_url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
    headers = {"X-API-Key": "jobboerse-jobsuche"}
    for interesse in interessen:
        st.markdown(f"**{interesse}**")
        params = {
            "wo": "Saarland",
            "was": interesse,
            "size": 5
        }
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            jobs = response.json().get("stellenangebote", [])
            if jobs:
                for job in jobs:
                    titel = job.get("titel", "Kein Titel")
                    arbeitgeber = job.get("arbeitgeber", {}).get("name", "Unbekannt")
                    ort = job.get("arbeitsort", {}).get("ort", "Unbekannt")
                    link = job.get("links", {}).get("details", "#")
                    st.markdown(f"- [{titel}]({link}) bei **{arbeitgeber}** in *{ort}*")
            else:
                st.markdown("Keine aktuellen Angebote gefunden.")
        else:
            st.markdown("Fehler beim Abrufen der Jobangebote.")

    if beratung == "Ja":
        st.subheader("📞 Beratungsmöglichkeiten")
        st.markdown("- Agentur für Arbeit: [www.arbeitsagentur.de](https://www.arbeitsagentur.de)")
        st.markdown("- Berufsberatung vor Ort oder telefonisch")
        st.markdown("- Coaching mit AVGS-Gutschein möglich")

    st.success("✅ Auswertung abgeschlossen. Du kannst deine Angaben anpassen und erneut auswerten.")

