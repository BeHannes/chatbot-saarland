import streamlit as st

st.set_page_config(page_title="Berufsorientierung Saarland", layout="centered")

st.title("💬 Berufsorientierung im Saarland")
st.write("Willkommen! Dieser Chatbot hilft dir bei beruflicher Neuorientierung nach Jobverlust oder drohendem Jobverlust.")

# Schritt 1: Wohnort und Beruf
st.header("1️⃣ Deine aktuelle Situation")
wohnort = st.text_input("In welchem Ort im Saarland wohnst du?")
beruf = st.text_input("Was ist dein aktueller oder letzter Beruf?")
situation = st.selectbox("Wie ist deine aktuelle Lage?", [
    "Ich habe meinen Job verloren",
    "Ich bin von Jobverlust bedroht",
    "Ich möchte mich freiwillig neu orientieren"
])

# Schritt 2: Interessen
st.header("2️⃣ Deine Interessen")
interessen = st.multiselect("Welche Bereiche interessieren dich?", [
    "IT & Digitalisierung",
    "Gesundheit & Soziales",
    "Umwelt & Nachhaltigkeit",
    "Handwerk & Technik",
    "Bildung & Pädagogik",
    "Kaufmännisch & Verwaltung"
])

# Schritt 3: Weiterbildung
st.header("3️⃣ Weiterbildung")
weiterbildung = st.selectbox("Hast du Interesse an einer Weiterbildung oder Umschulung?", [
    "Ja, ich möchte mich weiterbilden",
    "Vielleicht, ich bin mir noch unsicher",
    "Nein, aktuell nicht"
])

# Schritt 4: Beratung
st.header("4️⃣ Beratung")
beratung = st.selectbox("Möchtest du eine persönliche Beratung in Anspruch nehmen?", [
    "Ja, bitte",
    "Vielleicht später",
    "Nein"
])

# Schritt 5: Empfehlungen anzeigen
if st.button("📋 Empfehlungen anzeigen"):
    st.subheader("🔍 Deine Angaben")
    st.write(f"**Wohnort:** {wohnort}")
    st.write(f"**Beruf:** {beruf}")
    st.write(f"**Situation:** {situation}")
    st.write(f"**Interessen:** {', '.join(interessen)}")
    st.write(f"**Weiterbildung:** {weiterbildung}")
    st.write(f"**Beratung:** {beratung}")

    st.subheader("🌱 Branchen mit Zukunft")
    if "IT & Digitalisierung" in interessen:
        st.markdown("- **IT & Digitalisierung**: KI, Cybersecurity, Cloud, Datenanalyse")
    if "Gesundheit & Soziales" in interessen:
        st.markdown("- **Gesundheit & Soziales**: Pflege, Medizintechnik, psychosoziale Beratung")
    if "Umwelt & Nachhaltigkeit" in interessen:
        st.markdown("- **Umwelt & Nachhaltigkeit**: Recycling, erneuerbare Energien, Umwelttechnik")
    if "Handwerk & Technik" in interessen:
        st.markdown("- **Handwerk & Technik**: Gebäudetechnik, Fahrzeugtechnik, SHK")
    if "Bildung & Pädagogik" in interessen:
        st.markdown("- **Bildung & Pädagogik**: Erzieher/in, Bildungscoach, pädagogische Weiterbildungen")
    if "Kaufmännisch & Verwaltung" in interessen:
        st.markdown("- **Kaufmännisch & Verwaltung**: Buchhaltung, Controlling, Projektorganisation")

    st.subheader("🎓 Weiterbildungsangebote")
    st.markdown("- [KURSNET der Agentur für Arbeit](https://kursnet-finden.arbeitsagentur.de)")
    st.markdown("- [Weiterbildungsportal Saarland](https://weiterbildungsportal.saarland/)")
    st.markdown("- [IHK Saarland](https://www.saarland.ihk.de)")
    st.markdown("- [HWK des Saarlandes](https://www.hwk-saarland.de)")

    if beratung == "Ja, bitte":
        st.subheader("📞 Beratungsmöglichkeiten")
        st.markdown("- Agentur für Arbeit: Persönliche Beratung und Bildungsgutschein")
        st.markdown("- IHK/HWK: Beratung zu Umschulungen und Meisterkursen")
        st.markdown("- Jobcenter: Förderprogramme und Coaching")

    st.success("✅ Du kannst diese Informationen nutzen, um deine nächsten Schritte zu planen. Viel Erfolg!")


