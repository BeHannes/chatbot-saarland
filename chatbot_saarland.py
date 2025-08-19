# chatbot_saarland.py

import streamlit as st

st.set_page_config(page_title="Berufsorientierungs-Chatbot Saarland", page_icon="💼", layout="centered")

st.title("💼 Berufsorientierungs-Chatbot Saarland")
st.markdown("""
Willkommen! Dieser Chatbot hilft Menschen im Saarland, die von **Jobverlust** betroffen sind oder sich beruflich **neu orientieren** möchten.

Bitte beantworte die folgenden Fragen, damit wir dir passende Informationen und Empfehlungen geben können.
""")

with st.form("chatbot_form"):
    wohnort = st.text_input("🏠 In welchem Ort im Saarland wohnst du?")
    beruf = st.text_input("🧑‍💼 In welchem Beruf warst du zuletzt tätig?")
    situation = st.selectbox("📉 Was ist deine aktuelle Situation?", [
        "Ich habe meinen Job verloren",
        "Ich bin von Jobverlust bedroht",
        "Ich möchte mich beruflich verändern"
    ])
    interessen = st.text_area("🎯 Welche beruflichen Interessen oder Stärken hast du?")
    weiterbildung = st.selectbox("📚 Bist du offen für Weiterbildung oder Umschulung?", [
        "Ja, ich möchte mich weiterbilden",
        "Vielleicht, ich bin unsicher",
        "Nein, aktuell nicht"
    ])
    beratung = st.selectbox("🤝 Möchtest du persönliche Beratung in Anspruch nehmen?", [
        "Ja, bitte",
        "Vielleicht später",
        "Nein"
    ])
    submitted = st.form_submit_button("Antworten abschicken")

if submitted:
    st.success("✅ Vielen Dank für deine Angaben!")
    st.markdown("### 📝 Deine Zusammenfassung")
    st.write(f"- **Wohnort:** {wohnort}")
    st.write(f"- **Beruf:** {beruf}")
    st.write(f"- **Situation:** {situation}")
    st.write(f"- **Interessen/Stärken:** {interessen}")
    st.write(f"- **Weiterbildungswunsch:** {weiterbildung}")
    st.write(f"- **Beratungswunsch:** {beratung}")

    st.markdown("### 📌 Empfehlungen & Ressourcen")

    st.markdown("""
- 🔗 [Agentur für Arbeit Saarland](https://www.arbeitsagentur.de/vor-ort/saarland) – Beratung, Arbeitslosmeldung, Weiterbildung
- 🔗 [KURSNET](https://kursnet-finden.arbeitsagentur.de/kurs/) – Weiterbildungsangebote in deiner Region
- 🔗 [IHK Saarland](https://www.saarland.ihk.de/) – Informationen zu Umschulungen und beruflicher Neuorientierung
- 🔗 [HWK Saarland](https://www.hwk-saarland.de/) – Angebote für handwerkliche Berufe und Weiterbildung
- 📞 **Hotline der Agentur für Arbeit:** 0800 4 5555 00 (kostenfrei)
""")

    st.markdown("💬 Wenn du möchtest, kannst du deine Angaben speichern oder mit einer Beratungsstelle teilen.")

    st.info("👉 Dies ist ein Prototyp. Für eine persönliche Beratung empfehlen wir den Kontakt zur Agentur für Arbeit oder IHK/HWK.")


